# Selección e Integración del Patrón — Observer (Observador)

## 1. Requerimiento del dominio
Cuando un pedido queda preparado, el estudiante debe recibir un aviso

## 2. Patrón aplicado
Observer (Publicador / Suscriptor)

## 3. Diseño del patrón en Diagrama (Mermaid)

```mermaid
classDiagram
    class Pedido {
        +string estudiante
        +string tipoMenu
        +string estado
        +suscribir(IObservadorPedido obs)
        +cambiarEstadoAPreparado()
        -notificar()
    }

    class IObservadorPedido {
        <<interface>>
        +onPedidoPreparado(pedido)
    }

    class EstudianteNotificador {
        +onPedidoPreparado(pedido)
    }

    class PantallaCocinaNotificador {
        +onPedidoPreparado(pedido)
    }

    Pedido "1" --> "*" IObservadorPedido : notifica a
    EstudianteNotificador ..|> IObservadorPedido
    PantallaCocinaNotificador ..|> IObservadorPedido
```

## 4. Justificación
¿por que ese patron?: permite conectar o desconectar facilmente los canales
de notificacion. cuando el pedido cambia a preparado, pedido envia el
aviso sin importar si es por correo, app movil o pantalla de cocina

¿que pasa sin el?: pedido tendria que llamar directamente a clases
como correouniversitario.enviar(). esto une demasiado el pedido con
la mensajeria y afecta srp (responsabilidad unica) y ocp(abierto/cerrado)
porque para agregar otro canal habria que modificar pedido
