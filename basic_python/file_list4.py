#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, glob

def print_file_list( dir ):

    for fname in glob.glob( "%s/*" % target_dir ):
        if os.path.isfile( fname ):
            print( "[file]: %s" % fname )

        if os.path.isdir( fname ):
            print( "[dir]: %s" % fname )
            print_file_list( fname )
        

target_dir = sys.argv[1]

print_file_list( target_dir )




# yield: 呼び出しもとに戻ってフィードバックを渡す