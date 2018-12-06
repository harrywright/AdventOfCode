import itertools

changes = [int(frequency) for frequency in open("input.txt").readlines()]

print(sum(changes))



freq = 0
seen = {0}
for num in itertools.cycle(changes):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)

