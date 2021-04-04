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
words = ('hex', 'play', 'beeacon',
         'joy', 'holly', 'cloth', 'catch',
         'teeth', 'cat', 'noise',
         'employee', 'software')

import re # !build_match_apply_function

def build_match_apply_function(pattern, search, replace):
   
   def matches_rule(noun):
      return re.search(pattern, noun)
   def apply_rule(noun):
      return re.sub(search, replace, noun)

   return (matches_rule, apply_rule)

#def rules(file_path):
#   with open(file_path, encoding = 'utf-8') as plur_pattern_file:
#      for line in plur_pattern_file:
#         pattern, search, replace = line.split(None,3)
#         yield build_match_apply_function(pattern, search, replace)


import os # !LazyRules

class LazyPlurRules:  

   def __init__(self, rules_filename = 'pluralization_rules.txt'):
      self.patten_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), rules_filename), encoding='utf-8')
      self.cache = []
   
   def __iter__(self):
      self.cache_index = 0
      return self

   def __next__(self):
      self.cache_index += 1
      if len(self.cache) >= self.cache_index:
         return self.cache[self.cache_index - 1]

      if self.patten_file.closed:
         raise StopIteration

      line = self.patten_file.readline()
      if not line:
         self.patten_file.close()
         raise StopIteration

      pattern, search, replace = line.split(None, 3)
      funcs = build_match_apply_function(
         pattern, search, replace)
      self.cache.append(funcs)
      return funcs

rules = LazyPlurRules()

def plural(noun):
   for match_rule, apply_rule in rules:
      if match_rule(noun):
         return apply_rule(noun)

###################################################
###################################################

class Fib:
   def __init__(self, max):
      self.max = max

   def __iter__(self):
      self.a = 0
      self.b = 1
      return self

   def __next__(self):
      fib = self.a
      if fib > self.max:
         raise StopIteration
      self.a, self.b = self.b, self.a + self.b
      return fib
   
class FibByIndex:
   def __init__(self, index):
      self.index = 0
      self.index_to_find = index

   def __iter__(self):
      self.a = 0
      self.b = 1
      return self

   def __next__(self):
      if self.index > self.index_to_find:
         raise StopIteration
      self.a, self.b = self.b, self.a + self.b
      self.index += 1
      return self.a  

###################################################
###################################################

import itertools

def alphametic_solver(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
 
    #print('words: {0}'.format(words))
    #print('len(first_letters): {0}'.format(n))
    #
    #print('unique_characters: {0}'.format(unique_characters))
    #print('first_letters: {0}'.format(first_letters))
    #print('sorted_characters: {0}'.format(sorted_characters))
    #
    #print('characters: {0}'.format(characters))
    #print('digits: {0}'.format(digits))

    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
   solution = alphametic_solver('SEND + MORE == HONEY')
   if solution:
      print(solution)