import time

#print((lambda l:[n for n in l if n%100==0])(range(500)))

print((lambda a,b,c:a+b+c)(time.time(),time.time(),time.time()))
