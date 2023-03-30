Sets
 i    jugadores / j1*j7 /      
 j    atributos / rol, controlBalon, disparo, rebotes, defensa /
 p    roles / ataque, centro, defensa /
 f    atrFísicos / controlBalon, disparo, rebotes /
;

Table roles (i, p)
    ataque  centro  defensa
j1  1       0       0
j2  0       1       0
j3  1       0       1
j4  0       1       1
j5  1       0       1
j6  0       1       1
j7  1       0       1
;

Table caracteristicas (i, j)
      rol   controlBalon    disparo     rebotes    defensa
j1     1         3             3           1          3                          
j2     2         2             1           3          2
j3     3         2             3           2          2
j4     4         1             3           3          1
j5     3         3             3           3          3
j6     4         3             1           2          3
j7     3         3             2           2          1
;

Table atribFisicos (i, f)
      controlBalon    disparo     rebotes
j1         3             3           1                                 
j2         2             1           3       
j3         2             3           2       
j4         1             3           3       
j5         3             3           3       
j6         3             1           2       
j7         3             2           2       
;

Parameter
 rol(p)    minimo de jugadores en cada rol    / ataque 2, centro 1, defensa 4 /
;

Variables
 z
 x(i)
;

Binary Variable
 x
;

Equations
 funcionObjetivo
 restJugadores            el equipo titular debe tener 5 jugadores.
 restrPosiciones(p)       por lo menos cuatro miembros deben ser capaces de jugar en la defensiva por lo menos dos jugadores deben jugar como atacantes y al menos uno debe jugar en el centro.
 restrAtribFisicos(f)     control de balon - disparo - rebote promedio del equipo titular debe ser por lo menos dos.
 restrJ2oJ3               si el jugador 2 esta no puede estar el 3 y al revés.
;

funcionObjetivo         ..      z =e= sum((i), x(i) * caracteristicas(i, 'defensa'));
restJugadores           ..      sum((i), x(i)) =e= 5;
restrPosiciones(p)      ..      sum((i), x(i) * roles(i, p)) =g= rol(p);
restrAtribFisicos(f)    ..      sum((i), x(i) * atribFisicos(i, f)) / 5 =g= 2;
restrJ2oJ3              ..      x('j2') + x('j3') =e= 1;

model jugadores /all/;

option mip = CPLEX;
Solve jugadores using mip maximizing z;
Display z.l;
Display x.l;


