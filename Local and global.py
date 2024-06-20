
# Local ANd Global Variables

x = 24

print ("first variable cc" ,x)
def hello():
    x = 25
    return x
print(hello())


y= 24
print ("first variable x",y)

def hello():
    global y
    y= 25
    return y
print(hello())
print (y)