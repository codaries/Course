
abc = "sus"
print(list(range(10)))

while abc == "sus":
    print("sus")
    break

for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

base = int(input("something "))

for i in range(base):
    print((" " * (base-(i+1))) + ("*" * (i+i+1)))


