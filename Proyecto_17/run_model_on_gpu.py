
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(path):
    
    """
    Carga la parte de entrenamiento del conjunto de datos desde la ruta.
    """
    
    # coloca tu c�digo aqu�

    return train_gen_flow


def load_test(path):
    
    """
    Carga la parte de validaci�n/prueba del conjunto de datos desde la ruta
    """
    
    #  coloca tu c�digo aqu�

    return test_gen_flow


def create_model(input_shape):
    
    """
    Define el modelo
    """
    
    #  coloca tu c�digo aqu�

    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):

    """
    Entrena el modelo dados los par�metros
    """
    
    #  coloca tu c�digo aqu�

    return model


