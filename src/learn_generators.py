# This is the code from https://realpython.com/introduction-to-python-generators/
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
        # print('reversed_num =', reversed_num, 'temp =', temp)

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    print('Entering infinite palindromes')
    num = 0
    while True:
        print('num =', num, is_palindrome(num))
        if is_palindrome(num):
            print('Before yield', num)
            # Example: generator
            i = (yield num)
            if i is not None:
                print('reassigned:', i, num)
                num = i
            else:
                print('not reassigned', num)
        num += 1


pal_gen = infinite_palindromes()
print('Before for loop')
for i in pal_gen:
    print('palindrome =', i)
    digits = len(str(i))
    # Example: generator advanced methods
    j = pal_gen.send(10 ** (digits))
    print('Second palindrome =', j)
    if i > 1000:
        break