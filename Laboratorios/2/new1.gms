Sets
i procesador origen /o1*o3/ 
j procesador destino /d1*d2/
k tipo procesos /k1*k2/
;

Table costos(i,j)
    d1   d2
o1  300  500   
o2  200  300
o3  600  300
;
Table cantOri(i,k)
    k1      k2
o1  60      80
o2  80      50
o3  50      50
;

Table cantDest(j,k)
    k1      k2
d1  100     60
d2  90      120
;

Variables
x(i,j,k)
z funcion objetivo
;
Positive Variable
x
;

Equations
 funcionObjetivo
 restrOrigen(i,k)
 restrDestino(j,k)
;

funcionObjetivo       ..      z =e= sum((i, j, k), x(i, j, k) * costos(i, j));
restrOrigen(i,k)      ..      sum((j), x(i, j, k)) =e= cantOri(i,k);
restrDestino(j,k)     ..      sum((i), x(i, j, k)) =e= cantDest(j,k);

Model procesadores /all/ ;

option lp = CPLEX;

solve procesadores using lp minimizing z;

Display z.l;
Display x.l;