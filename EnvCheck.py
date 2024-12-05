import sys
import os

if sys.prefix != sys.base_prefix:
   print("##Virtual##")
else:
   print("NOT Virtual")

