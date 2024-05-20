class StopFunction(Exception):
    pass

def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n / 10))

def getLastDigits(n, nc):
    return int(str(n)[-nc:])

def getAllButLastDigits(n, nc):
    return int(str(n)[:-nc]) if nc < len(str(n)) else 0

def getEvenDigitsSum(n):
    n_str = str(n)
    evenDigitsSum = sum(int(n_str[i]) for i in range(len(n_str)) if i % 2 == 0)

    return evenDigitsSum

def getOddDigitsSum(n):
    n_str = str(n)
    oddDigitsSum = sum(int(n_str[i]) for i in range(len(n_str)) if i % 2 != 0)

    return oddDigitsSum

def isDivisibleBy1(n):
    return True

def isDivisibleBy2(n):
    numbers = [0, 2, 4, 6, 8]
    last_number = getLastDigits(n, 1)

    return last_number in numbers

def isDivisibleBy3(n):
    return sumDigits(n) % 3 == 0

def isDivisibleBy4(n):
    lastTwoNumbers = getLastDigits(n, 2)

    return lastTwoNumbers % 4 == 0

def isDivisibleBy5(n):
    numbers = [0, 5]
    last_number = getLastDigits(n, 1)

    return last_number in numbers

def isDivisibleBy7(n):
    doubled_last_number = getLastDigits(n, 1) * 2
    substr_result = n - doubled_last_number

    return substr_result % 7 == 0

def isDivisibleBy8(n):
    last_three_numbers = getLastDigits(n, 3)

    return last_three_numbers % 8 == 0

def isDivisibleBy9(n):
    return sumDigits(n) % 9 == 0

def isDivisibleBy10(n):
    last_number = getLastDigits(n, 1)

    return last_number == 0

def isDivisibleBy11(n):
    evenDigitsSum = getEvenDigitsSum(n)
    oddDigitsSum = getOddDigitsSum(n)

    absoluteDiff = abs(evenDigitsSum - oddDigitsSum)

    return absoluteDiff % 11 == 0

def isDivisibleBy13(n):
    lastDigit = getLastDigits(n, 1)
    multipliedLastDigit = lastDigit * 9
    numberWithoutLastDigit = getAllButLastDigits(n, 1)

    return abs(multipliedLastDigit - numberWithoutLastDigit) % 13 == 0

def isDivisibleBy16(n):
    lastFourDigits = getLastDigits(n, 4)

    return lastFourDigits & 16 == 0

def isDivisibleBy17(n):
    lastDigit = getLastDigits(n, 1)
    multipliedLastDigit = lastDigit * 5
    numberWithoutLastDigit = getAllButLastDigits(n, 1)

    return abs(multipliedLastDigit - numberWithoutLastDigit) % 17 == 0

def isDivisibleBy19(n):
    lastDigit = getLastDigits(n, 1)
    multipliedLastDigit = lastDigit * 2
    numberWithoutLastDigit = getAllButLastDigits(n, 1)

    return abs(multipliedLastDigit - numberWithoutLastDigit) % 19 == 0

def isDivisibleBy20(n):
    lastDigits = getLastDigits(n, 2)

    return lastDigits == 0 or lastDigits % 20 == 0

class Runner:
    def __init__(self):
        self.n = 0
        self.divisibility = { 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False }

    def fixDivisibility(self):
        self.divisibility[6] = self.divisibility[2] & self.divisibility[3]
        self.divisibility[12] = self.divisibility[3] & self.divisibility[4]
        self.divisibility[14] = self.divisibility[2] & self.divisibility[7]
        self.divisibility[15] = self.divisibility[3] & self.divisibility[5]
        self.divisibility[18] = self.divisibility[2] & self.divisibility[9]

        print(str(self.n) + ": " + str(sum(value for value in self.divisibility.values() if value)))

    def getDivisibility(self, n):
        self.divisibility = { 
            1: isDivisibleBy1(n), 
            2: isDivisibleBy2(n),
            3: isDivisibleBy3(n),
            4: isDivisibleBy4(n),
            5: isDivisibleBy5(n),
            6: False,
            7: isDivisibleBy7(n),
            8: isDivisibleBy8(n),
            9: isDivisibleBy9(n),
            10: isDivisibleBy10(n),
            11: isDivisibleBy11(n),
            12: False,
            13: isDivisibleBy13(n),
            14: False,
            15: False,
            16: isDivisibleBy16(n),
            17: isDivisibleBy17(n),
            18: False,
            19: isDivisibleBy19(n),
            20: isDivisibleBy20(n)
        }

        self.fixDivisibility()

    def returnDivisibility(self):
        print(self.divisibility)

    def run(self):
        while(True):
            self.n = self.n + 10

            self.getDivisibility(self.n)

            if all(self.divisibility.values()): 
                print(str(self.n) + " TAK")
                break
#            else:
#                print(str(self.n) + " NIE")


def main():
    runner = Runner()
    runner.run()

main()
