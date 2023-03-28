Sets
i 'canciones' /i1*i8/
generos /BluesRock, RockAndRoll /
;
Parameter tablaCanciones(i, generos);
tablaCanciones('i1', 'BluesRock') = 1;
tablaCanciones('i2', 'RockAndRoll') = 1;
tablaCanciones('i3', 'BluesRock') = 1;
tablaCanciones('i4', 'RockAndRoll') = 1;
tablaCanciones('i5', 'BluesRock') = 1;
tablaCanciones('i6', 'RockAndRoll') = 1;
tablaCanciones('i8', 'BluesRock') = 1;
tablaCanciones('i8', 'RockAndRoll') = 1;

Parameter
tiempo(i) /i1 4, i2 5, i3 3, i4 2, i5 4, i6 3, i7 5, i8 4/;

Variables
a(i)
b(i)
z
;
Binary Variables
a
b
;

Equations
funcionObj
minA
maxA
minB
maxB
BluesA
BluesB
rockA
condicion1
condicion2
orden
;

funcionObj      ..  z=e= sum(i, a(i) + b(i));
minA            ..  sum(i, a(i)* tiempo(i))=g=14;
maxA            ..  sum(i, a(i)* tiempo(i))=l=16;
minB            ..  sum(i, a(i)* tiempo(i))=g=14;
maxB            ..  sum(i, a(i)* tiempo(i))=l=16;
BluesA          ..  sum(i, a(i)* tablaCanciones(i, 'BluesRock')) =e=2;
BluesB          ..  sum(i, b(i)* tablaCanciones(i, 'BluesRock')) =e=2;
rockA           ..  sum(i, a(i)* tablaCanciones(i, 'RockAndRoll')) =g=3;
condicion1      ..  1-a('i1') =g= a('i5');
condicion2      ..  a('i2') + a('i4') =l= b('i1')+1;
orden(i).. 1-a(i) =g= b(i);

Model canciones /all/;
option mip=cplex
Solve canciones using mip maximizing z;
Display a.l;
Display b.l;