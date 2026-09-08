Un archivo `detecciones.md` con una tabla de 4 filas. Por cada violacion:
- que principio se viola (S, O, L/I o D),
- por que es una violacion (1 a 2 lineas con TUS palabras).
  
I : Segregación de Interfaces: Se viola porque IEmpleadoDeFarmacia tiene muchas funciones distintas el cajero esta obligado a hacer cosas o funciones que no deveria hacer en su trabajo como autorizar ventas controladas o ajustar precios
O : Abierto/Cerrado: Se viola en GestorDePedidos porque utiliza un switch para decidir el descuento segun los tipo de cliente si por algunmotivo aparese un nuevo tipo de cliente se tendria que modificar el codigo creando mas conflicto
D : Inversión de Dependencias: Se viola porque GestorDePedidos crea directamente BaseDeDatosMySql y CorreoSmtp se debiaria crear clases concretasy que dependa de depender de esas clases concretas debería depender de interfaces o abstracciones
S : Responsabilidad unica: Se viola porque GestorDePedidos hace demasiadas cosas dentro de ProcesarPedido: calcula el descuento, guarda el pedido genera el comprobante y envía el correo cada responsabilidad podría estar separada para trabajar de manera eficiente 
  
- donde vive (clase y metodo),

I: IEmpleadoDeFarmacia y Cajero — AutorizarVentaControlada, AjustarPrecio y VerLibroDeControlados
O: GestorDePedidos — ProcesarPedido
D: GestorDePedidos — ProcesarPedido
S: GestorDePedidos — ProcesarPedido
