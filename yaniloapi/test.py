


a = int(input("边长:"))
for i in range(1,a+1):
  print(" "*(a-i)+("*"*i).replace(''," ").lstrip())
for j in range(a-1,0,-1):
  print(" "*(a-j)+("*"*j).replace(''," ").lstrip())
