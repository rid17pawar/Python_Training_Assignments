print("Enter a string:")
msg = input()

vowels = "aeiou"
vowels_list = (char for char in msg if char in vowels)

for c in vowels_list:
	print(c, end=",")

print()