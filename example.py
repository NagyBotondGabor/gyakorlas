import random

print("Számok gyakorisága egy adott intervallumban")
print("mindjárt kicsengetnek,ki nem szarja le most ezt???")

def isPerfect(n):
    if n == 1 or n == 0:
        return False
    else:
            divNumbers = [1]
    for i in range(2, n, 1):
        if n % i == 0:
            divNumbers.append(i)
    
    return sum(divNumbers) == n


def randomGenerator(s, e, a):
    numbers = list()
    for i in range(a):
        numbers.append(random.randint(s, e))
    return numbers    



def makeNumber(text):
    while True: 
        n = input(text)
        try:
            n = int(n)
            return n
        except ValueError:
            print("Agyhalooott...")

#Itt indul a főprogram(main)

perfectNumbers = list()
perfectNumFreq = dict()

startMessage = "Kezdő érték: "
lastMessage  = "Végérték: "
amountMessage = "értékek száma: "

start = makeNumber(startMessage)
end = makeNumber(lastMessage)
amount =makeNumber(amountMessage)

print(start, end, amount)

randomNumbers = randomGenerator(start, end, amount)
print(randomNumbers)

for num in randomNumbers:
    if isPerfect(num):
        perfectNumbers.append(num)
for num in perfectNumbers:
    if num in perfectNumFreq.keys():
        perfectNumFreq[num] += 1
    else:
        perfectNumFreq[num] = 1
for key in perfectNumFreq.keys():
    print(f"{key}: {perfectNumFreq[key]} db")









