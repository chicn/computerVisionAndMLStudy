#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, glob

target_dir = sys.argv[1]

for fname in glob.glob( "%s/*" % target_dir ):
    print( fname )