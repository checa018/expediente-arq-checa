Deteccion de Violaciones SOLID en esqueleto-A.cs

SRP (Single Responsibility Principle)
  -Donde: En la clase GestorDePedidos (metodo ProcesarPedido).
  -Por que: Realiza multiples tareas no relacionadas: calcula precios, imprime el vale por consola, orquesta la persistencia
   en base de datos y envia correos electronicos
  
OCP (Open/Closed Principle)
  -Donde: En el bloque switch (tipoMenu) dentro de ProcesarPedido.
  -Por que: Si se agrega un nuevo menu (ej. "ejecutivo"), es obligatorio modificar la clase existente, rompiendo el principio 
   de estar abierto a extension pero cerrado a modificacion
   
DIP (Dependency Inversion Principle)
  -Donde: Instanciacion directa con new BaseDeDatosComedor() y new CorreoUniversitario().
  -Por que: El modulo de alto nivel depende de implementaciones concretas de bajo nivel en lugar
   de abstracciones/interfaces (IPedidoRepository, INotificador)
