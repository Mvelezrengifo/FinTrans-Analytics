FinTrans-Analytics

Financial Transaction Analytics Architecture | Microsoft Fabric

Executive Summary

FinTrans-Analytics es una implementación de arquitectura analítica orientada a transacciones financieras, desarrollada en Microsoft Fabric.

El proyecto diseña y construye una solución estructurada para la transformación, modelado dimensional y análisis de datos transaccionales, habilitando métricas ejecutivas y visualización estratégica.

Se trabajó bajo restricciones reales de entorno (capacidad limitada de cuenta educativa), priorizando diseño estructural, integridad de datos y lógica de negocio.

Business Context

Una organización de servicios financieros requiere:

Consolidar transacciones en un modelo estructurado.

Generar métricas mensuales y comparativas.

Identificar productos y cuentas de mayor impacto.

Analizar distribución por canal y tipo de transacción.

Preparar datos confiables para reporting ejecutivo.

El objetivo fue diseñar una arquitectura analítica que soporte estas necesidades.

Architecture Overview

La solución fue construida en Microsoft Fabric utilizando:

Lakehouse como capa de almacenamiento.

Transformación con PySpark.

Modelado dimensional tipo estrella.

Power BI como capa de visualización.

Arquitectura lógica:

Raw Data → Cleaning & Transformation → Dimensional Model → Aggregations → Dashboard Layer

Data Engineering Layer
Ingesta

Carga inicial de dataset transaccional (1,000 registros).

Validación de estructura y tipos de datos.

(La ingesta en tiempo real no fue implementada debido a restricciones de capacidad del entorno. La arquitectura está preparada para soportarla.)

Data Cleaning & Transformation

Normalización de montos negativos.

Creación de columnas derivadas:

TransactionAmount_Positive

IsCredit

IsDebit

Conversión de fechas y generación de columnas Year / Month.

Validación de consistencia en tipos y valores.

Dimensional Modeling

Se implementó un modelo estrella compuesto por:

Fact Table

FactTransaction

Dimensions

DimDate

DimProduct

DimAccount

Se utilizaron surrogate keys para garantizar integridad y escalabilidad.

Este diseño permite:

Análisis temporal eficiente.

Segmentación por producto y cuenta.

Escalabilidad futura para nuevas dimensiones.

Metrics & Business Logic

Se desarrollaron agregaciones estratégicas:

Total Revenue mensual.

Distribución por tipo de transacción.

Top 5 productos por monto.

Top 5 cuentas por volumen transaccional.

Análisis por canal de operación.

Se generó una tabla agregada optimizada para reporting:
FactTransaction_Summary

Visualization Layer

Se construyó un dashboard en Power BI que incluye:

Evolución mensual de transacciones.

Ranking de productos y cuentas.

Distribución por canal.

Segmentación por tipo de transacción.

Pantallazos incluidos en la carpeta pantallazos/.

(Integración con IA y PNF no fue posible por restricciones del entorno, pero el modelo está preparado para extenderse a capacidades avanzadas.)

Technical Constraints & Design Decisions

Entorno con capacidad limitada (cuenta educativa).

Sin soporte para streaming en tiempo real.

Sin activación de funcionalidades avanzadas de IA.

Decisión estratégica:
Priorizar arquitectura sólida, modelo dimensional correcto y métricas de negocio claras sobre componentes no críticos.

Impact & Scalability

La solución permite:

Escalabilidad a ingesta en tiempo real.

Integración futura con modelos predictivos.

Extensión hacia análisis de riesgo o scoring.

Implementación en entornos empresariales sin rediseño estructural.

El diseño está preparado para evolucionar hacia un entorno productivo.