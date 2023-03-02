Sets
 i / n1*n12 /
;

Alias (j, i);

Table aristas(i, j)
    n1  n2  n3  n4  n5  n6  n7  n8  n9  n10 n11 n12
n1  1   1   1   0   1   0   0   0   0   0   0   0
n2  1   1   0   0   1   0   0   0   0   0   0   0
n3  1   0   1   1   1   1   1   1   0   0   0   0
n4  0   0   1   1   1   1   0   0   0   0   1   0
n5  1   1   1   1   1   0   0   0   0   1   1   0
n6  0   0   1   1   0   1   0   1   0   0   1   0
n7  0   0   1   0   0   0   1   1   0   0   0   1
n8  0   0   1   0   0   1   1   1   1   0   1   1
n9  0   0   0   0   0   0   0   1   1   1   1   1
n10 0   0   0   0   1   0   0   0   1   1   1   0
n11 0   0   0   1   1   1   0   1   1   1   1   0
n12 0   0   0   0   0   0   1   1   1   0   0   1
;

Variables
 z      funcion objetivo
 x(i)   revisar si se escoge o no el enlace
;


Binary Variable
 x
;

Equations
 funcionObjetivo    tiene que minimizar el total de los enlaces escogidos
 restrEnlaces(j)    revisa que cada nodo tenga mínimo un enlace a otro
;

funcionObjetivo     ..      z =e= sum((i), x(i));
restrEnlaces(j)     ..      sum((i), aristas(i, j) * x(i)) =g= 1;

Model antenas /all/;

Option mip=CPLEX;
Solve antenas using mip minimizing z;

Display z.l;
Display x.l;


