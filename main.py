def add(g,h):#function definition
    return g+h
def sub(g,h):
    return g-h
def mul(g,h):
    return g*h
def div(g,h):
    return g/h
n1=int(input('Enter number1:'))
n2=int(input('Enter number2:'))
answer=add(n1,n2)
print(n1,'+' ,n2,'=',answer)
answer=sub(n1,n2)
print(n1,'-' ,n2,'=',answer)
answer=mul(n1,n2)
print(n1,'*' ,n2,'=',answer)
answer=div(n1,n2)
print(n1,'/' ,n2,'=',answer)