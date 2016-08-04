#! /bin/bash

#BACKUPS_FOLDER="/home/vagrant/backups/"
BACKUPS_FOLDER="/mnt/backups/"

curl -v -XPUT spider-verse:9200/_snapshot/categorizing_backup?pretty=True \
-d '
{
    "type": "fs",
    "settings": {
        "location": "/mnt/backups/",
        "compress": "true"
    }
}
'
