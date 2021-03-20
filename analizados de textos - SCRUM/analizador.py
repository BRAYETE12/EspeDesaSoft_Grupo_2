# -*- coding: utf-8 -*-

import numpy as np
import nltk
from textblob import TextBlob 
from textblob.sentiments import NaiveBayesAnalyzer
import csv

def importar(url):
    
    archivo = open(url, "r", encoding='utf-8')
    entrada = list( csv.reader(archivo) )   
    entrada.pop(0)
    
    lista = [] 
    palabras = []
    for a in entrada:
        
        blob = TextBlob( a[14], analyzer=NaiveBayesAnalyzer() )
        bagtext =  list(blob.noun_phrases)
        lista.append([ a[2],bagtext, blob.sentiment ]) 
        palabras = palabras + bagtext
        
    fc = frecuencia(lista, palabras)
  #  print( fc )
    
    return lista


def frecuencia(lista, palabras):
    
    palabras = list(np.unique(np.array(palabras)))
    fc = np.empty( len(palabras) )
    lt = []
    
    for l in lista:
        for i in range(len(palabras)):
            fc[i] = fc[i] + l[2].count( palabras[i] )
    
    for i in range(len(palabras)):
        lt.append([ palabras[i], fc[i] ]) 
    
    return lt
    
listado = importar('scopus.csv')

print(listado)