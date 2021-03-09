#!/usr/bin/env ruby
import zlib
import sys

data_file = sys.argv[1]

data = open(data_file, "rb").read()
deco = zlib.decompress(data)

wrfd = open(data_file + ".dec", "w")

wrfd.write(deco.decode("utf8"))
wrfd.close()
print("Data {} decompressed to {}".format(data_file, data_file + ".dec"))
