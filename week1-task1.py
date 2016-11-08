import random as r
numbers = [5,3,8,6,1,9,2,7]
newIndex = r.sample(range(len(numbers)), len(numbers))
shuffled = []
for j in newIndex:
    shuffled.append(numbers[j])
print(shuffled)
