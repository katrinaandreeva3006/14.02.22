def average(*args):
  return sum(args, 0.0) / len(args)
print(average(*[1, 2, 3, 4]))
print(average(1, 2, 3))