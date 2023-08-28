a = "cat"
num = len(a)
z = 0
list_a = []
while (z<num):
    list_a.append(a[z])
    z = z+1
list_b = list_a
list_actual = []
word = ""
print("Hell")
for x in list_a:

    word = ""
    word = word + str(x)
    list_b.pop(0)
    list_c = list_b
    print(word)
    for y in list_b:
        word = word + str(y)
        list_b.pop(0)
        print(word)
        for z in list_b:
            word = word + str(z)
            list_actual.append(word)
            print(word)
        list_b = list_c
    list_b = list_a
print(list_actual)
