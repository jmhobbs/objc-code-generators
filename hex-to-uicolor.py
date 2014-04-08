import sys
import os

if 2 != len(sys.argv):
    print "usage: %s <hex color>" % os.path.basename(sys.argv[0])
    print
    print "Given an HTML hex color, print out a UIColor."
    sys.exit(1)

hex_color = sys.argv[1].strip().strip("#")

r = int(hex_color[:2], 16)
g = int(hex_color[2:4], 16)
b = int(hex_color[4:], 16)

print "// #%s" % hex_color
print "[[UIColor alloc] initWithRed:%0.2ff green:%0.2ff blue:%0.2ff alpha:1.0f];" % (r / 255.0, g / 255.0, b / 255.0)
