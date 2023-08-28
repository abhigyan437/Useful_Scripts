a = "विजय"
b = "कुमार विजय"
c = "वि के राठी"
d = "विनय राठी"
#db=[a]
#db=b.split()
db = c.split()
"""for a in list_db:
    print(str(a)[0:2])
    z = str(a).encode("ascii")
    print(z.decode('ascii'))"""

inp = input("Enter - ")
list_input = inp.split()
truth = 0
count = 0
for y in db:
    for x in list_input:
        if y==x or str(y)[0]==str(x)[0]:
            count=1
    if count==1:
        truth=1
    else:
        truth=0
if truth==1:
    print("Matched")
print("Completed")
