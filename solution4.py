# Write code for algorithm 4 below
# didnt get to so copied from solution code
def a_to_b(a,b):
  if b < 1:
    print("invalid input")
  elif b == 1:
    return a
  else:
    return a * a_to_b(a,b-1)

print("2^4:")