import sys
import os.path
import re

if 2 != len(sys.argv) or sys.argv[1][-2:] != '.h':
    print "usage: %s <ClassHeader.h>" % os.path.basename(sys.argv[0])
    print
    print "Given an class header file, extract the properties and generate an NSCoding implementation."
    sys.exit(1)

PROPERTY_MATCHER = re.compile(r'\@property *(\(.*\))? *(?P<type>.*) +\*?(?P<name>.*);')


def encoderForClass(klass):
    if klass in ('bool', 'BOOL'):
        return 'encodeBool'
    return 'encodeObject'


def decoderForClass(klass):
    if klass in ('bool', 'BOOL'):
        return 'decodeBoolForKey'
    return 'decodeObjectForKey'


props = []
with open(sys.argv[1], 'rb') as handle:
    for line in handle:
        match = PROPERTY_MATCHER.search(line)
        if match:
            props.append({
                "class": match.group('type'),
                "name": match.group('name'),
                "keyName": match.group('name')[0].upper() + match.group('name')[1:],
                "encoder": encoderForClass(match.group('type')),
                "decoder": decoderForClass(match.group('type'))
            })

print "#pragma mark - NSCoding"
print

for prop in props:
    print '#define k%(keyName)s  @"%(keyName)s"' % prop

print
print '- (void)encodeWithCoder:(NSCoder *)encoder {'

for prop in props:
    print '    [encoder %(encoder)s forKey:k%(keyName)s];' % prop

print '}'
print

print '- (id)initWithCoder:(NSCoder *)decoder {'
print '    self = [self init];'
for prop in props:
    print '    self.%(name)s = [decoder %(decoder)s:k%(keyName)s];' % prop
print '    return self;'
print '}'
