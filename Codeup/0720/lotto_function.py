import random

# n을 넣으면 그 횟수만큼
def generate_lotto(n):
    result = []
    for i in range(5):
        numbers = range(1, 46)
        pick = random.sample(numbers, 6)
        pick.sort()
        result.append(pick)
        return result

def check(buy_number, result_numbers):
    print()

print(generate_lotto(5))