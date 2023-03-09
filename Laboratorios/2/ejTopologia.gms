Sets
 i      nodos / n1*n7 /
 c      coordenadas / x, y /
;

Alias (j, i)

Table conexionesRaw(i, c) matriz pre-procesada
    x   y
n1  20  6
n2  22  1
n3  9   2
n4  3   25
n5  21  10
n6  29  2
n7  14  12
;

Parameter
 conexiones(i, j) matriz de conexiones finales
;

Scalar d;

loop((i, j),
    d = sqrt( sqr(conexionesRaw(i, 'x') - conexionesRaw(j, 'x')) + sqr(conexionesRaw(i, 'y') - conexionesRaw(j, 'y')) );
    Display d;
    if(d <= 20 and d > 0,
        conexiones(i, j) = d;
    elseif(d = 0),
        conexiones(i, j) = 999;
    else
        conexiones(i, j) = 999;
    );
);

Variables
 z      función objetivo
 x(i, j)    saber si el enlace i-j se escogió o no
;

Binary Variable
 x
;

Equations
 funcionObjetivo
 restrNodoOrigen(i)
 restrNodoDestino(j)
 restrNodoInter(i)
;

funcionObjetivo                                     ..      z =e= sum((i, j), conexiones(i, j) * x(i, j));
restrNodoOrigen(i)$(ord(i) = 4)                     ..      sum((j), x(i, j)) =e= 1;
restrNodoDestino(j)$(ord(j) = 6)                    ..      sum((i), x(i, j)) =e= 1;
restrNodoInter(i)$(ord(i) <> 4 and ord(i) <> 6)     ..      sum((j), x(i, j)) - sum((j), x(j, i)) =e= 0;

Model topologia /all/;
Option mip=CPLEX;
Solve topologia using mip minimizing z;

Display conexiones;
Display x.l;
Display z.l;
