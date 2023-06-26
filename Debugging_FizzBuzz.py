# First issue with the code is that the if statement printing FizzBuzz was printing FizzBuzz on numbers divisible by both 3 and 5. 
# This was caused because the first if statement had an or instead of an and.

# Second issue is that the program should loop through and print 1-100, however if the number is divisible by 3 it should print 'Fizz'. 
#   If number is divisible by 5 program should print 'Buzz' instead of number. If number is divisible by 3 and 5 program should print 
#   FizzBuzz. With that being said, the entire section of code should be a single if statement rather than 3 seperate if statements. 
#   This was corrected by changing the second and third if statements to elif.

#for number in range(1, 101):
#  if number % 3 == 0 or number % 5 == 0:
#    print("FizzBuzz")
#  if number % 3 == 0:
#    print("Fizz")
#  if number % 5 == 0:
#    print("Buzz")
#  else:
#    print([number])    Problem: outputing numbers in brackets. Solution: Remove brackets from around numbers.


for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)