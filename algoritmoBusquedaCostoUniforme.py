!pip install treelib

from treelib import Tree

g=Tree()

grafo={'U':{'V':2,'X':1,'W':5},
       'X':{'U':1,'V':2,'W':3,'Y':1},
       'V':{'U':2,'X':2,'W':3},
       'Y':{'X':1,'W':1,'Z':2},
       'W':{'V':3,'X':3,'Y':1,'Z':5},
       'Z':{'Y':2,'W':5}}

pq=[]
visitados=[]
id=1

g=Tree()

nodo=g.create_node(tag='U',data=['U',0],identifier=id)

pq.append(nodo)

while len(pq) !=0:
  pq.sort(key=lambda X:X.data[1])
  nodo_actual=pq.pop(0)
  costo_actual=nodo_actual.data[1]
  if nodo_actual.tag=='Z':
    g.show()
  visitados.append(nodo_actual.tag)
  hijos=list(grafo[nodo_actual.tag].items())
  for hijo in hijos:
    id=id+1
    nodo_hijo=g.create_node(tag=hijo[0],data=list(hijo),identifier=id,parent=nodo_actual.identifier)
    costo_hijo=hijo[1]
    costo_acumulado=costo_actual+costo_hijo
    if hijo[0]not in visitados:
      lista=[nodo.tag for nodo in pq]
      if hijo[0] in lista:
        index=lista.index(hijo[0])
        if costo_acumulado < pq[index].data[1]:
          pq[index].data[1]=costo_hijo
      else:
        pq.append(nodo_hijo)


d=g.nodes
for clave in d:
  if g.is_ancestor (d[clave].identifier, nodo_actual.identifier):
    print (d[clave].data)
print (nodo_actual.data)