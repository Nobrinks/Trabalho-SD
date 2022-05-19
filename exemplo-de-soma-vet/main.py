from time import time
import sys
from vector_150000 import vector 

sys.path.append("..")
from pyDF.pydf import *
from pyDF.nodes import Feeder


nprocs = int(sys.argv[1]) # 3

# vector = [1, 2, 5, 6, 7, 9, 2, 6, 2, 6, 1, 12]
# subs
  # [1, 2, 5, 6]
  # [7, 9, 2, 6]
  # [2, 6, 1, 12]

def add_to_vet(args):
  const, vet = args[0]["const"], args[0]["vs"] 
  new_sub_vet = []
  for item in vet:
    new_sub_vet += [const + item]
  return new_sub_vet


def join_soma(args):
  new_vet = []
  for partial in args:
    new_vet += partial
  # print(new_vet)

def split(vector, num_parts):
  quotient, rest = divmod(len(vector), num_parts)
  new_vet = []
  for i in range(num_parts):
    new_vet += [vector[i * quotient + min(i, rest):(i + 1) * quotient + min(i + 1, rest)]]
  return new_vet

vector_splited = split(vector, nprocs)

graph = DFGraph()

result_node = Node(join_soma, nprocs)
graph.add(result_node)


for i in range(nprocs):
  add_to_vet_feeder = Feeder({"const": 10,"vs": vector_splited[i]})
  parcial_add = Node(add_to_vet, 1)

  graph.add(add_to_vet_feeder) 
  graph.add(parcial_add)

  add_to_vet_feeder.add_edge(parcial_add, 0)
  parcial_add.add_edge(result_node, i)


scheduler = Scheduler(graph, nprocs, mpi_enabled=False)

start_time = time()

scheduler.start()

end_time = time()

print(f"tempo total {end_time - start_time}")
