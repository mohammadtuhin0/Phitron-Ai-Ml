message = input()
words = message.split()

count = 0

if "ai" in words:
    count += 1
if "data" in words:
    count += 1
if "model" in words:
    count += 1
if "learn" in words:
    count += 1
if "train" in words:
    count += 1
if "neural" in words:
    count += 1

if count >= 2:
    print("AI Detected")
else:
    print("Not AI Related")