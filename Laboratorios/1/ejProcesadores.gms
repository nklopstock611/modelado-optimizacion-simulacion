Sets
 i      procesadores origen     / o1*o3 /
 j      procesadores destion    / d1*d4 /
;

Parameters
 cantOrigen(i)     procesos a suministrar por los origenes
                   / o1 300, o2 500, o3 200 /
 cantDestino(j)    procesos demandados por los destinos
                   / d1 200, d2 300, d3 100, d4 400 /
;

Table costos(i, j)
    d1  d2  d3  d4
o1  8   6   10  9
o2  9   12  13  7
o3  14  9   16  5
;

Variables
 z          funcion objetivo
 x(i, j)    variable de decisión
;

Positive Variable
 x
;

Equations
 funcionObjetivo
 restrOrigen(i)
 restrDestino(j)
;

funcionObjetivo     ..      z =e= sum((i, j), x(i, j) * costos(i, j));
restrOrigen(i)      ..      sum((j), x(i, j)) =e= cantOrigen(i);
restrDestino(j)     ..      sum((i), x(i, j)) =e= cantDestino(j);

Model procesadores /all/ ;

option mip=CPLEX;
Solve procesadores using mip minimizing z;

Display z.l;
Display x.l;


