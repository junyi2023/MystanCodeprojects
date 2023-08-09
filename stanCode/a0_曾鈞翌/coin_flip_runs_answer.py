"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r

def main():
    print("Let's flip a coin!")
    times = int(input("Number of rus:"))
    #print(times)
    result = ""
    #print(result)
    count = 0
    while True:
        if count == times:
            break
        coin = r.randint(0,1)
        if coin == 1:
            coin = "H"
        elif coin == 0:
            coin = "T"
        result = str(result+coin)
        if len(result) == 2:
            if result[-1] == result[-2]:
                count += 1
        elif len(result) > 2:
            if result[-1] == result[-2]:
                if result[-2] != result[-3]:
                    count += 1
    print(result)

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
