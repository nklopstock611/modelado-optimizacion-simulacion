%Juan Camilo Falla 201922219
%Nicolas Klopstock 202021352
clc
clear all
syms z x y

z = (1-x)^2 + 100*(y-x^2)^2;

figure
ezsurf(x,y,z)

%punto de inicio y parametros para ejecutar el algo
iter = 1;
xy = [0,10];

conv = 1*10^-5;
alpha = 1;
gradBoi = gradient(z);
hessiano = hessian(z);

%se inicializan parametros

soluciones = zeros(3,1);
norma = Inf;

% llenar el vecor con el punto 1

soluciones (1,1) = xy(1,1);
soluciones (2,1) = xy(1,2);
soluciones (3,1) = double(subs(z, [x,y], xy));
puntoAnterior = xy;


while abs(norma)>conv
        iter = iter+1;
        gradEval = subs(gradBoi,[x,y],puntoAnterior);
        gradActual= double(gradEval);
        hessEval = subs(hessiano,[x,y],puntoAnterior);
        hessActual = double(hessEval);
        hessInverso = inv(hessActual);
        variacionXY = alpha*(hessInverso*gradActual);
        nuevoPunto = puntoAnterior - variacionXY';
        puntoAnterior = nuevoPunto;
        soluciones (1,iter) = nuevoPunto(1,1);
        soluciones (2,iter) = nuevoPunto(1,2);
        soluciones (3,iter) = double(subs(z, [x,y], nuevoPunto));
        norma= norm(gradActual);
end

hold on;
puntos_x = soluciones(1,:);
puntos_y = soluciones(2,:);
puntos_z = soluciones(3,:);

plot3(puntos_x, puntos_y, puntos_z, 'o', 'MarkerSize', 10, 'MarkerFaceColor', 'red');
plot3(puntos_x, puntos_y, puntos_z, '-');