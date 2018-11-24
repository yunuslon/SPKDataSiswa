import pandas as pd
import numpy as np
import math
from pandas import DataFrame, read_csv
from orm.models import Kelas,Siswa,HasilTes,Karakter,NilaiAkademik,Plomba,Bobot
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 


#reportPDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='apllication/pdf')
    return None


sw = Siswa.objects.all()
kl = Kelas.objects.all()
krt = Karakter.objects.all()
ht = HasilTes.objects.all()
na = NilaiAkademik.objects.all()
pl = Plomba.objects.all()
bb = Bobot.objects.all()

# Untuk memanggil seluruh data nilai dan mata pelajaran setiap atribut 
def ListNilaiAkademik(sw):
    if len(sw)>0:
        cols = ['mata_pelajaran','nilai']
        
        kel ={
            cols[0] : [str(a.nilai_akademiks.mata_pelajaran) for a in sw],
            cols[1] : [str(a.nilai_akademiks.nilai) for a in sw],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListKelas(sw):
    if len(sw)>0:
        cols = ['mata_pelajaran','nilai']
        
        kel ={
            cols[0] : [str(a.kelass.mata_pelajaran) for a in sw],
            cols[1] : [str(a.kelass.nilai) for a in sw],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListHasilTes(sw):
    if len(sw)>0:
        cols = ['mata_pelajaran','nilai']
        
        kel ={
            cols[0] : [str(a.hasiltess.mata_pelajaran) for a in sw],
            cols[1] : [str(a.hasiltess.nilai) for a in sw],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListPlomba(sw):
    if len(sw)>0:
        cols = ['mata_pelajaran','nilai']
        
        kel ={
            cols[0] : [str(a.plombas.mata_pelajaran) for a in sw],
            cols[1] : [str(a.plombas.nilai) for a in sw],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def ListKarakter(sw):
    if len(sw)>0:
        cols = ['mata_pelajaran','nilai']
        
        kel ={
            cols[0] : [str(a.karakters.mata_pelajaran) for a in sw],
            cols[1] : [str(a.karakters.nilai) for a in sw],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]


###########################untuk menyeleksi data yang bersangkutan dengan olimpiade Biologi##########################
def SlkSiswaBio(sw):
    swa={
        'Nama':[a.kelass.siswa for a in sw ],
        'Mata_Pelajaran':[a.kelass.mata_pelajaran for a in sw ]
        }
    c= pd.DataFrame(data=swa)
    tmpA=list(zip(c.Mata_Pelajaran,c.Nama))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "biologi":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nama'])
    return df

def SlkNilaiAkademikBio(sw):
    c= ListNilaiAkademik(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "biologi":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKelasBio(sw):
    c= ListKelas(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "biologi":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkHasilTesBio(sw):
    c= ListHasilTes(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "biologi":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkPlombaBio(sw):
    c= ListPlomba(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "biologi":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKarakterBio(sw):
    c= ListKarakter(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "biologi":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df
def Hasil_KarakterBio(sw):
    kr=SlkKarakterBio(sw)
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

def Hasil_KelasBio(sw):
    kls=SlkKelasBio(sw)
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

def Hasil_PlombaBio(sw):
    plb=SlkPlombaBio(sw)
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

def Hasil_NilaiAkademikBio(sw):
    nla=SlkNilaiAkademikBio(sw)
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

def HasilTesBio(sw):
    htb=SlkHasilTesBio(sw)
    b = 0
    tampung=[]
    for y in range(len(htb)):
        a=(math.pow(int(htb.Nilai[y]),2))
        b = b+a
    for i in range(len(htb)):
        s = int(htb.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)

    dfhst=pd.DataFrame(data=tampung,columns=['Hasil Tes'])
    return dfhst
# ################################################################################
def Matrix_DataAwalBio(sw):
    swa= SlkSiswaBio(sw)
    nak= SlkNilaiAkademikBio(sw)
    krat= SlkKarakterBio(sw)
    plb= SlkPlombaBio(sw)
    hts= SlkHasilTesBio(sw)
    kls= SlkKelasBio(sw)

    new=pd.concat([swa,nak,krat,plb,hts,kls],axis=1)
    new.columns=['Nama','Nilai_Akademik','Karakter','Pengalaman_lomba','Hasil_Tes','Kelas']
    return new

###############################Matrix Ternormalisasi###########################################################

def Matrix_TernormalisasiBio(sw):
    swa= SlkSiswaBio(sw)
    na=Hasil_NilaiAkademikBio(sw)
    krt=Hasil_KarakterBio(sw)
    pl=Hasil_PlombaBio(sw)
    htm=HasilTesBio(sw)
    hk=Hasil_KelasBio(sw)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Matrix Pembobotan###########################################################

def Matrix_PembobotanBio(sw):
    swa= SlkSiswaBio(sw)
    na=Hasil_NilaiAkademikBio(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterBio(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaBio(sw)*(bb[0].plomba/100)
    htm=HasilTesBio(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasBio(sw)*(bb[0].kelas/100)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Hasil Akhir###########################################################

def Hasil_AkhirBio(sw):
    swa= SlkSiswaBio(sw)
    na=Hasil_NilaiAkademikBio(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterBio(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaBio(sw)*(bb[0].plomba/100)
    htm=HasilTesBio(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasBio(sw)*(bb[0].kelas/100)
    pl.columns=['pl']
    htm.columns=['htm']
    Benefit=na.NilaiAkademik+krt.Karakter+pl.pl+htm.htm
    Rangking=Benefit-hk.Kelas
    ra=round(Rangking,4)
    bnf=round(Benefit,4)
    bhk=round(hk,4)
    new =pd.concat([swa,bnf,bhk,ra],axis=1)
    new.columns=['Nama','Benefit','Coast','Rangking']
    hasil=new.sort_values(['Rangking'],ascending=[False])
    return hasil

#############################################################################################################
#############################################FIsika########################################################
############################################################################################################


def SlkSiswaFis(sw):
    swa={
        'Nama':[a.kelass.siswa for a in sw ],
        'Mata_Pelajaran':[a.kelass.mata_pelajaran for a in sw ]
        }
    c= pd.DataFrame(data=swa)
    tmpA=list(zip(c.Mata_Pelajaran,c.Nama))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "fisika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nama'])
    return df

def SlkNilaiAkademikFis(sw):
    c= ListNilaiAkademik(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "fisika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKelasFis(sw):
    c= ListKelas(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "fisika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkHasilTesFis(sw):
    c= ListHasilTes(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "fisika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkPlombaFis(sw):
    c= ListPlomba(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "fisika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKarakterFis(sw):
    c= ListKarakter(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "fisika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def Hasil_KarakterFis(sw):
    kr=SlkKarakterFis(sw)
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

def Hasil_KelasFis(sw):
    kls=SlkKelasFis(sw)
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

def Hasil_PlombaFis(sw):
    plb=SlkPlombaFis(sw)
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

def Hasil_NilaiAkademikFis(sw):
    nla=SlkNilaiAkademikFis(sw)
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

def HasilTesFis(sw):
    htb=SlkHasilTesFis(sw)
    b = 0
    tampung=[]
    for y in range(len(htb)):
        a=(math.pow(int(htb.Nilai[y]),2))
        b = b+a
    for i in range(len(htb)):
        s = int(htb.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)

    dfhst=pd.DataFrame(data=tampung,columns=['Hasil Tes'])
    return dfhst
# ################################################################################
def Matrix_DataAwalFis(sw):
    swa= SlkSiswaFis(sw)
    nak= SlkNilaiAkademikFis(sw)
    krat= SlkKarakterFis(sw)
    plb= SlkPlombaFis(sw)
    hts= SlkHasilTesFis(sw)
    kls= SlkKelasFis(sw)

    new=pd.concat([swa,nak,krat,plb,hts,kls],axis=1)
    new.columns=['Nama','Nilai_Akademik','Karakter','Pengalaman_lomba','Hasil_Tes','Kelas']
    return new

###############################Matrix Ternormalisasi###########################################################

def Matrix_TernormalisasiFis(sw):
    swa= SlkSiswaFis(sw)
    na=Hasil_NilaiAkademikFis(sw)
    krt=Hasil_KarakterFis(sw)
    pl=Hasil_PlombaFis(sw)
    htm=HasilTesFis(sw)
    hk=Hasil_KelasFis(sw)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Matrix Pembobotan###########################################################

def Matrix_PembobotanFis(sw):
    swa= SlkSiswaFis(sw)
    na=Hasil_NilaiAkademikFis(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterFis(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaFis(sw)*(bb[0].plomba/100)
    htm=HasilTesFis(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasFis(sw)*(bb[0].kelas/100)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Hasil Akhir###########################################################

def Hasil_AkhirFis(sw):
    swa= SlkSiswaFis(sw)
    na=Hasil_NilaiAkademikFis(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterFis(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaFis(sw)*(bb[0].plomba/100)
    htm=HasilTesFis(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasFis(sw)*(bb[0].kelas/100)
    pl.columns=['pl']
    htm.columns=['htm']
    Benefit=na.NilaiAkademik+krt.Karakter+pl.pl+htm.htm
    Rangking=Benefit-hk.Kelas
    ra=round(Rangking,4)
    bnf=round(Benefit,4)
    bhk=round(hk,4)
    new =pd.concat([swa,bnf,bhk,ra],axis=1)
    new.columns=['Nama','Benefit','Coast','Rangking']
    hasil=new.sort_values(['Rangking'],ascending=[False])
    return hasil

    ####################################################################################################
    ###################################Kimia###########################################################
    ###################################################################################################

    ###########################untuk menyeleksi data yang bersangkutan dengan olimpiade kimia##########################
def SlkSiswaKim(sw):
    swa={
        'Nama':[a.kelass.siswa for a in sw ],
        'Mata_Pelajaran':[a.kelass.mata_pelajaran for a in sw ]
        }
    c= pd.DataFrame(data=swa)
    tmpA=list(zip(c.Mata_Pelajaran,c.Nama))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "kimia":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nama'])
    return df

def SlkNilaiAkademikKim(sw):
    c= ListNilaiAkademik(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "kimia":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKelasKim(sw):
    c= ListKelas(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "kimia":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkHasilTesKim(sw):
    c= ListHasilTes(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "kimia":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkPlombaKim(sw):
    c= ListPlomba(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "kimia":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKarakterKim(sw):
    c= ListKarakter(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "kimia":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def Hasil_KarakterKim(sw):
    kr=SlkKarakterKim(sw)
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

def Hasil_KelasKim(sw):
    kls=SlkKelasKim(sw)
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

def Hasil_PlombaKim(sw):
    plb=SlkPlombaKim(sw)
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

def Hasil_NilaiAkademikKim(sw):
    nla=SlkNilaiAkademikKim(sw)
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

def HasilTesKim(sw):
    htb=SlkHasilTesKim(sw)
    b = 0
    tampung=[]
    for y in range(len(htb)):
        a=(math.pow(int(htb.Nilai[y]),2))
        b = b+a
    for i in range(len(htb)):
        s = int(htb.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)

    dfhst=pd.DataFrame(data=tampung,columns=['Hasil Tes'])
    return dfhst
# ################################################################################
def Matrix_DataAwalKim(sw):
    swa= SlkSiswaKim(sw)
    nak= SlkNilaiAkademikKim(sw)
    krat= SlkKarakterKim(sw)
    plb= SlkPlombaKim(sw)
    hts= SlkHasilTesKim(sw)
    kls= SlkKelasKim(sw)

    new=pd.concat([swa,nak,krat,plb,hts,kls],axis=1)
    new.columns=['Nama','Nilai_Akademik','Karakter','Pengalaman_lomba','Hasil_Tes','Kelas']
    return new

###############################Matrix Ternormalisasi###########################################################

def Matrix_TernormalisasiKim(sw):
    swa= SlkSiswaKim(sw)
    na=Hasil_NilaiAkademikKim(sw)
    krt=Hasil_KarakterKim(sw)
    pl=Hasil_PlombaKim(sw)
    htm=HasilTesKim(sw)
    hk=Hasil_KelasKim(sw)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Matrix Pembobotan###########################################################

def Matrix_PembobotanKim(sw):
    swa= SlkSiswaKim(sw)
    na=Hasil_NilaiAkademikKim(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterKim(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaKim(sw)*(bb[0].plomba/100)
    htm=HasilTesKim(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasKim(sw)*(bb[0].kelas/100)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Hasil Akhir###########################################################

def Hasil_AkhirKim(sw):
    swa= SlkSiswaKim(sw)
    na=Hasil_NilaiAkademikKim(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterKim(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaKim(sw)*(bb[0].plomba/100)
    htm=HasilTesKim(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasKim(sw)*(bb[0].kelas/100)
    pl.columns=['pl']
    htm.columns=['htm']
    Benefit=na.NilaiAkademik+krt.Karakter+pl.pl+htm.htm
    Rangking=Benefit-hk.Kelas
    ra=round(Rangking,4)
    bnf=round(Benefit,4)
    bhk=round(hk,4)
    new =pd.concat([swa,bnf,bhk,ra],axis=1)
    new.columns=['Nama','Benefit','Coast','Rangking']
    hasil=new.sort_values(['Rangking'],ascending=[False])
    return hasil
####################################################################################################
    ###################################Matematika###########################################################
    ###################################################################################################



def SlkSiswaMat(sw):
    swa={
        'Nama':[a.kelass.siswa for a in sw ],
        'Mata_Pelajaran':[a.kelass.mata_pelajaran for a in sw ]
        }
    c= pd.DataFrame(data=swa)
    tmpA=list(zip(c.Mata_Pelajaran,c.Nama))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "matematika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nama'])
    return df

def SlkNilaiAkademikMat(sw):
    c= ListNilaiAkademik(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "matematika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKelasMat(sw):
    c= ListKelas(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "matematika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkHasilTesMat(sw):
    c= ListHasilTes(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "matematika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkPlombaMat(sw):
    c= ListPlomba(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "matematika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def SlkKarakterMat(sw):
    c= ListKarakter(sw)
    tmpA=list(zip(c.mata_pelajaran,c.nilai))
    tmp=[]
    for i in range(len(c)):
        if tmpA[i][0] == "matematika":
            tmp.append(tmpA[i][1])
    df=pd.DataFrame(data=tmp,columns=['Nilai'])
    return df

def Hasil_KarakterMat(sw):
    kr=SlkKarakterMat(sw)
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

def Hasil_KelasMat(sw):
    kls=SlkKelasMat(sw)
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

def Hasil_PlombaMat(sw):
    plb=SlkPlombaMat(sw)
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

def Hasil_NilaiAkademikMat(sw):
    nla=SlkNilaiAkademikMat(sw)
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

def HasilTesMat(sw):
    htb=SlkHasilTesMat(sw)
    b = 0
    tampung=[]
    for y in range(len(htb)):
        a=(math.pow(int(htb.Nilai[y]),2))
        b = b+a
    for i in range(len(htb)):
        s = int(htb.Nilai[i])
        ad=s/(math.sqrt(b))
        tampung.append(ad)

    dfhst=pd.DataFrame(data=tampung,columns=['Hasil Tes'])
    return dfhst
# ################################################################################
def Matrix_DataAwalMat(sw):
    swa= SlkSiswaMat(sw)
    nak= SlkNilaiAkademikMat(sw)
    krat= SlkKarakterMat(sw)
    plb= SlkPlombaMat(sw)
    hts= SlkHasilTesMat(sw)
    kls= SlkKelasMat(sw)

    new=pd.concat([swa,nak,krat,plb,hts,kls],axis=1)
    new.columns=['Nama','Nilai_Akademik','Karakter','Pengalaman_lomba','Hasil_Tes','Kelas']
    return new

###############################Matrix Ternormalisasi###########################################################

def Matrix_TernormalisasiMat(sw):
    swa= SlkSiswaMat(sw)
    na=Hasil_NilaiAkademikMat(sw)
    krt=Hasil_KarakterMat(sw)
    pl=Hasil_PlombaMat(sw)
    htm=HasilTesMat(sw)
    hk=Hasil_KelasMat(sw)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Matrix Pembobotan###########################################################

def Matrix_PembobotanMat(sw):
    swa= SlkSiswaMat(sw)
    na=Hasil_NilaiAkademikMat(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterMat(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaMat(sw)*(bb[0].plomba/100)
    htm=HasilTesMat(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasMat(sw)*(bb[0].kelas/100)
    
    new = pd.concat([swa,na,krt,pl,htm,hk],axis=1)
    return new

###############################Hasil Akhir###########################################################

def Hasil_AkhirMat(sw):
    swa= SlkSiswaMat(sw)
    na=Hasil_NilaiAkademikMat(sw)*(bb[0].nilai_akademik/100)
    krt=Hasil_KarakterMat(sw)*(bb[0].karakter/100)
    pl=Hasil_PlombaMat(sw)*(bb[0].plomba/100)
    htm=HasilTesMat(sw)*(bb[0].hasil_tes/100)
    hk=Hasil_KelasMat(sw)*(bb[0].kelas/100)
    pl.columns=['pl']
    htm.columns=['htm']
    Benefit=na.NilaiAkademik+krt.Karakter+pl.pl+htm.htm
    Rangking=Benefit-hk.Kelas
    ra=round(Rangking,4)
    bnf=round(Benefit,4)
    bhk=round(hk,4)
    new =pd.concat([swa,bnf,bhk,ra],axis=1)
    new.columns=['Nama','Benefit','Coast','Rangking']
    hasil=new.sort_values(['Rangking'],ascending=[False])
    return hasil