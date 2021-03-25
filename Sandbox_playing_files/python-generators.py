# Python Generators
def gen():
	yield None # send out the first value
	x = yield None # get the first value out of send
	while True:
		x = yield x # get the next value out of send

g=gen()
print(next(g))
print(g.send(None))
print(g.send(1))
print(next(g))
