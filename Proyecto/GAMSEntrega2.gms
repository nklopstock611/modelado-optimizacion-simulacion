
$Set NODES 6
$Set DESIRED 1
$Set TYPES 3
$Set SOURCE 1
$Set MUST_VISIT 3 

Sets
  i   network nodes / n1*n%NODES% /
  f   secuencia de cada enlace seleccionado / f1*f%MUST_VISIT% /
  t   secuencia de tipos de nodos / t1*t%TYPES% /

alias(j,i);
alias(k,i);

alias(d,f);

*$ontext
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
n6   0    0    1
;
*$offtext

*Dynamic set for reducing the compilation time.
*$ontext
Set links(i,j);

Loop( (i,j),
      if( c(i,j)<999,
        links[i,j]=Yes;
      )
);
*$offtext


Variables
  x(i,j,f)      Indicates if the link i-j is selected or not.
  y(i,t)        indica si el tipo de nodo 
  z           Objective function  ;

Binary Variable x;

Equations
objectiveFunction        objective function

*$ontext
restr1(i,j,f)
restr2(f)
restr3(i,j)
restr4(i)
restr5(j)
restr7(i,f)
restr8(i,j,f,d)
restr9(f,t)
restr10(f,t)
;

objectiveFunction       ..  z =e= sum((i,j,f), c(i,j) * x(i,j,f));

*$ontext

*No repetir enlace
restr1(i,j,f)                 ..  x(i,j,f) + x(j,i,f) =l= 1;

*Por cada f, solo un (i,j) debe ser escogido.
restr2(f)   ..   sum((i,j), x(i,j,f))=e=1;

*Por cada enlace (i,j) a lo sumo puede estar activado para un e cualquiera.
restr3(i,j)   ..   sum(f, x(i,j,f))=l=1;

*para todo nodo i, debe salir un enlace.
restr4(i)   ..   sum((j,f), x(i,j,f))=e=1;

*Para todo nodo j, debe llegar un enlace.
restr5(j)   ..   sum((i,f), x(i,j,f))=e=1;

restr7(i,f)$(ord(i)=%SOURCE% and ord(f)=1)   ..   sum(j, x(i,j,f))=e=1;

restr8(i,j,f,d)$(ord(d)=ord(f)+1 and ord(f)<%MUST_VISIT%)  ..   sum((k)$(links(j,k)), x(j,k,d))=g=x(i,j,f);

***Resttricciones de cantidades de murales deseados. Por cada enlace se revisan las selecciones de nodos

restr9(f,t)$(ord(t)=2) .. sum((i,j), x(i,j,f)*type(i,t))=e= %DESIRED%;

***Por cada enlace se recisa para ver si cumple con las restricciones de refrescos

restr10(f,t)$(ord(t)=3) .. sum((i,j), x(i,j,f)*type(i,t))=e=1;

Model model1 /all/ ;
option mip=SCIP
Solve model1 using mip minimizing z;

Display x.l;
Display z.l;
