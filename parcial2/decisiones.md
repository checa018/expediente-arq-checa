P2.1 - Eleccion y Justificacion de Patrones
Situacion 1: Vencimiento de Membresias

Patron aplicado: Observer
Justificacion: Permite que el modulo de socios mande la senal de vencimiento 
sin saber quien la recibe si no se aplica hay que modificar el codigo de socios 
cada vez que pidan agregar otro aviso como WhatsApp o Promociones lo que rompe los
principios de responsabilidad unica y abierto cerrado


Situacion 2: Calculo Dinamico de Tarifas

Patron aplicado: Strategy
Justificacion: Separa cada regla de cobro en su propia clase para que la logica no 
viva metida en un if/else si no se aplica hay que copiar el mismo bloque de codigo 
en cobros y cotizaciones y cuando el dueno cambie precios por temporada habra que 
modificar ambos lugares arriesgando errores


Situacion 3: Pasarela de Pagos Externa

Patron aplicado: Adapter
Justificacion: Funciona como un traductor entre el SDK externo en ingles con montos
en centavos y el codigo de nuestro gimnasio si no se aplica el dominio queda acoplado 
a la libreria del proveedor actual y cambiarlo el proximo ano exigiria rehacer todo
el sistema de cobros




P2.3 :La Conexión SOLID

La solucion en solucion.py aplica el Principio de Abierto/Cerrado (Open/Closed Principle - OCP)

Se nota en CalculadorTarifaContext. La clase queda intacta sin tener que tocar el codigo ni meter mas if/else cada vez que el dueno cambie las reglas por temporada (cerrada a modificacion). Si manana inventan una tarifa nueva solo creas otra clase con ITarifaStrategy y se la pasas directo con establecer_estrategia() (abierta a extension)
