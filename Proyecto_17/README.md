# Visión Artificial

El objetivo del proyecto es crear un modelo con una red neuronal ResNet50 para poder predecir edades basándonos en imágenes.

Se trabaja únicamente con pandas para la lectura de datos, matplotlib para el EDA, y tensorflow para la red neuronal.

El objetivo era lograr un MAE para el conjunto de validación de máximo 8, y se logró conseguir esta métrica de 6.61, por lo que se puede afirmar que el modelo tiene un buen poder predictivo para edades utilizando fotografías.

Para alcanzar la métrica objetivo se tuvieron que realizar varias modificaciones al modelo y al dataset, lo que más impacto tuvo fue añadir una capa Dropout con un dropout rate de .5, ajustar la tasa de aprendizaje del optimizador Adam a 0.00005, y hacer una aumentación del conjunto de entrenamiento para tener más información disponible para entrenar al modelo.