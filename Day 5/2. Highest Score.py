import random

scores = []

for i in range(10):
    scores.append(random.randint(0, 100))

print(scores)

max_score = 0

for score in scores:
    if score > max_score:
        max_score = score

print(f"Highest score is {max_score}")
print(f"Highest score is {max(scores)}")