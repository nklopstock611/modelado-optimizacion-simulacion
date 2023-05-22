clc, clear all, close all

syms f_x x;

f_x = x.^5 - 8*x.^3 + 10*x + 6;
x_i_i = -2.5;
x_i = x_i_i;

figure
ezplot(f_x, [-3, 3])
hold on;

convergencia = 0.001;

a = 0.1;

xMin = -2.5;
xMax = 2.5;

d1_f_x = diff(f_x);
d2_f_x = diff(d1_f_x);

d1_f_x_i = double(subs(d1_f_x, x, x_i));

maxmins = [];
while x_i <= xMax
    cont = 1;
    while abs(d1_f_x_i) > convergencia
        cont = cont + 1;       
        d1_f_x_i = double(subs(d1_f_x, x_i)); %Primera derivada evaluada en x_i
        d2_f_x_i = double(subs(d2_f_x, x_i)); %Segunda derivada evaluada en x_i
        x_i_new = x_i - a * (d1_f_x_i/d2_f_x_i); %Expresión de Newton Raphson: x(i+1) = x(i) - a*f'(x(i))/f''(x(i))
        x_i = x_i_new;  %Actualizamos el x_i
        f_x_i = double(subs(f_x, x_i)); %Evaluamos el x_i en la f(x) para graficar posteriormente
        plot(x_i, f_x_i, 'or')    
    end
    x_i_max_prev_iter = double(subs(f_x, x_i_new));
    maxmins = [maxmins x_i_max_prev_iter];
    x_i_i = x_i_i + 0.1;
    x_i = x_i_i;
    x_i
    d1_f_x_i = double(subs(d1_f_x, x, x_i));
    d1_f_x_i
end

y_coor=double(subs(f_x, x_i_new));

plot(x_i_new,y_coor,'o')
str2 = num2str(y_coor);
if d2_f_x_i <0
    text(x_i_new -0.3,y_coor+30,['maximo ', str2]);
else
    text(x_i_new -0.3,y_coor-30,['minimo ', str2]);
end

