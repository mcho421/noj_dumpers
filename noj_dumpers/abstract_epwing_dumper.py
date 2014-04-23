#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import re
import string
import sys
import eb

UNKNOWN_SYMBOL = '�'

class abstractstatic(staticmethod):
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True

class AbstractEpwingDumper(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, dictdir, outfile):
        super(AbstractEpwingDumper, self).__init__()
        self._stop = False
        self.dictdir = dictdir
        self.outfile = outfile

        eb.eb_initialize_library()
        self.book     = eb.EB_Book()
        self.appendix = eb.EB_Appendix() 
        self.hookset  = eb.EB_Hookset()

        eb.eb_set_hooks(self.hookset, (
            (eb.EB_HOOK_NARROW_FONT, self._hook_font),
            (eb.EB_HOOK_WIDE_FONT, self._hook_font),
            (eb.EB_HOOK_BEGIN_REFERENCE, self._hook_begin_reference),
            (eb.EB_HOOK_END_REFERENCE, self._hook_end_reference),
            (eb.EB_HOOK_SET_INDENT, self._hook_set_indent),
            (eb.EB_HOOK_BEGIN_KEYWORD, self._hook_begin_keyword),
            (eb.EB_HOOK_END_KEYWORD, self._hook_end_keyword),
            (eb.EB_HOOK_BEGIN_SUPERSCRIPT, self._hook_begin_superscript),
            (eb.EB_HOOK_END_SUPERSCRIPT, self._hook_end_superscript),
            (eb.EB_HOOK_BEGIN_SUBSCRIPT, self._hook_begin_subscript),
            (eb.EB_HOOK_END_SUBSCRIPT, self._hook_end_subscript),
            (eb.EB_HOOK_BEGIN_DECORATION, self._hook_begin_emphasis),
            (eb.EB_HOOK_END_DECORATION, self._hook_end_emphasis),
            (eb.EB_HOOK_BEGIN_MONO_GRAPHIC, self._hook_begin_mono_graphic),
            (eb.EB_HOOK_END_MONO_GRAPHIC, self._hook_end_mono_graphic),
            (eb.EB_HOOK_BEGIN_COLOR_BMP, self._hook_begin_color_bmp),
            (eb.EB_HOOK_BEGIN_COLOR_JPEG, self._hook_begin_color_jpeg),
            (eb.EB_HOOK_END_COLOR_GRAPHIC, self._hook_end_color_graphic),
            (eb.EB_HOOK_BEGIN_WAVE, self._hook_begin_wave),
            (eb.EB_HOOK_END_WAVE, self._hook_end_wave),
        ))

        try:
            eb.eb_bind(self.book, self.dictdir)
        except eb.EBError, (error, message):
            code = eb.eb_error_string(error)
            sys.stderr.write("Error: %s: %s\n" % (code, message))
            sys.exit(1)
        eb.eb_set_subbook(self.book, 0)

    @abc.abstractproperty
    def first_pos(self):
        pass

    @abc.abstractproperty
    def last_pos(self):
        pass

    @abc.abstractproperty
    def gaiji(self):
        pass

    @property
    def dirty_data(self):
        return list()

    @abstractstatic
    def get_title():
        pass

    @abstractstatic
    def get_version():
        pass

    @staticmethod
    def get_format():
        return "1"

    def _hook_font(self, book, appendix, container, code, argv):
        if (code, argv[0]) in self.gaiji:
            replacement = "{{0x{}}}".format(
                    self.gaiji[(code, argv[0])].encode('hex'))
        else:
            replacement = "{{0x{}}}".format(UNKNOWN_SYMBOL.encode('hex'))
        eb.eb_write_text_string(book, replacement)
        return eb.EB_SUCCESS

    def _hook_begin_reference(self, book, appendix, container, code, argv):
         eb.eb_write_text_string(book, "<LINK>")
         return eb.EB_SUCCESS

    def _hook_end_reference(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</LINK[{:d}:{:d}]>".format(
            argv[1], argv[2]))
        return eb.EB_SUCCESS

    def _hook_set_indent(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<INDENT={:d}>".format(
            argv[1]))
        return eb.EB_SUCCESS

    def _hook_begin_keyword(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<HEAD>")
        return eb.EB_SUCCESS

    def _hook_end_keyword(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</HEAD>")
        return eb.EB_SUCCESS

    def _hook_begin_superscript(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<SUP>")
        return eb.EB_SUCCESS

    def _hook_end_superscript(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</SUP>")
        return eb.EB_SUCCESS

    def _hook_begin_subscript(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<SUB>")
        return eb.EB_SUCCESS

    def _hook_end_subscript(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</SUB>")
        return eb.EB_SUCCESS

    def _hook_begin_emphasis(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<B>")
        return eb.EB_SUCCESS

    def _hook_end_emphasis(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</B>")
        return eb.EB_SUCCESS

    def _hook_begin_mono_graphic(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<FIG>")
        return eb.EB_SUCCESS

    def _hook_end_mono_graphic(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</FIG>")
        return eb.EB_SUCCESS

    def _hook_begin_color_bmp(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<FIG>")
        return eb.EB_SUCCESS

    def _hook_begin_color_jpeg(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<FIG>")
        return eb.EB_SUCCESS

    def _hook_end_color_graphic(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</FIG>")
        return eb.EB_SUCCESS

    def _hook_begin_wave(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "<WAV>")
        return eb.EB_SUCCESS

    def _hook_end_wave(self, book, appendix, container, code, argv):
        eb.eb_write_text_string(book, "</WAV>")
        return eb.EB_SUCCESS

    def _get_content(self):
        buffer = []
        while 1:
            data = eb.eb_read_text(self.book, self.appendix, 
                    self.hookset, None)
            if not data:
                break
            buffer.append(data)
        data = string.join(buffer, "")
        return data

    def _replace_gaiji_hex_sub_helper(self, match):
        """Returns the utf-8 gaiji given the utf-8 hex code
        for the gaiji"""
        return match.group(1).decode('hex').decode('utf-8')

    def _replace_gaiji_hex(self, unicode_string):
        """Given a unicode string, replace all instances of gaiji
        hexadecimal tags to appropriate UTF-8 gaiji. Returns 
        a new string with all gaiji hex tags replaced with gaiji"""
        #print re.findall("{0x[0-9a-f]+}", unicode_string)
        return re.sub(ur'{0x([0-9a-f]+)}', 
                self._replace_gaiji_hex_sub_helper, unicode_string)

    def stop_dump(self):
        self._stop = True

    def sanitize_dirty_data(self, text):
        for find, replace in self.dirty_data:
            text = text.replace(find, replace)
        return text


    def write_metadata(self):
        self.outfile.write("FORMAT: {}\n".format(self.get_format()))
        self.outfile.write("TITLE: {}\n".format(self.get_title().encode('utf-8')))
        self.outfile.write("VERSION: {}\n".format(self.get_version()))
        self.outfile.write('\n')

    def dump_generator(self):
        self.write_metadata()
        pos = self.first_pos
        eb.eb_seek_text(self.book, pos)
        while pos < self.last_pos:
            if self._stop == True:
                print "Dumping Stopped"
                return

            content = self._get_content() + "<PAGE>"
            unicode_content = content.decode('euc-jp', errors='ignore')
            unicode_content = self._replace_gaiji_hex(unicode_content)
            unicode_content = self.sanitize_dirty_data(unicode_content)
            self.outfile.write(unicode_content.encode('utf-8', errors='ignore'))
            pos = eb.eb_tell_text(self.book)
            # print(pos)
            # print >>self.outfile, pos
            # eb.eb_seek_text(self.book, (pos[0], pos[1]-2))
            eb.eb_seek_text(self.book, (pos[0], pos[1]))
            yield pos[0] - self.first_pos[0]
        self.outfile.close()

    def __len__(self):
        return self.last_pos[0] - self.first_pos[0]
