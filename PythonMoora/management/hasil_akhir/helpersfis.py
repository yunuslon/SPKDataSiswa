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
na = NilaiAkademik.objects.all().filter(mata_pelajaran='fisika')

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

def Hasil_KarakterFis(na):
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

def Hasil_KelasFis(na):
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

def Hasil_PlombaFis(na):
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

def Hasil_NilaiAkademikFis(na):
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

def HasilTesFis(na):
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

def Matrix_DataAwalFis(na):
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

def Matrix_TernormalisasiFis(na):
    swa= ListSiswa(na)
    nak=round(Hasil_NilaiAkademikFis(na),5)
    hk=round(Hasil_KarakterFis(na),5)
    hp=round(Hasil_PlombaFis(na),5)
    ht=round(HasilTesFis(na),5)
    hkl=round(Hasil_KelasFis(na),5)
    new = pd.concat([swa,nak,hk,hp,ht,hkl],axis=1)
    return new
###############################Matrix Pembobotan###########################################################

def Matrix_PembobotanFis(na):
    swa= ListSiswa(na)
    nak=round(Hasil_NilaiAkademikFis(na)*(bb[0].nilai_akademik/100),5)
    hk=round(Hasil_KarakterFis(na)*(bb[0].karakter/100),5)
    hp=round(Hasil_PlombaFis(na)*(bb[0].plomba/100),5)
    ht=round(HasilTesFis(na)*(bb[0].hasil_tes/100),5)
    hkl=round(Hasil_KelasFis(na)*(bb[0].kelas/100),5)
    
    new = pd.concat([swa,nak,hk,hp,ht,hkl],axis=1)
    return new

###############################Hasil Akhir###########################################################

def Hasil_AkhirFis(na):
    swa= ListSiswa(na)
    nak=Hasil_NilaiAkademikFis(na)*(bb[0].nilai_akademik/100)
    hk=Hasil_KarakterFis(na)*(bb[0].karakter/100)
    hp=Hasil_PlombaFis(na)*(bb[0].plomba/100)
    ht=HasilTesFis(na)*(bb[0].hasil_tes/100)
    hkl=Hasil_KelasFis(na)*(bb[0].kelas/100)
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
