num = int(input("Enter a number: "))

# Check Even or Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Check Prime Number
if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")