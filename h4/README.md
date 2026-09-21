# Documentación de Arquitectura - Sistema de Gestión y Rastreo de Encomiendas

## 1. Diagrama C4 Nivel 1: Diagrama de Contexto

Muestra el sistema como una caja central, los actores del dominio y los sistemas externos integrados.

```mermaid
graph TD
    classDef actor fill:#08427b,stroke:#052e56,stroke-width:2px,color:#fff;
    classDef system fill:#1168bd,stroke:#0b4884,stroke-width:2px,color:#fff;
    classDef external fill:#999999,stroke:#666666,stroke-width:2px,color:#fff;

    Cliente["👤 Cliente<br/>(Consulta estado y recibe notificaciones)"]:::actor
    Operador["👤 Operador Logístico<br/>(Registra y actualiza envíos)"]:::actor
    Supervisor["👤 Supervisor<br/>(Supervisa incidencias y entregas)"]:::actor

    SistemaLogistica["📦 Sistema de Gestión y Rastreo de Encomiendas<br/>[Sistema Central]<br/>Gestiona el registro, la asignación de transporte y las notificaciones."]:::system

    ServicioNotif["📱 Servicio Externo de Notificaciones<br/>[Sistema Externo]<br/>Pasarela de WhatsApp / Email"]:::external

    Cliente -->|Consulta estado de encomienda| SistemaLogistica
    Operador -->|Registra encomienda y actualiza estado| SistemaLogistica
    Supervisor -->|Supervisa incidencias| SistemaLogistica
    SistemaLogistica -->|Envía mensajes de evento| ServicioNotif
    ServicioNotif -->|Notifica cambios de estado| Cliente
```

---

## 2. Diagrama C4 Nivel 2: Diagrama de Contenedores

Muestra los contenedores del sistema y la ubicación exacta de los dos patrones fusionados (**Strategy** y **Observer** en `final.py`).

```mermaid
graph TD
    classDef actor fill:#08427b,stroke:#052e56,stroke-width:2px,color:#fff;
    classDef container fill:#1168bd,stroke:#0b4884,stroke-width:2px,color:#fff;
    classDef db fill:#2b78e4,stroke:#1b4d8e,stroke-width:2px,color:#fff;

    Cliente["👤 Cliente"]:::actor
    Operador["👤 Operador Logístico"]:::actor

    subgraph SistemaLogistica ["📦 Sistema de Gestión y Rastreo de Encomiendas"]
        RastreoPantalla["💻 Pantalla de Rastreo / UI<br/>[Contenedor: Web Interface]<br/>Interfaz para consulta y registro de encomiendas."]:::container

        subgraph ModuloCore ["Core Logístico (final.py)"]
            GestorEncomienda["⚙️ GestorEncomienda / Encomienda<br/>[Componente Central]"]:::container
            
            EstrategiaTransporte["🔀 Módulo de Transporte<br/>[Patrón Strategy]<br/>(TransporteAereo / TransporteTerrestre)"]:::container
            
            NotificadorObserver["🔔 Bus de Eventos / Notificador<br/>[Patrón Observer]<br/>(Cliente / Supervisor Observadores)"]:::container
        end

        Database[("🛢️ Base de Datos<br/>[Contenedor: EncomiendaRepositoryBD]<br/>Almacena encomiendas y registros.")]:::db
    end

    Cliente -->|Consulta estado| RastreoPantalla
    Operador -->|Actualiza estado| RastreoPantalla
    RastreoPantalla -->|Invoca| GestorEncomienda
    GestorEncomienda -->|Selecciona algoritmo de envio| EstrategiaTransporte
    GestorEncomienda -->|Dispara notificación de evento| NotificadorObserver
    GestorEncomienda -->|Persiste estado| Database
    NotificadorObserver -->|Notifica cambio| Cliente
```
