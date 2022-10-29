import random
import time

# MD.ATIKUR RAHMAN
# https://github.com/atik59/Lottery-Random-Number-

levelStart = 1
levelEnd = 5
termStart = 1
termEnd = 3
level = random.randrange(levelStart,levelEnd)

def concat(x,y):
    return int(f"{x}{y}")


# print(level)
term = random.randrange(termStart,termEnd)
# print(term)

# def concat(x,y):
#     return int(f"{x}{y}")
# print(concat(level, term))

levelTerm = concat(level, term)


def outPut(levelTerm, RandomCode):
    time.sleep(2)
    print("Level : ", level)
    time.sleep(2)
    print("Term : ", term)
    time.sleep(2)
    print("Level/Term : ", levelTerm)

    symbol = '-'
    if RandomCode < 10:
        time.sleep(4)
        print("Congratulation ID-Number : ", f'{levelTerm}{symbol}{"00"}{RandomCode}')
        time.sleep(4)
        print("Lottery Done")
    else:
        time.sleep(4)
        print("Congratulation ID-Number : ", f'{levelTerm}{symbol}{"0"}{RandomCode}')
        time.sleep(4)
        print("Lottery Done")


if levelTerm == 11:
    RandomCode = random.randrange(1, 101)
    outPut(levelTerm, RandomCode)
elif levelTerm == 12:
    RandomCode = random.randrange(1, 35)
    outPut(levelTerm, RandomCode)
elif levelTerm == 21:
    RandomCode = random.randrange(1, 23)
    outPut(levelTerm, RandomCode)
elif levelTerm == 22:
    RandomCode = random.randrange(1, 9)
    outPut(levelTerm, RandomCode)
elif levelTerm == 31:
    RandomCode = random.randrange(1, 9)
    outPut(levelTerm, RandomCode)
elif levelTerm == 32:
    RandomCode = random.randrange(1, 53)
    outPut(levelTerm, RandomCode)
elif levelTerm == 41:
    RandomCode = random.randrange(1, 14)
    outPut(levelTerm, RandomCode)
elif levelTerm == 42:
    RandomCode = random.randrange(1, 39)
    outPut(levelTerm, RandomCode)
else:
    print("Invalid random code. Please try again.")