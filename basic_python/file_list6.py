#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, glob

class FileInformation( object ):

    def __init__( self, fname):
        self.fname = fname

    def _str__( self ):
        return "[file]: %s" % self.fname

def each_file( dir ):

    for fname in glob.glob( "%s/*" % dir ):

        if os.path.isfile( fname ):
            yield FileInformation( fname )

        if os.path.isdir( fname ):
            for finfo in each_file( fname ):
                yield finfo

    raise StopIteration

if __name__ == '__main__':

    target_dir = sys.argv[1]

    for finfo in each_file( target_dir ):
        print( finfo )