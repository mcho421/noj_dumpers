#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import eb
import progressbar as pb
from daijirin2_dumper import Daijirin2Dumper
from wadai5_dumper import Wadai5Dumper

__version__ = '1.0.0a'

HELPTEXT = """An EPWING dictionary dumper.

This writes the contents of the specified EPWING dictionary to a text file.
See --version for supported EPWING dictionaries.

This dumper is compatible with the Natural Order Japanese suite of tools.
After dumping, use the converter tool to convert the dump file into an 
appropriate format for importing."""

DUMPERS = [Daijirin2Dumper, Wadai5Dumper]

class EpwingNotSupported(Exception): pass

class VersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print "noj_dumper v{}\n".format(__version__)
        print "Supported EPWING dictionaries and dumper versions:"
        for d in DUMPERS:
            print u"v{} -- {}".format(d.get_version(), d.get_title())
        sys.exit(0)


def parse_epwing_dir(parser, arg):
    if not os.path.isdir(arg):
        parser.error("Directory does not exist: \"{}\"".format(arg))
    else:
        return arg

def get_epwing_title(dictdir):
    eb.eb_initialize_library()
    book     = eb.EB_Book()
    appendix = eb.EB_Appendix() 
    hookset  = eb.EB_Hookset()

    eb.eb_bind(book, dictdir)
    eb.eb_set_subbook(book, 0)

    title = eb.eb_subbook_title(book).decode('euc-jp')

    eb.eb_finalize_library()
    return title

def dumper_factory(dictdir, outfile):
    title = get_epwing_title(dictdir)
    for d in DUMPERS:
        if title == d.get_title():
            return d(dictdir, outfile)
    raise EpwingNotSupported(u"EPWING dictionary \"{}\" not supported.".format(
        title))
    return None

# TODO -c --stdout Write output to stdout
# TODO -f --force Force overwriting of output file

def main():
    parser = argparse.ArgumentParser(description=HELPTEXT)
    parser.add_argument('--version', action=VersionAction,
        help="show dumper version numbers", nargs=0)
    parser.add_argument("EPWING_DIR", help="directory to the EPWING folder",
        type=lambda x : parse_epwing_dir(parser, x))
    parser.add_argument("-o", "--output", help="data dumped to this file",
        type=argparse.FileType('w'))
    args = parser.parse_args()

    try:
        outfile = args.output
        if outfile is None:
            outfile = open('out', 'w')
        dictdir = args.EPWING_DIR

        dumper = dumper_factory(dictdir, outfile)
        print u"Loaded EPWING dictionary: \"{}\"".format(dumper.get_title())
        print u"Dumper version for above dictionary: {}".format(dumper.get_version())
        print u"Dumping to file: \"{}\"".format(outfile.name)
        print

        widgets = ['Dumping: ', pb.Percentage(), ' ', pb.Bar(),
                   ' ', pb.Timer(), ' ']
        pbar = pb.ProgressBar(widgets=widgets, maxval=len(dumper)).start()

        for i in dumper.dump_generator():
            pbar.update(i)
        pbar.finish()
    except eb.EBError, (error, message):
        code = eb.eb_error_string(error)
        sys.stderr.write("{}: error: {}: {}\n".format(sys.argv[0], code, message))
        sys.exit(1)
    except EpwingNotSupported as e:
        sys.stderr.write(e.message + '\n')
        sys.exit(1)


if __name__ == '__main__':
    main()
