#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string
import sys

import eb
from wadai5_gaiji import WADAI5_GAIJI
from abstract_epwing_dumper import AbstractEpwingDumper

__version__ = "1.0.0a"

class Wadai5Dumper(AbstractEpwingDumper):
    """Dump Kenkyusha 5th EPWING Dictionary into a file.
    Sanitises the output for re-importing with Importer"""
    def __init__(self, dictdir, outfile):
        super(Wadai5Dumper, self).__init__(dictdir, outfile)

    @property
    def first_pos(self):
        return (108260, 1608)

    @property
    def last_pos(self):
        return (159979, 1882)

    @property
    def gaiji(self):
        return WADAI5_GAIJI

    @staticmethod
    def get_title():
        return u"研究社　新和英大辞典　第５版"
        
    @staticmethod
    def get_version():
        return __version__

        
def main():
    dictdir = 'C:\\Users\\Mathew\\ISO\\[EPWING] KenKyuSha 5th'
    outfile = open('kendump.txt', 'w')
    dumper = Wadai5Dumper(dictdir, outfile)
    
    import progressbar as pb
    widgets = ['Dumping: ', pb.Percentage(), ' ', pb.Bar(),
               ' ', pb.Timer(), ' ']
    pbar = pb.ProgressBar(widgets=widgets, maxval=len(dumper)).start()

    for i in dumper.dump_generator():
        pbar.update(i)
    pbar.finish()

if __name__ == '__main__':
    main()
