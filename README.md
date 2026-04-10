💳 FinTrans-Analytics – Microsoft Fabric
Arquitectura analítica orientada a transacciones financieras, desarrollada en Microsoft Fabric con enfoque en Lakehouse + Spark + Power BI.

📌 Resumen Ejecutivo
Implementación de una solución estructurada para transformación, modelado dimensional y análisis de datos financieros.

Generación de métricas ejecutivas y visualización estratégica.

Diseñado bajo restricciones reales de entorno (cuenta educativa), priorizando integridad de datos y lógica de negocio.

🏢 Contexto Empresarial
Una organización de servicios financieros requiere:

Consolidar transacciones en un modelo estructurado.

Generar métricas mensuales y comparativas.

Identificar productos y cuentas de mayor impacto.

Analizar distribución por canal y tipo de transacción.

Preparar datos confiables para reporting ejecutivo.

🏗️ Arquitectura General
Lakehouse → almacenamiento de datos.

PySpark → limpieza y transformación.

Modelo dimensional tipo estrella → integridad y escalabilidad.

Power BI → visualización ejecutiva.

Flujo lógico:

Código
Datos brutos → Limpieza y transformación → Modelo dimensional → Agregaciones → Panel de control (Power BI)
🧹 Ingeniería de Datos
Ingesta inicial de 1000 registros transaccionales.

Validación de estructura y tipos de datos.

Normalización de montos negativos.

Creación de columnas derivadas:

ImportePositivo

IsCredit / IsDebit

Año / Mes

Validación de consistencia en valores.

🏗️ Modelado Dimensional
Tabla de hechos: FactTransaction

Dimensiones:

DimDate

DimProduct

DimAccount

Diseño estrella con claves sustitutas para integridad y escalabilidad.

📈 Métricas Estratégicas
Ingresos totales mensuales.

Distribución por tipo de transacción.

Top 5 productos por monto.

Top 5 cuentas por volumen.

Análisis por canal de operación.

Tabla agregada optimizada: FactTransaction_Summary.

📊 Visualización en Power BI
Evolución mensual de transacciones.

Ranking de productos y cuentas.

Distribución por canal.

Segmentación por tipo de transacción.

(Pantallazos incluidos en carpeta pantallazos/).

⚙️ Restricciones Técnicas
Entorno educativo con capacidad limitada.

Sin soporte para streaming en tiempo real.

Sin activación de IA avanzada.

Decisión estratégica: priorizar arquitectura sólida y métricas claras.

🌍 Impacto y Escalabilidad
Escalable a ingesta en tiempo real.

Integración futura con modelos predictivos.

Extensión hacia análisis de riesgo o scoring.

Preparado para entornos productivos sin rediseño estructural.

👤 Autor
Mauricio Vélez Rengifo  
Ingeniero de Datos | Desarrollador Backend

GitHub: Mvelezrengifo

LinkedIn: Mauricio Vélez
