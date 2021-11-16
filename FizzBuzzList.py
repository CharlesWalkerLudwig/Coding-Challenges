ans = []
def fizzbuzz(limit):
  for x in range(limit):
    x += 1
    if (x % 3 == 0) and (x % 5 == 0):
      ans.append("FizzBuzz")
    elif x % 5 == 0:
      ans.append("Buzz")
    elif x % 3 == 0:
      ans.append("Fizz")
    else:
      ans.append(x)

fizzbuzz(16)
print(ans)



