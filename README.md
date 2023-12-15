# GETTING STARTED
start with data-init notebook to split original data into some basic starting features

# USEFUL COMMANDS

```
# sync bucket contents to local dir (add the dir to .gitignore)
aws s3 sync s3://<bucketname>/ bucket-dump/

# replace data in bucket with new parquet copies from local /data dir
for file in data/*.parquet; do { aws s3 cp $file s3://<bucketname>/; } done
```
