a = "Good professor"
b = "Lovely professor"
c = "beautiful teaching style and solpa good no"
d = "Could summarise teachings better"
e = "Goodie good good"
L = [a, b, c, d, e]
count = 0
for i in L:
    if "good" in i or "Good" in i:
        count+=1

print("Positive reviews: ", count)
