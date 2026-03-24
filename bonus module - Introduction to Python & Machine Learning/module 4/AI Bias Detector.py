predictions = input().split()

count_a = 0
count_b = 0

for p in predictions:
    if p == "A":
        count_a += 1
    else:
        count_b += 1
    
total = count_a + count_b

if count_a / total > 0.7 or count_b / total > 0.7:
    print("Biased Model")
else:
    print("Fair Model")