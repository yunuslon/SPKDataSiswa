import os,django
import pandas as pd
from orm.models import Siswa,Kelas,Karakter,HasilTes,NilaiAkademik,Plomba,TesOlimpiade,Bobot
import math

tp =TesOlimpiade.objects.all()

def ListTesOlimpiade(tp):
    if len(tp)>0:
        cols = ['mata_pelajaran','no','gambar','pertayaan',
                'jawabanA','jawabanB','jawabanC','jawabanD','jawabanE','kunci']
        
        topd ={
            cols[0] : [str(a.mata_pelajaran) for a in tp],
            cols[1] : [int(a.no) for a in tp],
            cols[2] : [str(a.gambar) for a in tp],
            cols[3] : [str(a.pertayaan) for a in tp],
            cols[4] : [str(a.jawabanA) for a in tp],
            cols[5] : [str(a.jawabanB) for a in tp],
            cols[6] : [str(a.jawabanC) for a in tp],
            cols[7] : [str(a.jawabanD) for a in tp],
            cols[8] : [str(a.jawabanE) for a in tp],
            cols[9] : [str(a.kunci) for a in tp],
        }
        dfmt = pd.DataFrame(data=topd)
        return dfmt
    else:
        return[]

def SleksiSoalBio(tp):
    c= ListTesOlimpiade(tp)
    tmpA=list(zip(c.mata_pelajaran,c.no,c.gambar,c.pertayaan,
                  c.jawabanA,c.jawabanB,c.jawabanC,c.jawabanD,c.jawabanE,c.kunci))
    def no():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp, columns=['No'])
        return df

    def gambar():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][2])
        df=pd.DataFrame(data=tmp, columns=['Gambar'])
        return df
    
    def pertayaan():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][3])
        df=pd.DataFrame(data=tmp, columns=['Pertayaan'])
        return df

    def jawabanA():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][4])
        df=pd.DataFrame(data=tmp, columns=['JawabanA'])
        return df

    def jawabanB():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][5])
        df=pd.DataFrame(data=tmp, columns=['JawabanB'])
        return df

    def jawabanC():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][6])
        df=pd.DataFrame(data=tmp, columns=['JawabanC'])
        return df

    def jawabanD():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][7])
        df=pd.DataFrame(data=tmp, columns=['JawabanD'])
        return df

    def jawabanE():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][8])
        df=pd.DataFrame(data=tmp, columns=['JawabanE'])
        return df
    
    def kunci():
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][9])
        df=pd.DataFrame(data=tmp, columns=['Kunci'])
        return df
    
    gabung= pd.concat([no(),gambar(),pertayaan(),jawabanA(),jawabanB(),jawabanC(),jawabanD(),jawabanE(),kunci()],
                      axis=1)

    return gabung
