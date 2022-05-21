from time import time
import sys
from vector_5000000 import vector 

sys.path.append("..")
from pyDF.pydf import *
from pyDF.nodes import Feeder

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

def creat_graph(num_works, vector_splited):
  graph = DFGraph()

  result_node = Node(join_soma, num_works)
  graph.add(result_node)

  for i in range(num_works):
    add_to_vet_feeder = Feeder({"const": 10,"vs": vector_splited[i]})
    parcial_add = Node(add_to_vet, 1)

    graph.add(add_to_vet_feeder) 
    graph.add(parcial_add)

    add_to_vet_feeder.add_edge(parcial_add, 0)
    parcial_add.add_edge(result_node, i)

  scheduler = Scheduler(graph, num_works, mpi_enabled=False)
  start_time = time()
  scheduler.start()
  end_time = time()

  print(f"tempo total {end_time - start_time}")

if (__name__ == "__main__"):
  nprocs = int(sys.argv[1])
  vector_splited = split(vector, nprocs)
  creat_graph(nprocs, vector_splited)
else:
  for workes in range(1, 7):
    vector_splited = split(vector, workes)
    print(f"numero de workers {workes}")
    creat_graph(workes, vector_splited)