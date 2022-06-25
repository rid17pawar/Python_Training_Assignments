
def containsVowels(list):
    vowels = "aeiou"
    vowels_count_dict = {}.fromkeys(vowels, 0)

    for c in msg:
        if c in vowels:
            vowels_count_dict[c] += 1

    return vowels_count_dict


def print_dict(dict):
    for k in dict.keys():
        print(f"{k}:{dict[k]}")


# driver code 
print("Enter a string:")
msg = input()
dict = containsVowels(msg)
print_dict(dict)

print()