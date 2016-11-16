#!/bin/bash
#find /media/some/sophie-hhd/books/pdf2epub -type f -iname "*.epub" | parallel -j8 ./filescanner.sh {} \;
#use as above
#file name
name=$1
s="$(clamscan "$name")"
echo "$name ....is .. $s"
