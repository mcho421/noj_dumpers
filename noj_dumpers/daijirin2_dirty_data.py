#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textwrap import dedent
from eb import EB_HOOK_NARROW_FONT, EB_HOOK_WIDE_FONT

DAIJIRIN2_DIRTY_DATA = [
    (dedent(u"""\
        <HEAD>ぐ・む</HEAD> （接尾）〔動詞五［四］段型活用〕
        <INDENT=4>"""),
     dedent(u"""\
        <HEAD>ぐ・む</HEAD> （接尾）
        <INDENT=4>〔動詞五［四］段型活用〕
        """)
    ), (
        u"""<HEAD>しも</HEAD> （助動）（しも（しま）・しも（しもう）・しも（しもう）・しも（しもう）・しまえ・しめ（しまえ））""",
        u"""<HEAD>しも</HEAD> （助動）(しも（しま）・しも（しもう）・しも（しもう）・しも（しもう）・しまえ・しめ（しまえ）)"""
    ), (
        u"""<HEAD>うれわ・し</HEAD> ウレハシ 【憂はし】 （形）シク""",
        u"""<HEAD>うれわ・し</HEAD> ウレハシ 【憂はし】 （形シク）"""
    ), (
        u"""<HEAD>え-ほう</HEAD> ヱハウ [0] 【恵方】 ・ エハウ 【吉方・兄方】""",
        u"""<HEAD>え-ほう</HEAD> [0] ヱハウ 【恵方】 ・ エハウ 【吉方・兄方】"""
    ), (
        u"""<HEAD>がか・る</HEAD> （接尾）（動詞五［四］段型活用）""",
        u"""<HEAD>がか・る</HEAD> （接尾・動五［四］）"""
    ), (
        u"""<HEAD>ひこ-ひこ</HEAD> （副） （名）スル""",
        u"""<HEAD>ひこ-ひこ</HEAD> （副・名）スル"""
    ), (
        u"""<HEAD>びこ-びこ</HEAD> （副） （名）スル""",
        u"""<HEAD>びこ-びこ</HEAD> （副・名）スル"""
    ), (
        u"""<HEAD>ぽか-ぽか</HEAD> [1] （副） （名）スル""",
        u"""<HEAD>ぽか-ぽか</HEAD> [1] （副・名）スル"""
    ), (
        u"""<HEAD>かんねん-がく</HEAD> クワン― [3] 【観念学】 〖(フランス) idéologie〗""",
        u"""<HEAD>かんねん-がく</HEAD> クワン― [3] 【観念学】"""
    ), (
        u"""<HEAD>さっしゃる</HEAD> （助動）(さつしやら（さつしやろ・さつしやれ）・さつしやり（さつしやつ・さつしやい・さつしやれ）・さつしやる（さつしやるる）・さつしやる（さつしやるる）・さつし(やれ（さつしやるれ）・さつしやれ（さつしやれい・さつしやい）)""",
        u"""<HEAD>さっしゃる</HEAD> （助動）(さつしやら（さつしやろ・さつしやれ）・さつしやり（さつしやつ・さつしやい・さつしやれ）・さつしやる（さつしやるる）・さつしやる（さつしやるる）・さつしやれ（さつしやるれ）・さつしやれ（さつしやれい・さつしやい）)"""
    ), (
        u"""<HEAD>ぶ・る</HEAD> 【振る】 [1] （動ラ五［四］）""",
        u"""<HEAD>ぶ・る</HEAD> [1] 【振る】 （動ラ五［四］）"""
    ), (
        u"""<HEAD>や</HEAD> 【野】 [1]""",
        u"""<HEAD>や</HEAD> [1] 【野】"""
    ), (
        u"""<INDENT=1><HEAD>""",
        u"""<INDENT=1><PAGE><HEAD>"""
    )
]

def main():
    text = dedent(u"""\
        <INDENT=1><PAGE><HEAD>ぐ・む</HEAD> （接尾）〔動詞五［四］段型活用〕
        <INDENT=4>名詞に付いて，そのもののきざしが現れてくる，それが現れ始めるなどの意を表す。「涙―・む」「芽―・む」
        <INDENT=1><PAGE><HEAD>しも</HEAD> （助動）（しも（しま）・しも（しもう）・しも（しもう）・しも（しもう）・しまえ・しめ（しまえ））
        <INDENT=1><PAGE><HEAD>うれわ・し</HEAD> ウレハシ 【憂はし】 （形）シク
        <INDENT=1><PAGE><HEAD>え-ほう</HEAD> ヱハウ [0] 【恵方】 ・ エハウ 【吉方・兄方】
        <INDENT=1><PAGE><HEAD>がか・る</HEAD> （接尾）（動詞五［四］段型活用）
        <INDENT=1><PAGE><HEAD>ひこ-ひこ</HEAD> （副） （名）スル
        <INDENT=1><PAGE><HEAD>びこ-びこ</HEAD> （副） （名）スル
        <INDENT=1><PAGE><HEAD>ぽか-ぽか</HEAD> [1] （副） （名）スル
        <INDENT=1><PAGE><HEAD>かんねん-がく</HEAD> クワン― [3] 【観念学】 〖(フランス) idéologie〗
        <INDENT=1><PAGE><HEAD>さっしゃる</HEAD> （助動）(さつしやら（さつしやろ・さつしやれ）・さつしやり（さつしやつ・さつしやい・さつしやれ）・さつしやる（さつしやるる）・さつしやる（さつしやるる）・さつし(やれ（さつしやるれ）・さつしやれ（さつしやれい・さつしやい）)
        <INDENT=1><PAGE><HEAD>ぶ・る</HEAD> 【振る】 [1] （動ラ五［四］）
        <INDENT=1><PAGE><HEAD>や</HEAD> 【野】 [1]
        """)


    for find, replace in DAIJIRIN2_DIRTY_DATA:
        text = text.replace(find, replace)
    print text

if __name__ == '__main__':
    main()

