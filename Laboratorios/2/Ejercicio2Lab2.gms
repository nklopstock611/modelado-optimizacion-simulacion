Sets
i tecnicas /t1*t4/
j cientifico /c1*c6/
;

Table des(i,j)
    c1  c2  c3  c4  c5  c6
t1  85  88  87  82  91  86
t2  78  77  77  76  79  78
t3  82  81  82  80  86  81
t4  84  84  88  83  84  85
;

Variables
z
x(i,j)
;

Binary Variable
x
;

Equations
funcionObj
restCient(j)
restTec(i)
;

funcionObj     ..  z=e=sum((i,j), x(i,j)*des(i,j));
restCient(j)   ..  sum((i), x(i,j)) =l= 1;
restTec(i)     ..  sum((j), x(i,j)) =e= 1;

model cientificos /all/;

option mip = CPLEX;
Solve cientificos using mip maximizing z;
Display z.l;
Display x.l;