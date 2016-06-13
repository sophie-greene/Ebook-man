#!/bin/bash
#find /media/some/sophie-hhd/books/thrill/ -type f -iname "*.pdf" | parallel -j8 ./pdf2epub.sh {} /media/some/sophie-hhd/books/pdf2epub/ \;
#use as above
name=$1
epath=$2
mname="$(basename "$name")"
ename="$epath${mname%.*}.epub"
tmp="/tmp/${mname%.*}.epub"
if [ ! -f "$ename" ] ;
then

	ebook-convert "$name" "$tmp" >/dev/null
	mv "$tmp" "$ename"
	echo "converting $mname .....done"
	
fi
cp -n "$name" "/media/some/sophie-hhd/books/pdfproc/$mname"
rm "$name"



