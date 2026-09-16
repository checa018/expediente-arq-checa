
 P2.1 :Elección y Justificación de Patrones

Situación 1: Vencimiento de Membresías
Patrón aplicado: Observer (Observador).

Justificacion: Permite desacoplar el módulo de socios (Sujeto) de los
  destinatarios de los avisos (WhatsApp, Registro, Recepción, Promociones).
 Si no se aplica, se viola el principio Open/Closed y Single Responsibility,
  ya que cada nuevo módulo interesado obliga a modificar y re-probar el código central de socios,
  generando alta rigidez y acoplamiento

Situación 2: Cálculo Dinámico de Tarifas
Patrón aplicado: Strategy (Estrategia).
Justificación: Encapsula cada algoritmo de cálculo de tarifa 
(Mañana, Noche, Fin de Semana) en clases independientes bajo un contrato común.
Si no se aplica, la duplicación del bloque `if/else` en cobros y cotizaciones genera 
inconsistencias cuando el dueño cambia las reglas de temporada y exige modificar código condicional complejo

 Situación 3: Pasarela de Pagos Externa
Patrón aplicado:Adapter (Adaptador)
Justificación:*Convierte la interfaz incompatible del SDK
externo a los métodos requeridos por nuestro dominio
Si no se aplica, el sistema de cobros se acopla a detalles de terceros 
(centavos, tokens, inglés), impidiendo cambiar de proveedor el próximo año sin reescribir la lógica de la aplicación





P2.3 :La Conexión SOLID

La solución en `solucion.py` aplica el **Principio de Abierto/Cerrado (Open/Closed Principle - OCP). 

Se evidencia en la clase `CalculadorTarifaContext`, la cual queda cerrada a modificaciones (no requiere alterar código ni usar `if/else` al cambiar de 
temporada) y abierta a extensiones mediante el método `establecer_estrategia()`, permitiendo agregar nuevas tarifas heredando de `ITarifaStrategy` en la línea del método `obtener_cobro`.
