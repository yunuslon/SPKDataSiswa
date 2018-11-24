import os,django
import pandas as pd
from orm.models import Siswa,Kelas,Karakter,HasilTes,NilaiAkademik,Plomba,TesOlimpiade,Bobot
import math
from django.contrib.auth.models import User

sw = Siswa.objects.all()

def ListDataSiswa(sw):
    if len(sw)>0:
        cols = ['id','username','siswa','alamat','mata_pelajaran','nilai_akademik','jenjang',
               'sikap','intensitas']
        dt ={
            cols[0] : [int(a.id) for a in sw],
            cols[1] : [str(a.user) for a in sw],
            cols[2] : [str(a.nama) for a in sw],
            cols[3] : [str(a.alamat) for a in sw],
            cols[4] : [str(a.nilai_akademiks.mata_pelajaran) for a in sw],
            cols[5] : [int(a.nilai_akademiks.nilai) for a in sw],
            cols[6] : [str(a.kelass.jenjang) for a in sw],
            cols[7] : [str(a.karakters.sikap) for a in sw],
            cols[8] : [str(a.plombas.intensitas) for a in sw],
        }
        dfdata_siswa = pd.DataFrame(data=dt)
        return dfdata_siswa
    else:
        return[]
def Data_SiswaBio(sw):
    def SlkIdBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.id))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['Id'])
        return df

    def SlkUsernameBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.username))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['username'])
        return df

    def SlkSiswaBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.siswa))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['siswa'])
        return df

    def SlkAlamatBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.alamat))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['alamat'])
        return df

    def SlkMataPelajaranBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.mata_pelajaran))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['mata_pelajaran'])
        return df

    def SlkNilaiAkademikBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.nilai_akademik))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['nilai_akademik'])
        return df

    def SlkJenjangBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.jenjang))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['jenjang'])
        return df

    def SlkSikapBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.sikap))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['sikap'])
        return df

    def SlkIntensitasBio(sw):
        c= ListDataSiswa(sw)
        tmpA=list(zip(c.mata_pelajaran,c.intensitas))
        tmp=[]
        for i in range(len(c)):
            if tmpA[i][0] == "biologi":
                tmp.append(tmpA[i][1])
        df=pd.DataFrame(data=tmp,columns=['intensitas'])
        return df
    new=pd.concat([SlkIdBio(sw),SlkUsernameBio(sw),SlkSiswaBio(sw),SlkAlamatBio(sw),SlkMataPelajaranBio(sw),
    SlkNilaiAkademikBio(sw),SlkJenjangBio(sw),SlkSikapBio(sw),SlkIntensitasBio(sw)],axis=1)
    return new