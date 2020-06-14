def smallest_positive(in_list):
     s=None
     for x in in_list:
          if x<=0:
               continue
          
          elif s is None:
               s=x
          elif(x<s):
               s=x
     return s

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]))
# Correct output: 39.82
