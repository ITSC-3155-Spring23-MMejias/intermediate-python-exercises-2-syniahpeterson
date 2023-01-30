# Syniah Peterson
# I used https://www.calculatorsoup.com/calculators/discretemathematics/fibonacci-calculator.php for the sequence formula to calculate the fibbonacci sequence

# Imports libraries
import random
import math
import time

# Starts the timer
start = time.time()

# Gets the random integer
for i in range(1):
    num = random.randint(15, 35)

# Finds the fibbonacci number for the selected random integer
def fibonacci(integer):
    fib_list = []
    fib_list2 = []
    for i in range(0, integer + 1):
        fib_list.append(i)
    for i in fib_list:
        if i == 0:
            fib = 0
        elif i == 1:
            fib = 1
        else:
            fib = round((((1 + math.sqrt(5)) ** i)/((2 ** i) * math.sqrt(5))))
        fib_list2.append(fib)

        # Outputs the value of the fibbonacci number
    print("fib(" + str(integer) + ") = " + str(fib_list2[-1]))

    # Ends the timer
    end = time.time()

    # Calculates the totatl time
    total_time = end - start

    # Outputs the time statement
    print("fib(" + str(integer) + ") took " + str(total_time) + " seconds")
fibonacci(num)