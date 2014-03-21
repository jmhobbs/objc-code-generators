objc-code-generators
====================

Code generators for Objective-C because I don't know any better.

If there are better ways to do these, please let me know.

## nscoding-helper.py

Given a class header, generate an NSCoding implementation.

      usage: nscoding-helper.py <ClassHeader.h>

### Person.h

```objc
//
//  Person.h
//
//  Created by John Hobbs on 1/15/14.
//  Copyright (c) 2014 John Hobbs. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Person : NSObject <NSCoding>

@property NSNumber *id;
@property NSString *name;
@property NSURL *homepageURL;
@property bool usesPython;

@end
```

### Output

```objc
#pragma mark - NSCoding

#define kId  @"Id"
#define kName  @"Name"
#define kHomepageURL  @"HomepageURL"
#define kUsesPython  @"UsesPython"

- (void)encodeWithCoder:(NSCoder *)encoder {
    [encoder encodeObject forKey:kId];
    [encoder encodeObject forKey:kName];
    [encoder encodeObject forKey:kHomepageURL];
    [encoder encodeBool forKey:kUsesPython];
}

- (id)initWithCoder:(NSCoder *)decoder {
    self = [self init];
    self.id = [decoder decodeObjectForKey:kId];
    self.name = [decoder decodeObjectForKey:kName];
    self.homepageURL = [decoder decodeObjectForKey:kHomepageURL];
    self.usesPython = [decoder decodeBoolForKey:kUsesPython];
    return self;
}
```
