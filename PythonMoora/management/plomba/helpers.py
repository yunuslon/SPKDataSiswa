import pandas as pd
import numpy as np
import math
from pandas import DataFrame, read_csv
from orm.models import Plomba,Siswa

sw=Siswa.objects.all()
pl=Plomba.objects.all()

def ListPlomba(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        plb ={
            cols[0] : [int(a.plombas.nilai) for a in sw],
        }
        dfpl = pd.DataFrame(data=plb)
        return dfpl
    else:
        return[]

def Hasil_Plomba():
    plb=ListPlomba(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(plb.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = plb.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    if len(sw)>0:
        cols = ['intensitas']
        
        plmb ={
            cols[0] : [str(a.plombas.intensitas) for a in sw],
        }
        dfplmb = pd.DataFrame(data=plmb)
    swa={'nama':[a.nama for a in sw]}
    dfswa= pd.DataFrame(data=swa)
    Plomba=pd.DataFrame(data=tampung,columns=['Nilai'])
    new = pd.concat([dfswa,dfplmb, Plomba], axis=1)
    return new


def HasilPlomba_Pembobotan():
    b=Hasil_Plomba()
    lst=list(b)
    y=0
    d=[]
    lst
    
    for i in range(len(b)):
        y =0.15*b.Nilai[i]
        d.append(y)
        pb=pd.DataFrame(d,columns=['Nilai'])
    if len(sw)>0:
        cols = ['intensitas']
        
        plmb ={
            cols[0] : [str(a.plombas.intensitas) for a in sw],
        }
        dfplmb = pd.DataFrame(data=plmb)
    swa={'nama':[a.nama for a in sw]}
    dfswa= pd.DataFrame(data=swa)
    new = pd.concat([dfswa,dfplmb, pb], axis=1)
    return new
















