*************************************************************************
***      Problema de la Dieta                                         ***
*************************************************************************

Variables
  C     Cantidad de Carne.
  A     Cantidad de Arroz.
  L     Cantidad de Leche.
  P     Cantidad de Pan.
  z     Objective function;

Positive variable C, A, L, P;

Equations
objectiveFunction        objective function
calorias                 calorias
proteinas                proteinas
azucares                 azucares
grasas                   grasas
carbohidratos            carbohidratos
;

objectiveFunction                ..  z =e= 3000*C + 1000*A + 600*L + 700*P;

calorias                         ..  287*C + 204*A + 146*L + 245*P =g=1500;

proteinas                        ..  26*C + 4.2*A + 8*L + 6*P =g=63;

azucares                         ..  0*C + 0.01*A + 13*L + 25*P =l=25;

grasas                           ..  19.3*C + 0.5*A + 8*L + 0.8*P =l=50;

carbohidratos                    ..  0*C + 44.1*A + 11*L + 55*P =l=200;


Model model1 /all/ ;
option lp=CPLEX
Solve model1 using lp minimizing z;

Display C.l;
Display A.l;
Display L.l;
Display P.l;
Display z.l;



