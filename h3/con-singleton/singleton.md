Justificación patrón singleton
Análisis en el Sistema de Gestión y Seguimiento de Encomiendas

En el dominio de logística de encomiendas, las entidades principales como `Encomienda`, `PuntoDeControl` y `Entrega` 
son objetos de negocio múltiples y altamente dinámicos, por lo que la aplicación del patrón Singleton sobre ellas sería 
un antipatrón (Stateful Global Class).

¿Por qué no se aplica Singleton en las clases base?
1: Multiplicidad de Instancias:Cada encomienda tiene su propio estado, historial de tramos y destinatario.
Forzar un Singleton en las entidades rompería el modelo relacional del sistema.

2: Concurrencia: En un sistema de seguimiento masivo (donde operan múltiples operadores logísticos y clientes en al mismo tiempo),
un Singleton global crearía un cuello de botella innecesario en el acceso a datos.

Si fuera necesario:
El único componente donde Singleton estaría justificado en la fase final de infraestructura sería en el administrador de conexiones
de la base de datos (`DatabaseConnectionPool`) o en un hub centralizador de Notificaciones Push, pero **no** dentro del corazón del
dominio logístico
