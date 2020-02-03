from random import shuffle
import random
s = "abcdefghijklmnopqrstuvwxyz"
l = 2
p=['0','0','0','0']
p[0] =  "".join(random.sample(s,l ))
s="01234567890"
p[1] =  "".join(random.sample(s,l ))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p[2] =  "".join(random.sample(s,l ))
s="#!@#$%^&*()?"
p[3]= "".join(random.sample(s,l ))
shuffle(p)
for i in p:
    print(i,end="")
