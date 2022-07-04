import re
def minelem(arr): #finding min. element function
    max_ = arr[0]
    for ele in arr:
        if ele < max_:
           max_ = ele
    return max_
def countref(arr): #counting array items
    count1=0
    for ele in arr:
        count1 = count1+1
    return count1
i = 0
def func(): #default function
    with open("test.txt") as file:
        int_number = file.read()
        a = int_number.split()
        print(a)
        min = minelem(a)
        print("Min. element:")
        print(min)
        count = countref(a)
        print("Count:")
        print(count)
        ints = []
        for element in a:
            ints.append(int(element))
            b = minelem(ints)
        if (count < 6):
            print("Size of your array is less than 6. Program can't work in this case")
            print("Try again with size > 6")
        elif (count >= 6):
            print("Your changed array:")
            newmin = (b**2) + b
            ints.remove(b)
            ints.insert(4,newmin)
            print(ints)
            file.close()
with open("test.txt") as file: #opening file
        int_number = file.read()
        print(int_number)
mas = re.compile('[a-z,A-Z ]+$') #compile A-Z array 
if (mas.match(int_number)):
    print("There are some letters in your array")
else:
    print ("You dont have letters!")
    func()