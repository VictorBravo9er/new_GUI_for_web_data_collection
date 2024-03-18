
print("vikram", "Rupam", "abhi", sep="~~", end="\n*\n")
print("hi")
print("\n")

a = [21, "hi"]


f = open("r.txt", "w")
for i in range(len(a)):
    print("index:", i, "name:", a[i], sep=" ", file=f)


import time


for i in range(20):
    print(f"{1+i:2}", )
    time.sleep(2)