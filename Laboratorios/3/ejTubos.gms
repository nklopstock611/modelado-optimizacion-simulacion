Sets
 i  tubo   / t1*t7 /
 j  losa   / l1*l20 /
;

Table tubos(i, j) matriz de tubos
    l1  l2  l3  l4  l5  l6  l7  l8  l9  l10 l11 l12 l13 l14 l15 l16 l17 l18 l19 l20
t1  1   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
t2  0   0   0   0   1   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0
t3  0   1   1   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0
t4  0   0   0   0   0   0   0   0   1   1   0   0   1   1   0   0   0   0   0   0
t5  0   0   0   0   0   0   0   0   0   1   1   0   0   1   1   0   0   0   0   0
t6  0   0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   1   0   0   0
t7  0   0   0   0   0   0   0   1   0   0   0   1   0   0   0   1   0   0   1   1
;
;

Variables
 z      función objetivo
 x(j)   escoger o no la losa
;

Binary Variable
 x
;

Equations
 funcionObjetivo
 minimoTubos(i)
;

funcionObjetivo     ..    z =e= sum((j), x(j));
minimoTubos(i)      ..    sum((j), x(j) * tubos(i, j)) =g= 1;
* para cada losa levantada se debe ver más de 1 tubo, o sino no tendría sentido.

Model tubo /all/;
Option mip=CPLEX;
Solve tubo using mip minimizing z;

Display tubos;
Display x.l;
Display z.l;