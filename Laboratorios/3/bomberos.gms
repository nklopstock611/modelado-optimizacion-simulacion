Sets
    i   pueblos /p1*p6 /
;
Alias (j,i);
Table tiempo (i,j)
    p1  p2  p3  p4  p5  p6
p1  0   10  20  30  30  20
p2  10  0   25  35  20  10
p3  20  25  0   15  30  20    
p4  30  35  15  0   15  25
p5  30  20  30  15  0   14
p6  20  10  20  25  14  0

;

Parameter vecinos(i,j);

Parameter conexiones(i,j)
;
loop((i,j),
    if ((tiempo(i,j) <= 15),
        conexiones(i,j) = 1);
    if((tiempo(i,j) > 15),
        conexiones(i,j) = 0);
);
        
Display conexiones;
 

Variables
z
x(i);

Binary Variable
 x
;

Equations
 funcionObjetivo
 zonas(j) 
;

funcionObjetivo     ..      z =e= sum(i, x(i));
zonas(j)            ..      sum((i), conexiones(i, j) * x(i)) =g= 1;

Model bomberos /all/;
Option mip=CPLEX;
Solve bomberos using mip minimizing z;

Display x.l;
Display z.l;