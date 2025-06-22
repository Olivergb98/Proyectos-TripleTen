# Clasificación de Sentimientos con BERT

Este proyecto utiliza modelos de lenguaje basados en transformadores para clasificar sentimientos en reseñas de películas. Se parte de texto crudo y se aplica un pipeline completo de procesamiento, vectorización, entrenamiento y evaluación del modelo.

## Objetivo

Construir un modelo de NLP capaz de detectar el sentimiento (positivo o negativo) en textos utilizando embeddings generados con diferentes módulos de NLP como Bert, Spacy y TfidfVercorizer, y Clasificadores como LightGBM y Logistic Regression.

## Tecnologías usadas

- Python 3.10
- Transformers (HuggingFace)
- PyTorch (con soporte CUDA)
- Scikit-learn
- LightGBM
- NLTK y spaCy
- NumPy, Pandas, Matplotlib, Seaborn

## Instrucciones

Al tener errores de compatibilidad con versiones recientes de python, se utilizó Python 3.10 en un ambiente virtual. Para poder correr el notebook sin problemas, correr en la terminal de bash:
py -3.10 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

## Notas adicionales

1. El dataset se puede descargar en línea, el notebook cuenta con el link ya que puede ser muy pesado.
2. La primera vez que se ejecuta el notebook, el procesamiento con bert será realizado con la gpu, y se guardará un archivo con los resultados para evitar los largos tiempos de procesamiento si se vuelve a ejecutar.