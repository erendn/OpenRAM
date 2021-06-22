#!/usr/bin/env python3

import sys
from gdsMill import gdsMill

if len(sys.argv) < 4:
    print("Script to prefix every instance and structure with the root cell name to provide unique namespace.")
    print("Usage: {0} in.gds out.gds".format(sys.argv[0]))
    sys.exit(1)

prefix = sys.argv[1]

gds_file = sys.argv[2]
gds = gdsMill.VlsiLayout()
reader = gdsMill.Gds2reader(gds)
reader.loadFromFile(gds_file)

gds.uniquify()

writer = gdsMill.Gds2writer(gds)
writer.writeToFile(sys.argv[3])
