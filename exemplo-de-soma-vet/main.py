import sys

sys.path.append("..")
from pyDF.pydf import *


nprocs = int(sys.argv[1]) # 3

vetor = [1, 2, 5, 6, 7, 9, 2, 6, 2, 6, 1, 12]
# subs
  # [1, 2, 5, 6]
  # [7, 9, 2, 6]
  # [2, 6, 1, 12]

def soma_vet(const, vet):
  new_sub_vet = []
  for item in vet:
    new_sub_vet += [const + item]
  return new_sub_vet


def join_soma(args):
  new_vet = []
  for partial in args:
    new_vet += [partial]
  print(new_vet)

def split(vector, num_parts):
  quotient, rest = divmod(len(vector), num_parts)
  new_vet = []
  for i in range(num_parts):
    new_vet += [vector[i * quotient + min(i, rest):(i + 1) * quotient + min(i + 1, rest)]]
  return new_vet


print(soma_vet(5, vetor))
print(split(vetor, 5))
