import sys
from random import randint

def gen_vet(tm):
  l = [] 
  while len(l) < tm:  
    l.append(randint(1, 1000)) 
  print(l)


size = int(sys.argv[1])

gen_vet(size)

