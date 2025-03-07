# Write a program to print “Bright IT Career” ten times using for loop
for i in range(10):
    print('“Bright IT Career')
# Write a java program to print 1 to 20 numbers using the while loop.
i = 1
while i <= 20:
    print(i)
    i += 1
# Program to equal operator and not equal operators
a = 10
b = 20
c = 30
print(a == b)
print(a != b)

# Write a program to print the odd and even numbers.
print('Even Numbers:')
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("Odd Numbers")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Write a program to print largest number among three numbers.
if a > b:
    print('a is the largest number')
elif b > c:
    print('b is the largest number')
elif c > a:
    print('C is the largest number')

# Write a program to print even number between 10 and 20 using while
b = 10
while b <= 20:
    if b % 2 == 0:
        print(b)
    b += 1

# Write a program to print 1 to 10 using the do-while loop statement.

i = 1
while i <= 10:
    print(i)
    i += 1

# Write a program to find Armstrong number or not


def armstrong_number():
    num = 8208
    len_num = len(str(num))
    temp = int(num)
    sum_ = 0
    while temp > 0:
        r = temp % 10
        sum_ += r ** len_num
        temp //= 10
    if sum_ == num:
        return "It is a armstrong number"
    else:
        return "It is a not a armstrong number"


print(armstrong_number())

# Write a program to find the prime or not


def prime_or_not():
    num = 5
    for i in range(2, num):
        if num % i == 0:
            return 'Not prime'
    else:
        return 'Prime'


print(prime_or_not())


# Write a program to palindrome or not.
def str_palindrome_or_not():
    string = 'palindrome'
    if string == string[::-1]:
        return "palindrome"
    else:
        return "Not palindrome"


def num_palindrome_or_not():
    num = 141
    temp = num
    pal_num = 0
    while temp > 0:
        r = temp % 10
        pal_num = pal_num*10 + r
        temp = temp//10
    if num == pal_num:
        return f"{num} is a palindrome"
    else:
        return pal_num  # f"{num} is not a palindrome"


print(str_palindrome_or_not())
print(num_palindrome_or_not())


# Program to check whether a number is EVEN or ODD using switch
def even_or_not():
    if a % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
