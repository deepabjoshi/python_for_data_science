import gzip
import shutil
import bz2
import tarfile
import string
import random

content = b"Hello World!"
gzip_file = "/tmp/myfile.gz"
with gzip.open(gzip_file, 'wb') as fo:
    fo.write(content)

with gzip.open(gzip_file, 'rb') as fi:
    file_content = fi.read()
    print(file_content)

txt_file = "/tmp/myfile.txt"
gzip_txt_file = txt_file + '.gz'
with open(txt_file, 'rb') as fi:
    with gzip.open(gzip_txt_file, 'wb') as fo:
        shutil.copyfileobj(fi, fo)

with gzip.open(gzip_txt_file, 'rb') as fi:
    file_content = fi.read()
    print(file_content)

l = 1000
str1 = bin(''.join(random.choices("{0}{1}".format(string.ascii_letters, string.digits), k=l)))

compr_str = gzip.compress(str1)
print(gzip.decompress(compr_str))
print(len(str1) / len(compr_str))

bz2_compr_str = bz2.compress(str1)
uncompr_str = bz2.decompress(bz2_compr_str)
print(uncompr_str)
print(uncompr_str == str1)
print(len(str1) / len(bz2_compr_str))




