N = int(input())

yes_count = 0
no_count = 0

for _ in range(N):
    vote = input()
    
    if vote == "YES":
        yes_count += 1
    else:
        no_count += 1
        
if yes_count >= no_count:
    print("ACCEPT")
else:
    print("REJECT")