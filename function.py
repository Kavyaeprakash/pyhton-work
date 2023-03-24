# x=10

# def add():
#     global x
#     x=20
#     print('from inside funcion %d'%(x))
# add()

# print('from out side %d'%(x))

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))