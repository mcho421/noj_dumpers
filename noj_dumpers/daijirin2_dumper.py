#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string
import sys

import eb
from daijirin2_gaiji import DAIJIRIN2_GAIJI
from daijirin2_dirty_data import DAIJIRIN2_DIRTY_DATA
from abstract_epwing_dumper import AbstractEpwingDumper

__version__ = "1.0.0a"

class Daijirin2Dumper(AbstractEpwingDumper):
    """Dump Super Daijirin 2 EPWING Dictionary into a file.
    Sanitises the output for re-importing with Importer"""
    def __init__(self, dictdir, outfile):
        super(Daijirin2Dumper, self).__init__(dictdir, outfile)

    @property
    def first_pos(self):
        return (137772, 1054)

    @property
    def last_pos(self):
        return (157295, 162)

    @property
    def gaiji(self):
        return DAIJIRIN2_GAIJI

    @property
    def dirty_data(self):
        return DAIJIRIN2_DIRTY_DATA

    @staticmethod
    def get_title():
        return u"三省堂　スーパー大辞林"

    @staticmethod
    def get_version():
        return __version__

        
def main():
    dictdir = 'C:\\Users\\Mathew\\ISO\\[EPWING] Daijirin'
    outfile = open('daijirindump.txt', 'w')
    dumper = Daijirin2Dumper(dictdir, outfile)

    import progressbar as pb
    widgets = ['Dumping: ', pb.Percentage(), ' ', pb.Bar(),
               ' ', pb.Timer(), ' ']
    pbar = pb.ProgressBar(widgets=widgets, maxval=len(dumper)).start()

    for i in dumper.dump_generator():
        pbar.update(i)
    pbar.finish()

if __name__ == '__main__':
    main()
