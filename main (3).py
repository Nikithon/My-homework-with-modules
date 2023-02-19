from roman import *

list_of_roman_numbers= ['V', 'LVII', 'MCMXCV', 'XCIX', 'LXXIX', 'LXX']
print(list_of_roman_numbers)
for i in list_of_roman_numbers:
    print(i, '->' ,roman_to_int(i))

list_of_arabic_numbers=[5, 57, 1995, 99, 70, 79]
for i in list_of_arabic_numbers:
    print(i, '->',int_to_roman(i))
