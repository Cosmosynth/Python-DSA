addition = lambda a,b : a + b # format

type(addition)
print(addition(3 , 7))

def  even(n):
    if n%2==0:
        return True

print(even(12))

even1 = lambda nm : nm%2==0

print(even1(122))

# map()- applies func to all items in a collection 
number = [1, 2, 3, 4, 5, 6]

# for i in number:
#     print(i**2)

map(lambda x:x**2, number)
