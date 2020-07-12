def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Recursion - makes 6 loops of the method (E.G. 6 instances are currently running)
# Loops through until the result is 0 then it will begin returning
# until the first recursion call has been met.

# Return 1 - result = 0, k = 1 (0 + 1) = 1 | return 1
# Return 2 - result = 1, k = 2 (1 + 2) = 3 | return 3
# Return 3 - result = 3, k = 3 (3 + 3) = 6 | return 6
# return 4 - result = 6, k = 4 (6 + 4) = 10 | return 10
# return 5 - result = 10, k = 5 (10 + 5) = 15 | return 15
# return 6 - result = 15, k = 6 (15 + 6) = 21 | return 21


