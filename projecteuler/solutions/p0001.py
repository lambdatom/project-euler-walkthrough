def solve(): 
  sum = 0 
  
  for i in range(1000):
    mltp = 3*i 
    if ( mltp < 1000 ):
      sum += mltp

  for i in range(1000):
    mltp = 5*i
    if ( mltp < 1000 and mltp % 3 != 0 ):
      sum += mltp

  print(sum)


if __name__ == "__main__":
  solve()
