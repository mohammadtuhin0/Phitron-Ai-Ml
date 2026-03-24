pixels = list(map(int, input().split()))
total = 0
count = 0

for p in pixels:
    total += p
    count += 1
avg = total / count

if avg < 85:
    print("Dark Image")
elif avg <= 180:
    print("Normal Image")
else:
    print("Bright Image")