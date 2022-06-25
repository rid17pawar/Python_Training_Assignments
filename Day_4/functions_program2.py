
def containsVowels(list):
    vowels = "aeiou"
    vowels_list = (char for char in msg if char in vowels)
    return vowels_list


def print_list(list):
    for value in list:
        print(value, end=",")


# driver code 
print("Enter a string:")
msg = input()
list = containsVowels(msg)
print_list(list)

print()