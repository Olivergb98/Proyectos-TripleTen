# Proyecto final: Predicción de cancelación de clientes en empresa de telecomunicaciones

El objetivo del proyecto es poder predecir qué clientes pueden cancelar el servicio para poder tomar acciones antes de que suceda.


## Contenido del Proyecto

- `Proyecto_final.ipynb`: análisis exploratorio, preparación de datos, modelado y conclusiones
- `dataset/`: contiene los archivos CSV originales provistos.


## Objetivo

Detectar clientes en riesgo de churn utilizando modelos de Machine Learning, para que la empresa pueda intervenir a tiempo con campañas de retención.

## Modelos de Machine Learning

Se probaron múltiples algoritmos de clasificación:

- K-Nearest Neighbors
- Árboles de Decisión
- Random Forest
- XGBoost
- LightGBM
- Regresión Logística

### ⚖️ Métricas de Evaluación

Dado que el objetivo es detectar a la mayor cantidad posible de clientes que se van, se priorizó el uso de:

- `Recall Score`: para minimizar los falsos negativos
- `F1 Score`: para balance entre precisión y recall
- `ROC-AUC`: para evaluación general del modelo

## Mejor Modelo

La **Regresión Logística** ofreció el mejor desempeño en términos de `recall_score`, con valores en F1 y ROC_AUC comparables al resto de modelos, sus métreicas fueron : F1': 0.6068, 'Recall': 0.7833, 'ROC AUC': 0.8284


## Aplicación del Modelo

Se generó una columna con la probabilidad de cancelación (`churn_proba`). Los clientes con probabilidad mayor a 0.5 y que aún no han cancelado pueden ser **priorizados para contacto**, ordenados por nivel de riesgo, con facilidad de modificar la tolerancia dependiendo de las prioridades de la empresa.

## Conclusiones

El modelo desarrollado permite a la empresa anticiparse a cancelaciones y tomar decisiones basadas en datos. La Regresión Logística, por su simplicidad y rendimiento, es ideal para un primer despliegue productivo.

