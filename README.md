# eot-s3-stats
Script to calculate sizes and counts from S3 file list.

## Gathering file list from s3

Using the aws command line tool we will gather the file listing for a specific EOT year. 

In the example below we are gathering the EOT-2012 file listing. 

```bash
aws s3 ls s3://eotarchive/crawl-data/EOT-2012/ --recursive  > EOT-2012-S3.txt
```

## Calucluating statistics. 

Once we have the EOT year file listing we can generate the statistics. 

```bash

python3 eot-s3-stats.py EOT-2012-S3.txt
```

This will result in an output that looks like this. 

```
EOT Year: {'EOT-2012'}

File Sizes
##########
warc_size: 41.42 TB
wat_size: 885.15 GB
wet_size: 217.3 GB
cdx_size: 12.27 GB

File Counts
###########
warc_count: 78509
wat_count: 78509
wet_count: 78509
cdx_count: 78509
```
