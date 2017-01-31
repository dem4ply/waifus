#! /bin/bash

FILES=$(find . -name "*.template.json")

for f in $FILES
do
	index=${f%.*}
	index=${index%.*}
	index=${index##*/}
	echo $index
	curl -XPUT http://spiderman:9200/_template/$index -d@$f
done
