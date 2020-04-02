# Joe Degere
# 4/2/2020
# Palindrome example


faze = input('Enter a phrase and it will be checked to see if it\'s palindrome.')


def check(string):
    string = string.strip()
    string = string.lower()

    if len(string) <= 1:
        return 'approved'

    elif string[0] != string[-1]:
        return 'declined! Better luck next time \n' \
               'Try not to cry...'

    else:
        return check(string[1: -1])


if True:
    print(check(faze))

print('The length of your phrase is:\n')
print(len(faze))

# Just cause
print('Your phrase in all uppercase:\n')
print(faze.upper())
