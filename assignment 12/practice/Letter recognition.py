#  Recognition of uppercase and lowercase letters
def recodnition(strr):
    upper = 0
    lower = 0
    num = 0
    other = 0
    for s in strr:
        if 65 <= ord(s) <= 90:
            upper += 1
        elif 97 <= ord(s) <= 122:
            lower += 1
        elif 48 <= ord(s) <= 57:
            num += 1
        else:
            other += 1
    return upper, lower, num, other
string = input("enter your string:\n")
upper, lower, number, other = recodnition(string)
print("number of upper letters:", upper)
print("number of lower letters: ", lower)
print("number of numbers: ", number)
print("number of other characters: ", other)