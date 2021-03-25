# this is a coment
# this is hello world
print("hello world is (kind of) tiny")
# this is string formatting
print("this string is {}".format("AWESOME!!!"))
# variables dictionarys and lists
vara=1
varb=[1,2,2]# 1 2 and 3 list(indexed at 0)
print(varb[1])# prints 2
varab={"key":"value"}# dictionary
# math
print(1+2-3/10*100)
# for loops
for x in [1,2,3]:
	print(x)
# if elif else
a=2
if a == 0:
	# IF a is 0
	print("cond1")
elif a == 1:
	# ELSE IF a is 1
	print("cond2")
else:
	# ELSE
	print("sadly a is not 0 or 1")
# functions
def func(arga):
	print(arga)
func("code")
# oop
class code:
	# on initilaise
	def __init__(self,a):
		print(a)
		self.v=0
aaa=code(2)
print(aaa.v)
# exceptions and try..except..finally
try:
	raise Exception("if you see this there is something rong wit u")
except Exception:
	print("OHE NOES A EXCEPTION!!!")
finally:
	print("cleanup\n\n") # newlines with \n
# multiline strings
print("""
code is cool
right
""")
# user input
print(input("do you like waffles:"))
# executing a nother script
exec("print(1+2)")
print(eval("1+2"))
# run this by python3 howtopython.py in a terminal in your project
