RED = "\033[48;5;196m"
GREEN = "\033[48;5;34m" 
RESET = "\033[0m"


with open('sequence.txt') as f:
    numbers = []
    for line in f:
        line = line.strip()
        if line:
            numbers.append(float(line))

more_minus5 = 0  
less_minus5 = 0      

for num in numbers:
    if 0 >= num > -5: 
        more_minus5 += 1
    elif num < -5:
        less_minus5 += 1

all = more_minus5 + less_minus5


percent_more = more_minus5 / all * 100
percent_less = less_minus5 / all * 100


print(f"{percent_more}% | {(RED + " " + RESET)  * int(percent_more // 2)}")
print(f"{percent_less}% | {(GREEN + " " + RESET) * int(percent_less // 2)}")
