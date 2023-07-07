def square_num(n):
  return n * n
nums = list(map(int,input("enter the number:").split(",")))
print("Original List: ",nums)
result = map(square_num, nums)
print("Square of the number is:",list(result))
