
$Set NODES 6
$Set DESIRED 1
$Set TYPES 3
$Set SOURCE 1
$Set MUST_VISIT 3 

Sets
  i   network nodes / n1*n%NODES% /
  f   secuencia de cada enlace seleccionado / f1*f%MUST_VISIT% /
  t   secuencia de tipos de nodos / t1*t%TYPES% /

  alias(j,i)
  alias(f,g)
  alias(k,i)
  alias(d,f)
;

Table c(i,j) link cost
                 n1       n2      n3      n4      n5     n6
n1               999       2       5       5       2      9
n2                 2     999       3       5       1      9
n3                 5       3     999       2       3     11
n4                 5       5       2     999       4     12
n5                 2       2       3       4     999      4
n6                 6       2       3       6       4    999
;

Table type(i,t)

    t1   t2   t3
n1   1    0    0
n2   0    1    0
n3   0    1    0
n4   0    1    0
n5   0    0    1
n6   0    0    0
;

* t1 -> hotel
* t2 -> murales
* t3 -> parques
* t4 -> lugares random

Set links(i,j);

Loop( (i,j),
      if( c(i,j)<999,
        links[i,j]=Yes;
      )
);

Variables
  x(i,j,f)      Indicates if the link i-j is selected or not.
  w(i)          Lleva cuenta de los nodos visitados.
  z             Objective function.
;

Binary Variable x;
Binary Variable w;

Equations
objectiveFunction        objective function

restr1(i,j,f)
restr2(i,j,f,g)
restr3(f)
restr4(i,j)
restr5(i,f)
restr6(i,j,f,d)
restr7(i,j,f)
restr8(i,j,f)
restr9
restr10
restr11
restr12(j,f)
restr13(i)
;

objectiveFunction                                           ..      z =e= sum((i,j,f), c(i,j) * x(i,j,f));

** Restricciones TSP **

*No repetir enlace
restr1(i,j,f)                                               ..      x(i,j,f) + x(j,i,f) =l= 1;

*No repetir enlace "de regreso" ej. enlace 2-5, 5-2
restr2(i,j,f,g)$(ord(f)<>ord(g))                            ..      x(i,j,f) + x(j,i,g) =l= 1;           

*Por cada e, solo un (i,j) debe ser escogido.
restr3(f)                                                   ..      sum((i,j), x(i,j,f)) =e= 1;

*Por cada enlace (i,j) a lo sumo puede estar activado para un e cualquiera.
restr4(i,j)                                                 ..      sum(f, x(i,j,f)) =l= 1;

*Para el nodo inicial i=1, debe salir un enlace y ademas activamos el y(j,e) correspondiente.
restr5(i,f)$(ord(i)=%SOURCE% and ord(f)=1)                  ..      sum(j, x(i,j,f)) =e= 1;

restr6(i,j,f,d)$(ord(d)=ord(f)+1 and ord(f)<%MUST_VISIT%)   ..      sum((k)$(links(j,k)), x(j,k,d))=g=x(i,j,f);

** Restricciones de cantidades de murales deseados. Por cada enlace se revisan las selecciones de nodos **

restr7(i,j,f)                                               ..      w(i) =g= x(i,j,f);

restr8(i,j,f)                                               ..      w(j) =g= x(i,j,f);

restr9                                                      ..      sum(i, w(i)*type(i,"t2")) =e= %DESIRED%;

restr10                                                     ..      sum(i, w(i)) =e= %MUST_VISIT%;  

** Por cada enlace se recisa para ver si cumple con las restricciones de refrescos **

restr11                                                     ..      sum(i, w(i)*type(i,"t3")) =e= 1;

* El nodo SOURCE no puede ser un intermedio del TSP y forzarlo para que quede cierre el loop.
restr12(j,f)$(ord(j)=%SOURCE% and ord(f)=%MUST_VISIT%)      ..      sum(i, x(i,j,f)) =e= 1;

restr13(i)                                                  ..      sum((j,f), x(i,j,f)) =l= 1;
* =l= porque no tiene que pasar por todos los nodos.

Model model1 /all/ ;
option mip=SCIP
Solve model1 using mip minimizing z;

Display x.l;
Display w.l;
Display z.l;
