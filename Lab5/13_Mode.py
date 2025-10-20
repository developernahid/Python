data = [1, 1, 2, 3, 4, 5, 6]
frequency = {}

for i in data:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

max_freq = 0
for j in frequency:
    if frequency[j] > max_freq:
        max_freq = frequency[j]

print("Maximum frequency:", max_freq)
