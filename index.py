#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:42:45 2020

@author: h_djeddal
"""
import TextRepresenter as TR
import json

class IndexerSimple (object):
    def __init__(self,corp):
        self.corpus=corp
        
    def indexation(self):
        index= dict()
        index_inverse=dict()
        Trep=TR.PorterStemmer ()
        for doc in self.corpus :
            terms= Trep.getTextRepresentation(text)
            doc_id= doc.getId()
            index[doc_id] = terms
            for t in terms.keys():
                if (t in index_inverse.keys()):
                    if(doc_id in index_inverse[t].keys()):
                        index_inverse[t][doc_id] += terms[t]
                    else:
                        index_inverse[t][doc_id]= terms[t]
                else:
                    index_inverse[t][doc_id]=terms[t]
        self.index=index
        self.index_inverse =index_inverse
        
    def sauve(self):
        fichier_index = open("index.txt", "a")
        fichier_index_inverse = open("index_inverse.txt", "a")
        json.dump(self.index,fichier_index)
        json.dump(self.index_inverse,fichier_index_inverse)
        fichier_index.close()
        fichier_index_inverse.close()
        
a=" d'un paragraphe est marqué par un léger renfoncement ou par un saut de ligne"
a2=" suuuuuuuuuuuuuuuucker "
a3=a+a2
print(a3)
te=t.PorterStemmer ()
f=open("index.txt", "a")
json.dump(te.getTextRepresentation(a3),f)
f.close()
print(te.getTextRepresentation(a3))        