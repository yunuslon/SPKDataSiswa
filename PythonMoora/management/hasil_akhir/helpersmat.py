import pandas as pd
import numpy as np
import math
from pandas import DataFrame, read_csv
from orm.models import Kelas,Siswa,HasilTes,Karakter,NilaiAkademik,Plomba,Bobot
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 

bb = Bobot.objects.all()
na = NilaiAkademik.objects.all().filter(mata_pelajaran='matematika')

def ListSiswa(na):
    if len(na)>0:
        cols = ['Nama']
        
        kel ={
            cols[0] : [str(a.siswa.nama) for a in na],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListNilaiAkademik(na):
    if len(na)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [str(a.nilai) for a in na],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListKelas(na):
    if len(na)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [str(a.siswa.kelass.nilai) for a in na],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListHasilTes(na):
    if len(na)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [str(a.siswa.hasiltess.nilai) for a in na],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListPlomba(na):
    if len(na)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [str(a.siswa.plombas.nilai) for a in na],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListKarakter(na):
    if len(na)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [str(a.siswa.karakters.nilai) for a in na],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def Hasil_KarakterMat(na):
    kr=ListKarakter(na)
    b = 0
    tampung=[]
    for y in range(len(kr)):
        a = (math.pow(int(kr.Nilai[y]),2))
        b = b+a
    for i in range(len(kr)):
        s = int(kr.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    Karakter=pd.DataFrame(data=tampung,columns=['Karakter'])
    return Karakter

def Hasil_KelasMat(na):
    kls=ListKelas(na)
    b = 0
    tampung=[]
    for y in range(len(kls)):
        a=(math.pow(int(kls.Nilai[y]),2))
        b = b+a
    for i in range(len(kls)):
        s = int(kls.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    Kelas=pd.DataFrame(data=tampung,columns=['Kelas'])
    return Kelas

def Hasil_PlombaMat(na):
    plb=ListPlomba(na)
    b = 0
    tampung=[]
    for y in range(len(plb)):
        a=(math.pow(int(plb.Nilai[y]),2))
        b = b+a
    for i in range(len(plb)):
        s = int(plb.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    Plomba=pd.DataFrame(data=tampung,columns=['Penglaman Lomba'])
    return Plomba

def Hasil_NilaiAkademikMat(na):
    nla=ListNilaiAkademik(na)
    b = 0
    tampung=[]
    for y in range(len(nla)):
        a=(math.pow(int(nla.Nilai[y]),2))
        b = b+a
    for i in range(len(nla)):
        s = int(nla.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    NilaiAkademik=pd.DataFrame(data=tampung,columns=['NilaiAkademik'])
    return NilaiAkademik

def HasilTesMat(na):
    htb=ListHasilTes(na)
    b = 0
    tampung=[]
    for y in range(len(htb)):
        a=(math.pow(int(htb.Nilai[y]),2))
        b = b+a
    for i in range(len(htb)):
        s = int(htb.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)

    dfhst=pd.DataFrame(data=tampung,columns=['Hasil_Tes'])
    return dfhst

def Matrix_DataAwalMat(na):
    swa= ListSiswa(na)
    nak= ListNilaiAkademik(na)
    krat= ListKarakter(na)
    plb= ListPlomba(na)
    hts= ListHasilTes(na)
    kls= ListKelas(na)

    new=pd.concat([swa,nak,krat,plb,hts,kls],axis=1)
    new.columns=['Nama','Nilai_Akademik','Karakter','Pengalaman_lomba','Hasil_Tes','Kelas']
    return new

###############################Matrix Ternormalisasi###########################################################

def Matrix_TernormalisasiMat(na):
    swa= ListSiswa(na)
    nak=round(Hasil_NilaiAkademikMat(na),5)
    hk=round(Hasil_KarakterMat(na),5)
    hp=round(Hasil_PlombaMat(na),5)
    ht=round(HasilTesMat(na),5)
    hkl=round(Hasil_KelasMat(na),5)
    new = pd.concat([swa,nak,hk,hp,ht,hkl],axis=1)
    return new
###############################Matrix Pembobotan###########################################################

def Matrix_PembobotanMat(na):
    swa= ListSiswa(na)
    nak=round(Hasil_NilaiAkademikMat(na)*(bb[0].nilai_akademik/100),5)
    hk=round(Hasil_KarakterMat(na)*(bb[0].karakter/100),5)
    hp=round(Hasil_PlombaMat(na)*(bb[0].plomba/100),5)
    ht=round(HasilTesMat(na)*(bb[0].hasil_tes/100),5)
    hkl=round(Hasil_KelasMat(na)*(bb[0].kelas/100),5)
    
    new = pd.concat([swa,nak,hk,hp,ht,hkl],axis=1)
    return new

###############################Hasil Akhir###########################################################

def Hasil_AkhirMat(na):
    swa= ListSiswa(na)
    nak=Hasil_NilaiAkademikMat(na)*(bb[0].nilai_akademik/100)
    hk=Hasil_KarakterMat(na)*(bb[0].karakter/100)
    hp=Hasil_PlombaMat(na)*(bb[0].plomba/100)
    ht=HasilTesMat(na)*(bb[0].hasil_tes/100)
    hkl=Hasil_KelasMat(na)*(bb[0].kelas/100)
    hp.columns=['pl']
    ht.columns=['htm']
    Benefit=nak.NilaiAkademik+hk.Karakter+hp.pl+ht.htm
    Rangking=Benefit-hkl.Kelas
    ra=round(Rangking,4)
    bnf=round(Benefit,4)
    bhk=round(hkl,4)
    new =pd.concat([swa,bnf,bhk,ra],axis=1)
    new.columns=['Nama','Benefit','Coast','Rangking']
    hasil=new.sort_values(['Rangking'],ascending=[False])
    return hasil
