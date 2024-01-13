##Even_Odd

# num = int(input('Enter the Number: '))
# if num % 2 == 0:
#     print("Entered number is Even")
# else:
#     print('Entered number is odd')

#### find prime number

num = int(input('enter number :'))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('not prime ')
            break
    else:
        print('Number is PRIME')
else:
    print('Number is not Prime!')