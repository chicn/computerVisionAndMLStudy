#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, glob

target_dir = sys.argv[1]

for fname in glob.glob( "%s/*" % target_dir ):
    if os.path.isfile( fname ):
        print( "[file]: %s" % fname )

    if os.path.isdir( fname ):
        print( "[dir]: %s" % fname )
    