x=5

if (type(x) is int):
    print (True)
else:
    print (False)



y=5.0

if (type(y) is not float):
    print (False)
else:
    print (True)


a=20
b=20

if (a is b):
    print ("a and b are same")
b=30
if a is not b:
    print ("they are different")