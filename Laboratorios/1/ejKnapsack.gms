Sets
 i       objetos         / obj1, obj2, obj3, obj4, obj5 /
 j       caracteristicas / valor, peso /
;

Table caracts(i, j)
         valor   peso
obj1     12      9
obj2     5       2
obj3     9       2
obj4     6       1
obj5     4       3
;

Variables
 z       funcion objetivo
 x(i)    saber si el objeto i se escogio
;

Binary Variable
 x
;

Equations
funcionObjetivo
resPeso(j)
;

funcionObjetivo          ..              z =e= sum((i), x(i) * caracts(i, 'valor'));
resPeso(j)               ..              sum((i), x(i) * caracts(i, 'peso')) =l= 10;

Model knapsack /all/ ;

option mip=CPLEX;
Solve knapsack using mip maximizing z;

Display x.l;
Display z.l;
