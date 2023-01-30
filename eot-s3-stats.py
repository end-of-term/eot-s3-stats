import fileinput
import math
import re

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0 B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

warc_size = 0
warc_count = 0
wat_size = 0
wat_count = 0
wet_size = 0
wet_count = 0
cdx_size = 0
cdx_count = 0
eot_year = set()

eot_year_reg = re.compile(r'\/EOT-\d\d\d\d\/')

for line in fileinput.input():
    line = line.strip()
    s3_date, s3_time, s3_size, s3_name = line.split()

    if '/warc/' in s3_name:
        warc_size += int(s3_size)
        warc_count += 1
    elif '/wet/' in s3_name:
        wet_size += int(s3_size)
        wet_count += 1
    elif '/wat/' in s3_name:
        wat_size += int(s3_size)
        wat_count += 1
    elif '/cdx/' in s3_name:
        cdx_size += int(s3_size)
        cdx_count += 1
    found_year = eot_year_reg.search(s3_name).group()
    eot_year.add(found_year.strip('/'))
  
print('EOT Year:', eot_year)
print('\nFile Sizes\n##########')
print('warc_size:', convert_size(warc_size))
print('wat_size:', convert_size(wat_size))
print('wet_size:', convert_size(wet_size))
print('cdx_size:', convert_size(cdx_size))
print('\nFile Counts\n###########')
print('warc_count:', warc_count)
print('wat_count:', wat_count)
print('wet_count:', wet_count)
print('cdx_count:', cdx_count)
