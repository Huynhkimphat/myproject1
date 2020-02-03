import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
l = 8
p =  "".join(random.sample(s,l ))
print(p)