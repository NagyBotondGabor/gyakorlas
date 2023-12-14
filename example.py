import random

print("Számok gyakorisága egy adott intervallumban")
print("mindjárt kicsengetnek,ki nem szarja le most ezt???")

def isPerfect():
    pass


def randomGenerator(s, e, a):
    numbers = list()
    for i in range(a):
        numbers.append(random.randint(s, e))
    return numbers    



def makeNumber(text):
    #isCorrect = False
    while True: #not isCorrect:
        n = input(text)
        try:
            n = int(n)
            #isCorrect = True
            return n
        except ValueError:
            print("Agyhalooott...")

startMessage = "Kezdő érték: "
lastMessage  = "Végérték: "
amountMessage = "értékek száma: "

start = makeNumber(startMessage)
end = makeNumber(lastMessage)
amount =makeNumber(amountMessage)

print(start, end, amount)

randomGenerator(start, end, amount)