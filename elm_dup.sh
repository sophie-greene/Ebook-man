#!/bin/bash
#find /media/some/sophie-hhd/books/pdf2epub -type f -iname "*.epub" | parallel -j8 ./elm_dup.sh {} /media/some/sophie-hhd/books/thrill/ /media/some/sophie-hhd/books/pdfproc/ /media/some/sophie-hhd/books/pdfdup/ \;
#use as above
#file name
name=$1
#path where a duplicate might be found
epath=$2
#path where the original pdf is
ppath=$3
#path where the original should be moved
rpath=$4
mname="$(basename "$name")"
ename="$epath${mname%.*}.epub"
#orig pdf
pname="$ppath${mname%.*}.pdf"
rname="$rpath${mname%.*}.pdf"
if [ -f "$ename" ] ;
then
	rm "$name"
	mv "$pname" "$rname"
	echo "$mname ...... done"
	
fi




