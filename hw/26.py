string = input()
specials = {}
newString = []

for no in range(len(string)):
    char = string[no]
    if not char.isalpha():
        specials[no] = char
    else:
        newString.append((no, char))



newString = [item[1] for item in sorted(newString, key=lambda item: (ord(item[1].lower()), item[0]))]
specials = sorted(specials.items())

for no, char in specials:
    newString.insert(no, char)

print("".join(newString))
