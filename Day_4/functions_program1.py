def containsEven(list):
    for i in list:
        if i%2==0:
            print("This list contains an even number")
            break

    else:
        print("This list  doesn't contain any even number")

# driver code
nums = [1,5,93,50]
containsEven(nums)

print()
