# day 1

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

currentElfCalorie = 0

highestElfCalorie = 0
highestElfCalorie2 = 0
highestElfCalorie3 = 0

for s in contents:
    if s == '':
        if currentElfCalorie > highestElfCalorie:
            highestElfCalorie3 = highestElfCalorie2
            highestElfCalorie2 = highestElfCalorie
            highestElfCalorie = currentElfCalorie
        elif currentElfCalorie > highestElfCalorie2:
            highestElfCalorie3 = highestElfCalorie2
            highestElfCalorie2 = currentElfCalorie
        elif currentElfCalorie > highestElfCalorie3:
            highestElfCalorie3 = currentElfCalorie
        currentElfCalorie = 0
    else:
        currentElfCalorie += int(s)

totalTop3 = highestElfCalorie + highestElfCalorie2 + highestElfCalorie3
print(totalTop3)
