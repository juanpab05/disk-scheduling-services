"""
Hecho por: Juan Pablo Pazmiño Caicedo
Codigo: 2325093-3743
"""

from heapq import *

def sstf(arm_position, lrequests, debug=False):
  """
  Shortest Seek Time First implementation

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """
  distance=0
  distances=[]
  n=len(lrequests)
  x=0
  current_pos=arm_position
  #este vector sirve para no tener que modificar el lrequests original, ya que lo necesito para mostrar
  #las solicitudes al final
  lrequests2 = [i for i in lrequests]
 

  while(x<n):
    for a_request in lrequests2:
      distances.append((abs(a_request-current_pos), a_request)) 
      distances_sorted = sorted(distances, key=lambda x: x[0])
      requests_sorted = [y[1] for y in distances_sorted]
    lrequests2.remove(requests_sorted[0])
    distance += abs(requests_sorted[0]-current_pos)
    #print(requests_sorted)
    current_pos=requests_sorted[0]
    if debug: print("> ", current_pos ,"seeked")
    #Es necesario limpiar estos vectores para que no se acumulen los valores
    distances.clear()
    requests_sorted.clear()
    x=x+1

  average=distance / n
  return {
    "sequence": [arm_position] + lrequests,
    "average": average,
    "distance": distance,
  }

#print(sstf(50, [82,170,43,140,24,16,190]))
#print(sstf(20, [3, 8, 5, 39, 35, 25, 18], 39))