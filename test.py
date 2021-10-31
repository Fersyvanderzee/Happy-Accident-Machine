import random

duration_input = 'random'


for i in range(10):
    if duration_input == 'random':
        duration = random.randint(1, 10)
    print(duration)
