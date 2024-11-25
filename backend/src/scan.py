"""
Hecho por: Juan Pablo Pazmiño Caicedo
Codigo: 2325093-3743
"""

from heapq import *

def scan(arm_position, lrequests, ntracks, debug=False):
  """
  Shortest Seek Time First implementation

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
      ntracks(int): number of tracks
  """
  distance=0
  distances_up=[]
  distances_down=[]
  x=0
  current_pos=arm_position
  lrequests2 = [i for i in lrequests]
 
  #Se verifica que todos las solicitudes sean menores al numero de pistas
  for a in lrequests:
    if(a>ntracks):
      return{
        "ERROR: Una solicitud supera el numero de pistas"
      }
  
  if ntracks not in lrequests:
    lrequests2.append(ntracks)

  n=len(lrequests2)
    
  for a_request in lrequests2:
    if(a_request-current_pos>=0):
      distances_up.append(a_request) 
    else:
      distances_down.append(a_request)

  requests_sorted = sorted(distances_up)

  while(x<n):
    if(len(requests_sorted)==0):
      requests_sorted = sorted(distances_down, reverse=True)

    distance += abs(requests_sorted[0]-current_pos)
    #print(requests_sorted)
    current_pos=requests_sorted[0]
    if debug: print("> ", current_pos ,"seeked")
    requests_sorted.remove(requests_sorted[0])
    x=x+1

  average=distance / n
  return {
    "sequence": [arm_position] + lrequests,
    "average": average,
    "distance": distance,
  }

#print(scan(50, [82,170,43,140,24,16,190], 199))
#print(scan(20, [3, 8, 5, 39, 35, 25, 18], 39))
