a = 4
x = "Sally"
print(a)
print(x)
x = 5
y = "John"
print(type(x))
print(type(y))

#2myvar = "John"  diawali dengan angka
#my-var = "John"  pemisah denganan -
#my var = "John"  variabel ada space

#  multi variabel
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# variabel global
x = "awesome"

def myfunc():
    #variabel lokal haya didalam function
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 
