
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:00:23 2020

@author: 3803192
"""
import TextRepresenter as TR
import json

class Document(object):
     def __init__(self,id,titre="",date="",auteur="",mc="",txt="",lien=""):
         self.id=id
         self.txt=txt
         self.titre=titre
         self.date=date
         self.auteur=auteur
         self.mc=mc
         self.txt=txt
         self.lien=lien
     def getId(self):
         return self.id
     def getText(self):
         return self.txt
         
         
class Parser ():
    def __init__(self):
        self.list_doc=[]
    def getDocuments(self,nomfichier):
        l=1
        fichier = open(nomfichier, "r")
        read=False
        lignes = fichier.readlines()
        fichier.close() 
        prem=True
        lien=''
        texte=''
        mot_cle =''
        auteur = ''
        titre = ''
        date=''
        id=''
        ligne = lignes[0].strip()
        while(l<len(lignes)):
            
            if(read):
                ligne = lignes[l].strip()
                l+=1
                if(l==len(lignes)):
                    break;
            if(ligne[0:2]==".I"):
                read=True
                if(not prem):#On cree un nouveau doc
                    self.list_doc.append(Document(id,titre,date,auteur,mot_cle,texte,lien))  
                    lien=''
                    texte=''
                    mot_cle =''
                    auteur = ''
                    titre = ''
                    date=''
                    id='' 
                id=int(ligne[3:])
                prem=False
            if(ligne==".T"):
                read=True
                titre = lignes[l].strip()
                l+=1   
                
            if(ligne==".B"):
                read=True
                date = lignes[l].strip()
                l+=1 
                
            if(ligne==".A"):
                ligne = lignes[l].strip()
                l+=1
               
                while(l<len(lignes) and ligne[0:2]!=".C" and ligne[0:2]!=".I" and ligne[0:2]!=".T" and ligne[0:2]!=".B" and ligne[0:2]!=".A" and ligne[0:2]!=".W" and ligne[0:2]!=".X" and ligne[0:2]!=".K"):
                    auteur += ligne
                    ligne = lignes[l].strip()
                    l+=1
                    
                read=False
                
            if(ligne==".K"):
                ligne = lignes[l].strip()
                l+=1
                
                while(l<len(lignes) and ligne[0:2]!=".C" and ligne[0:2]!=".I" and ligne[0:2]!=".T" and ligne[0:2]!=".B" and ligne[0:2]!=".A" and ligne[0:2]!=".W" and ligne[0:2]!=".X" and ligne[0:2]!=".K"):
                    mot_cle += ligne
                    ligne = lignes[l].strip()
                    l+=1
                read=False
                
                    
            if(ligne==".W"):
                ligne = lignes[l].strip()
                l+=1
                while(l<len(lignes) and ligne[0:2]!=".C" and ligne[0:2]!=".I" and ligne[0:2]!=".T" and ligne[0:2]!=".B" and ligne[0:2]!=".A" and ligne[0:2]!=".W" and ligne[0:2]!=".X" and ligne[0:2]!=".K"):
                    texte += ligne
                    ligne = lignes[l].strip()
                    l+=1
                read=False
                
            if(ligne==".X"):
                
                ligne =lignes[l].strip()
                l+=1
                while(l<len(lignes) and ligne[0:2]!=".C" and ligne[0:2]!=".I" and ligne[0:2]!=".T" and ligne[0:2]!=".B" and ligne[0:2]!=".A" and ligne[0:2]!=".W" and ligne[0:2]!=".X" and ligne[0:2]!=".K"):
                    lien += ligne
                    ligne = lignes[l].strip()
                    l+=1
                read=False
            if(ligne==".C"):
                
                ligne = lignes[l].strip()
                l+=1
                while(l<len(lignes) and ligne[0:2]!=".I" and ligne[0:2]!=".T" and ligne[0:2]!=".B" and ligne[0:2]!=".A" and ligne[0:2]!=".W" and ligne[0:2]!=".X" and ligne[0:2]!=".K"):
                    ligne = lignes[l].strip()
                    l+=1
                read=False
        
        return        
class IndexerSimple (object):
    def __init__(self,corp):
        self.corpus=corp
        
    def indexation(self):
        index= dict()
        index_inverse=dict()
        Trep=TR.PorterStemmer ()
        for doc in self.corpus :
            terms= Trep.getTextRepresentation(doc.getText())
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

          
p=Parser()
p.getDocuments("data/cisi/cisi.txt")   
i=IndexerSimple(p.list_doc)          
                
                
                
                
                
            
        