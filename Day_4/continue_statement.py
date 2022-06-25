nums = [1,5,93,50,2]

even_nums = (num for num in nums if num%2==0)

for n in even_nums:
	print(n, end=",")
	continue

print()