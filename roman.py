class OutOfRangeError(ValueError): pass
class NonIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

###
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

to_roman_table = [ None ]
from_roman_table = {}

###
def to_roman(n):
   '''convert integer to Roman numeral'''
   if not (0 < n < 5000):
      raise OutOfRangeError('number <{}> is out of range - should be in range "0 < number < 5000"'.format(n))
   if int(n) != n:
      raise NonIntegerError('non-integers cannot be converted')

   return to_roman_table[n]

###
def from_roman(s):
   '''convert Roman numeral to integer'''
   if not isinstance(s, str):
      raise InvalidRomanNumeralError('Input should be a string')
   if not s:
      raise InvalidRomanNumeralError('Invalid Roman numeral: blank string passed')   
   if s not in from_roman_table:
      raise InvalidRomanNumeralError('Invalid Roman numeral: {}'.format(s))   
   
   return from_roman_table[s]


###

def build_lookup_tables():
   def build_to_roman(n):
      result = ''
      for numeral, integer in roman_numeral_map:
         if n >= integer:
            print('n:', n, 'numeral: ', numeral, 'integer:', integer)
            result = numeral
            n -= integer
            print('n:', n, 'result: ', result)
            break
      if n > 0:
         result += to_roman_table[n]
      print('n:', n, 'result: ', result, "\n---------")
      return result
   
   for integer in range(1, 5000):
      roman_numeral = build_to_roman(integer)
      to_roman_table.append(roman_numeral)
      from_roman_table[roman_numeral] = integer   

build_lookup_tables()