#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:35:09 2020

@author: 3803192
"""



p=Parser()
p.getDocuments("data/cisi/cisi.txt")   
i=IndexerSimple(p.list_doc) 
i.indexation()

def get_score_bool(q,index):
    scores=dict()
    for list(d) in index.items():
        scores[d[0]]=1
        for v in q:
            if(v not in d[1]):
                scores[d[0]]=0
            
    return scores    
        
