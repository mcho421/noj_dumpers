noj_dumper Readme
==============================================================================

What is noj_dumper?
---------------
noj_dumper is a command line program that allows you to dump EPWING 
dictionaries to a file. This dumper is compatible with the Natural Order
Japanese suite of tools and is the first step to importing an EPWING dictionary
into the lookup program. Use the converter tool to convert the dump file to an
appropriate format for importing.

The following EPWING dictionaries are currently supported:
- "研究社　新和英大辞典　第５版"
- "三省堂　スーパー大辞林"

Installation / How to use
-------------------------
These instructions are for Windows users. The instructions should be similar
for Mac and Linux.

- Windows users make sure your command prompt can display Japanese characters.
  One way this can be achieved is by setting your system locale to Japanese.

1) Unzip noj_dumper.

2) Open a console in the noj_dumper directory, and run noj_dumper.exe with 
   the path to an EPWING dictionary, e.g.
   
   $ noj_dumper "C:\EPWING\Daijirin"
   
   This should dump the dictionary to a file named "out".

For more information run with the -h flag.

Official Repository
-------------------
https://github.com/mcho421/noj_dumper (tentative)

Contact
-------
Mathew Chong
mathewchong.dev@gmail.com

Credits
-------
cb4960
    Gaiji data for EPWING dictionaries
    http://rikaisama.sourceforge.net/
aehlke
    Python binding for eb library
    https://github.com/aehlke/ebmodule
Motoyuki Kasahara
    Eb library
    http://www.sra.co.jp/people/m-kasahr/eb/index.html


