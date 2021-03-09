#!/usr/bin/env ruby
import zlib
import sys

data_file = sys.argv[1]

data = open(data_file, "r").read()
deco = zlib.compress(data.encode("utf8"))

wrfd = open(data_file + ".compressed", "wb")
wrfd.write(deco)
wrfd.close()
print("Data {} compressed to {}".format(data_file, data_file + ".compressed"))
