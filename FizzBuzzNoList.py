def fizzbuzz(limit):
  for x in range(limit):
    x += 1
    if x % 3 == 0 and x % 5 == 0:
      print("FizzBuzz")
    elif x % 5 == 0:
      print("Buzz")
    elif x % 3 == 0:
      print("Fizz")
    else:
      print(x)

fizzbuzz(16)
