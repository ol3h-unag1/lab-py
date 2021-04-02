SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
   '''Convert a file size to human-readable form.
      Keyword arguments:
      size -- file size in bytes
      a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
      if False, use multiples of 1000
      Returns: string
   '''
   if size < 0:
      raise ValueError('number must be non-negative')

   multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
   for suffix in SUFFIXES[multiple]:
      size /= multiple
      if size < multiple:
         return '{0:.2f} {1}'.format(size, suffix)

   raise ValueError('number too large')

###################################################
###################################################

def increment_value( val ):
   return val + 1

def to_bool( anything ):
   if anything: return True
   else: return False

###################################################
###################################################

import re # !build_match_apply_function

def build_match_apply_function(pattern, search, replace):
   
   def matches_rule(noun):
      return re.search(pattern, noun)
   def apply_rule(noun):
      return re.sub(search, replace, noun)

   return (matches_rule, apply_rule)

def rules(file_path):
   with open(file_path, encoding = 'utf-8') as plur_pattern_file:
      for line in plur_pattern_file:
         pattern, search, replace = line.split(None,3)
         yield build_match_apply_function(pattern, search, replace)

import os # !plural

plur_patterns_filename = 'pluralization_rules.txt'

def plural(noun, patterns_file_path = os.path.join( os.path.dirname(os.path.realpath(__file__)), plur_patterns_filename)):
   for match_rule, apply_rule in rules(patterns_file_path):
      if match_rule(noun):
         return apply_rule(noun)


if __name__ == '__main__':
   print(approximate_size(1000000000000, False))
   print(approximate_size(1000000000000))