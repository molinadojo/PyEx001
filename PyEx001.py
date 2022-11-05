
print("________________________________________________________")
print("Bienvenido a este su Puesto de Comida Rapida :)")
print("________________________________________________________")
precio_empanada = 1200
precio_pizza = 800
costo_empanada = 500
costo_pizza= 40

pedido_empanada = int(input("Cuantas docenas de empanadas Usted desea Pedir:"))

DineroEmpanada = precio_empanada * pedido_empanada
print("Dinero recaudado de empanadas $", DineroEmpanada)
costo_DineroEmpanada = costo_empanada * pedido_empanada
print("Dinero costo de empanada $", costo_DineroEmpanada)

print("________________________________________________________")
pedido_pizza = int(input ("Cuantas Pizzas Usted desea Pedir:"))

DineroPizza = precio_pizza * pedido_pizza
print("Dinero recaudado de pizza $", DineroPizza)
costo_DineroPizza = costo_pizza * pedido_pizza
print("Dinero costo de pizza $", costo_DineroPizza)
print("________________________________________________________")
dineroTotal_Bruto = DineroEmpanada + DineroPizza
print("El dinero en total en bruto es $", dineroTotal_Bruto)
print("________________________________________________________")
costoTotales = costo_DineroEmpanada + costo_DineroPizza 
print("Los Costos totales en bruto es $", costoTotales)
gananciasObtenidas =  dineroTotal_Bruto - costoTotales
print("________________________________________________________")
print("Ganancia en limpio, realizado el Balance: $", gananciasObtenidas)
print("________________________________________________________")
print("MUCHAS GRACIAS POR CONFIAR EN NOSOTROS :)")
print("// END //")