#!/bin/bash
pyinstaller --onefile noj_dumpers/noj_dumper.py
cp gpl.txt dist
cp COPYING dist
cp changes.txt dist
cp README.md dist/README.txt
