"""List = ["lol", "test"]

print(List)
print(len(List))

for i in List:
    print(i)

print(List[::-1])

myFriend = []
print(myFriend)

myFriend.append("Noob")
myFriend.append("Nomwhaan")
print(myFriend)

myFriend.remove("Nomwhaan")
print(myFriend)

del myFriend[0]
print(myFriend)

myFriend.append("Noob")
myFriend.append("Nomwhaan")

print(myFriend)
myFriend.clear()
print(myFriend)


tuple = ("among us", "sus")
tuple4 = tuple * 3
tuple3 = tuple + tuple

print(tuple3)
print(tuple4)

print("noob" in tuple4)
print("Nomwhaan" in myFriend)

noob = [300, 200]
print(max(noob))
print(min(noob))
print(len(noob))

print(tuple3[2])"""

"""tupleA = ("among us", "sussy")
listA = ("sus", "imposter")

a = list(tupleA)
b = tuple(listA)

print(a)
print(b)

bofa = {"Name": "Baicha", "Age": 14}
print(bofa.keys())
print(bofa.values())
print(bofa['Name'])
bofa['Name'] = "Nomwhaan"
bofa['Weight'] = 1310010310
print(bofa.items())"""

"""systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList)
        print(menuList[number][0], menuList[number][1])


while True:
    menuName = input("Plese Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()"""

settest = {"among us", "sus", "imposter"}
print(settest)

for x in settest:
    print(x)

settest.add("crewmate")