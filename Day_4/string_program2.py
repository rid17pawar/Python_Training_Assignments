print("Enter a string:")
msg = input()

vowels = "aeiou"
vowels_count = {}.fromkeys(vowels, 0)

for c in msg:
	if c in vowels:
		vowels_count[c] += 1

for k in vowels_count.keys():
	print(f"{k}:{vowels_count[k]}")