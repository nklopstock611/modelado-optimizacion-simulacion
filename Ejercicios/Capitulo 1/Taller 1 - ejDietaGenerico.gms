*************************************************************************
***      Taller 1: generalizar el problema de la dieta                ***
***                                                                   ***
***      Autores: Nicolas Klopstock, Juan Camilo Falla                ***
***      Codigos: 202021352, 201922219                                ***
*************************************************************************

Sets
 i       alimento / carne, arroz, leche, pan /
 j       caracteristicas / calorias, proteinas, azucares, grasas, carbohidratos, precio /
;

Table productos(i, j)
         calorias  proteinas  azucares  grasas  carbohidratos  precio
carne    287       26         0         19.3    0              3000
arroz    204       4.2        0.01      0.5     44.1           1000
leche    146       8          13        8       11             600
pan      245       6          25        0.8     55             700
;

Variables
 z       funcion objetivo
 C(i)    carne
 A(i)    arroz
 L(i)    leche
 P(i)    pan
;

Positive Variables
 C
 A
 L
 P
;

Equations
 funcionObjetivo
 restrCal(j)
 restrProt(j)
 restrAz(j)
 restrGras(j)
 restrCarbo(j)
;

funcionObjetivo             ..      z =e= sum((i), productos(i, 'precio') * C(i) + productos(i, 'precio') * A(i) + productos(i, 'precio') * L(i) + productos(i, 'precio') * P(i));
restrCal(j)$(ord(j)=1)      ..      sum((i), productos(i, j) * C(i) + productos(i, j) * A(i) + productos(i, j) * L(i) + productos(i, j) * P(i)) =g= 1500;
restrProt(j)$(ord(j)=2)     ..      sum((i), productos(i, j) * C(i) + productos(i, j) * A(i) + productos(i, j) * L(i) + productos(i, j) * P(i)) =g= 63;
restrAz(j)$(ord(j)=3)       ..      sum((i), productos(i, j) * C(i) + productos(i, j) * A(i) + productos(i, j) * L(i) + productos(i, j) * P(i)) =l= 25;
restrGras(j)$(ord(j)=4)     ..      sum((i), productos(i, j) * C(i) + productos(i, j) * A(i) + productos(i, j) * L(i) + productos(i, j) * P(i)) =l= 50;
restrCarbo(j)$(ord(j)=5)    ..      sum((i), productos(i, j) * C(i) + productos(i, j) * A(i) + productos(i, j) * L(i) + productos(i, j) * P(i)) =l= 200;

Model diet /all/ ;

option mip=CPLEX;
Solve diet using mip minimizing z;

Display C.l;
Display A.l;
Display L.l;
Display P.l;
Display z.l;