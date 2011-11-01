#!/usr/bin/python
#
# Copyright 2011 Tony Scelfo. All Rights Reserved.

"""Script to parse reader following json to link to plus profiles.

Script that iterates the following json dump from reader to make links
to G+ profiles so it is easy to make a circle with the people you used
to follow.
"""

__author__ = 'scelfo@gmail.com (Tony Scelfo)'

import json
import sys


NAME_AND_PROFILE = '%s: https://plus.google.com/%s'

PROFILE_CARD_IFRAME = (
    '<iframe width="301px"'
    'src="http://www.google.com/s2/u/0/widgets/ProfileCard?uid=%s&bc=0"'
    'frameborder="0"></iframe>')


def main(argv):
  if len(argv) < 2:
    print 'must specify an input file'
    sys.exit()

  input_file = argv[1]

  print 'Going to read from %s...' % input_file

  f = open(input_file, 'r')
  parsed_json = json.load(f)

  for friend in parsed_json['friends']:
    if 'profileIds' in friend:
      # Friends can have more than one profileId, the first seems to be the
      # one that google+ wants.
      id = friend['profileIds'][0]
      if True:
        print PROFILE_CARD_IFRAME % id
      else:
        print NAME_AND_PROFILE % (friend['displayName'], id)


if __name__ == '__main__':
  main(sys.argv)
