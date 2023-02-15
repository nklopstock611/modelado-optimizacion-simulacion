Sets
 i      conjunto de empleados / e1*e4 /
 j      conjunto de trabajos / t1*t4 /
;

Table horas(i, j)
    t1  t2  t3  t4
e1  14  5   8   7
e2  2   12  6   5
e3  7   8   3   9
e4  2   4   6   10
;

Variables
 z
 e(i, j)       saber si el empleado i escogió
 t(i, j)       saber si el trabajo j se escogió
;

Binary Variables
 e
 t
;

Equations
 funcionObjetivo
 restrEmpleados(j)
 restrTrabajos(i)
;

funcionObjetivo       ..      z =e= sum((i, j), horas(i, j));
restrEmpleados(j)     ..      sum((i), e(i, j)) =e= 1;
restrTrabajos(i)      ..      sum((j), t(i, j)) =e= 1;

Model modelHoras /all/ ;

option mip=CPLEX;
Solve modelHoras using mip minimizing z;

Display z.l;
Display e.l;
*Display t.l;
