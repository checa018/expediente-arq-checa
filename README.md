# expediente-arq-checa
Expediente de arquitectura de software

Datos del estudiante
Marco Antonio Checa Mamani

Variante: logistica (Sistema de Gestión y Seguimiento de Encomiendas)


actores del sistema

-	Cliente 
Registra o consulta su encomienda. 
Rastrea su paquete mediante el código de seguimiento. 
Recibe notificaciones sobre cambios de estado. 
-	Operador logístico 
Registra las encomiendas. 
Registra los movimientos de los envíos. 
Actualiza los estados en los puntos de control. 
-	Supervisor 
Supervisa los envíos y movimientos. 
Revisa las incidencias. 
Resuelve problemas relacionados con los envíos. 
-	Administrador del sistema 
Gestiona usuarios y permisos. 
Configura parámetros generales del sistema. 
Supervisa el funcionamiento general. 
-	Aerolínea / Sistema de transporte 
Proporciona información sobre los tramos y movimientos de carga. 
Intercambia información con el sistema de seguimiento.



Inventario de módulos

- Gestión de Encomiendas
Registrar y administrar las encomiendas.
Gestionar código de seguimiento, peso, origen y destino.
- Gestión de Envíos
Consolidar varias encomiendas en un envío.
Administrar la información general del envío.
- Gestión de Tramos
Registrar las diferentes etapas o rutas del envío.
Gestionar origen, destino y medio de transporte de cada tramo.
- Seguimiento y Puntos de Control
Registrar los movimientos de las encomiendas.
Actualizar y consultar el estado del envío en cada punto de control.
- Gestión de Entregas
Registrar la entrega de la encomienda.
Confirmar que el paquete fue recibido por el destinatario.
- Gestión de Incidencias
Registrar problemas durante el transporte.
Permitir al supervisor revisar y resolver las incidencias.
- Notificaciones
Avisar al cliente cuando cambia el estado de su encomienda.
Informar sobre eventos importantes del envío.
- Reportes e Integraciones
Generar reportes de envíos, rutas y tiempos de entrega.
Intercambiar información con sistemas externos como aerolíneas 



classDiagram
    class Usuario {
	    +int idUsuario
	    +string nombre
	    +string rol
	    +login()
    }

    class Encomienda {
	    +string codigoSeguimiento
	    +decimal peso
	    +string estado
	    +consultarEstado()
    }

    class Envio {
	    +string codigoEnvio
	    +date fechaSalida
	    +consolidar()
    }

    class Tramo {
	    +string medioTransporte
	    +date fechaSalida
    }

    class PuntoDeControl {
	    +string ubicacion
	    +date fechaHora
	    +registrarMovimiento()
    }

    class Entrega {
	    +string destinatario
	    +confirmarEntrega()
    }

    class Incidencia {
	    +string descripcion
	    +resolver()
    }

    Usuario "1" --> "0..*" Encomienda : gestiona / consulta
    Usuario "1" --> "0..*" Incidencia : reporta
    Envio "1" o-- "1..*" Encomienda : consolida
    Envio "1" *-- "1..*" Tramo : contiene
    Tramo "1" --> "0..*" PuntoDeControl : registra
    Encomienda "1" --> "0..1" Entrega : finaliza en
    Encomienda "1" --> "0..*" Incidencia : presenta

<img width="1247" height="1097" alt="Captura de pantalla 2026-08-31 210113" src="https://github.com/user-attachments/assets/e37f2655-585a-4b35-87ff-75d9775629dd" />


Atributo 1: Eficiencia (performance)
las búsquedas masivas pueden congelar el sistema. para no saturar la base de datos, separo consultas de registros, y sumo servidores automáticamente por si hay mucho tráfico.

Atributo 2: Fiabilidad
para no perder datos si fallan las aerolíneas. se guardo eventos en espera si cae el internet, aislo los fallos externos para no trabar el sistema.
    



1: Que clase junta negocio + guardado + pantalla
R: encomienda (esta calse mescla consultar estado, pantalla rastreo  y guardar en la base de datos  )
 

2: División en cajas de una sola responsabilidad
Caja 1: encomienda (negocio)
guardar solo los datos puros del paquete (codigoseguimiento, peso, estado)
Caja 2: encomiendarepository (guardado)
guardar, actualizar y consultar los paquetes en la base de datos
Caja 3: rastreopantalla (pantalla)
mostrar la información del rastreo en la pantalla del cliente o del operador

3. Test de departamentos ¿Quién pediría cambios?
Caja encomienda (negocio): Departamento de operaciones y logística 
Caja encomiendarepository (guardado): Departamento de sistemas
Caja rastreopantalla (antalla): Departamento de Diseño o sistemas 



H2

classDiagram

    class Cliente {
        +int idCliente
        +string nombre
        +string telefono
        +string direccion
        +RegistrarEncomienda()
        +ConsultarEstado()
    }

    class OperadorLogistico {
        +int idOperador
        +string nombre
        +RegistrarEncomienda()
        +RegistrarMovimiento()
        +ActualizarEstado()
    }

    class Supervisor {
        +int idSupervisor
        +string nombre
        +SupervisarEnvios()
        +RevisarIncidencias()
        +ResolverIncidencia()
    }

    class Administrador {
        +int idAdministrador
        +string nombre
        +GestionarUsuarios()
        +GestionarPermisos()
        +ConfigurarSistema()
    }


    class IEncomiendaRepository {
        <<interface>>
        +Guardar(encomienda: Encomienda)
        +Actualizar(encomienda: Encomienda)
        +ObtenerPorCodigo(codigo: string) Encomienda
    }

    class INotificador {
        <<interface>>
        +EnviarNotificacion(mensaje: string)
    }

    class ITransporte {
        <<interface>>
        +Transportar(encomienda: Encomienda)
    }

    class IRastreo {
        <<interface>>
        +MostrarEstado(encomienda: Encomienda)
    }


    class Encomienda {
        +string codigoSeguimiento
        +decimal peso
        +string origen
        +string destino
        +string estado
        +DateTime fechaEstimadaLlegada
        +CambiarEstado(nuevoEstado: string)
        +ConsultarEstado()
    }


    class GestorEncomienda {
        +Registrar(encomienda: Encomienda)
        +ActualizarEstado(codigo: string)
        +Consultar(codigo: string)
    }


    
    class EncomiendaRepositoryBD {
        +Guardar(encomienda: Encomienda)
        +Actualizar(encomienda: Encomienda)
        +ObtenerPorCodigo(codigo: string) Encomienda
    }


    class RastreoPantalla {
        +MostrarEstado(encomienda: Encomienda)
    }

 
    class NotificadorCliente {
        +EnviarNotificacion(mensaje: string)
    }



    class TransporteAereo {
        +Transportar(encomienda: Encomienda)
    }

    class TransporteTerrestre {
        +Transportar(encomienda: Encomienda)
    }



    IEncomiendaRepository <|.. EncomiendaRepositoryBD : implementa

    INotificador <|.. NotificadorCliente : implementa

    ITransporte <|.. TransporteAereo : implementa
    ITransporte <|.. TransporteTerrestre : implementa

    IRastreo <|.. RastreoPantalla : implementa


    Cliente "1" --> "0..*" Encomienda : registra / consulta

    OperadorLogistico "1" --> "0..*" Encomienda : registra

    Supervisor "1" --> "0..*" Encomienda : supervisa

    Administrador "1" --> "0..*" OperadorLogistico : gestiona
    Administrador "1" --> "0..*" Supervisor : gestiona


    GestorEncomienda --> Encomienda : gestiona

    GestorEncomienda --> IEncomiendaRepository : usa contrato

    GestorEncomienda --> INotificador : usa contrato

    GestorEncomienda --> ITransporte : usa contrato

    RastreoPantalla --> Encomienda : visualiza


<img width="1754" height="916" alt="Captura de pantalla 2026-09-06 224054" src="https://github.com/user-attachments/assets/2381644b-5d44-4e2a-ba85-9a617c8817d7" />


Revisé mi diagrama del H1 y separé las responsabilidades que estaban concentradas en la clase encomienda  se quedo la clase  encomienda únicamente para manejar los datos y reglas propias de la encomienda y se creo EncomiendaRepositoryBD para encargarse exclusivamente del guardado y consulta de datos. Luego seagrego IEncomiendaRepository para que el sistema dependa de una interfaz y no directamente de la base de datos. También separé el rastreo mediante IRastreo y RastreoPantalla, y las notificaciones mediante INotificador y NotificadorCliente. Eliminé el switch que diferenciaba los tipos de transporte y lo reemplacé por ITransporte, TransporteAereo y TransporteTerrestre, aplicando OCP. Dividí las interfaces en contratos pequeños y específicos para aplicar ISP. Finalmente, agregué los actores Cliente, OperadorLogistico, Supervisor y Administrador para representar claramente sus funciones. Con estos cambios reduje el acoplamiento y logré una arquitectura más organizada, mantenible y fácil de ampliar.<img width="1247" 
