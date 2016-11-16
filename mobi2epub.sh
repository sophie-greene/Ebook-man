#!/bin/bash
#find /media/some/sophie-hhd/books/mobi/ -type f -iname "*.mobi" | parallel -j8 ./mobi2epub.sh {} /media/some/sophie-hhd/books/epub/ \;
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



