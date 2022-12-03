# day 2 https://adventofcode.com/2022/day/2

# A - rock     X - rock
# B - Paper    Y - paper
# C - scissor  Z - scissor

def result_score(opponent, mine):
    if opponent == mine:
        return 3
    elif opponent == 'R':
        if mine == 'P':
            return 6
        elif mine == 'S':
            return 0
    elif opponent == 'P':
        if mine == 'S':
            return 6
        elif mine == 'R':
            return 0
    elif opponent == 'S':
        if mine == 'R':
            return 6
        elif mine == 'P':
            return 0
    return 0


def selection_score(mine):
    if mine == 'R':
        return 1
    elif mine == 'P':
        return 2
    elif mine == 'S':
        return 3
    return 0


print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

opponentSelection = []
mySelection = []

for s in contents:
    if s[0] == 'A':
        opponentSelection.append('R')
    elif s[0] == 'B':
        opponentSelection.append('P')
    elif s[0] == 'C':
        opponentSelection.append('S')

    if s[2] == 'X':
        mySelection.append('R')
    elif s[2] == 'Y':
        mySelection.append('P')
    elif s[2] == 'Z':
        mySelection.append('S')

print(opponentSelection)
print(mySelection)

i = 0
totalScore = 0
for opponent in opponentSelection:
    totalScore += result_score(opponent, mySelection[i])
    totalScore += selection_score(mySelection[i])
    i += 1

print(totalScore)