
def trim(s):
    while s[:1] == ' ':
        s = s[1:]

    while s[-1:] == ' ':
        s = s[:-1]
    return s

print(trim(" ljfdsjfl "))