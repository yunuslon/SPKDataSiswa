from django.db import models
from django.contrib.auth.models import User
import time
import os
from orm import FileUploader



class Siswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Laki = 'Laki - Laki'
    Perempuan = 'Perempuan'
    JK_CHOICES  = (
        (Laki, 'Laki - Laki'),
        (Perempuan, 'Perempuan'),
    )
    jenis_kelamin = models.CharField(
        max_length=15,
        choices=JK_CHOICES,
        default=Laki,
    )
    alamat = models.TextField(blank=True, null=True)
   

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Siswa'
        ordering = ['id']

class NilaiAkademik(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='nilai_akademiks', blank=True, null=True)   

    biologi = 'biologi'
    fisika = 'fisika'
    kimia = 'kimia'
    matematika = 'matematika'
    mp_choise  = (
        (biologi, 'Biologi'),
        (fisika, 'Fisika'),
        (kimia, 'Kimia'),
        (matematika, 'Matematika'),
    )
    mata_pelajaran = models.CharField(
        max_length=10,
        choices=mp_choise,
        default=biologi,
    )
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Nilai_Akademik'
        ordering = ['id']

class HasilTes(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='hasiltess', blank=True, null=True)   
    biologi = 'biologi'
    fisika = 'fisika'
    kimia = 'kimia'
    matematika = 'matematika'
    mp_choise  = (
        (biologi, 'Biologi'),
        (fisika, 'Fisika'),
        (kimia, 'Kimia'),
        (matematika, 'Matematika'),
    )
    mata_pelajaran = models.CharField(
        max_length=10,
        choices=mp_choise,
        default=biologi,
    )
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'HasilTes'
        ordering = ['id']

class Kelas(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='kelass', blank=True, null=True)   
    biologi = 'biologi'
    fisika = 'fisika'
    kimia = 'kimia'
    matematika = 'matematika'
    mp_choise  = (
        (biologi, 'Biologi'),
        (fisika, 'Fisika'),
        (kimia, 'Kimia'),
        (matematika, 'Matematika'),
    )
    mata_pelajaran = models.CharField(
        max_length=10,
        choices=mp_choise,
        default=biologi,
    )

    jenjang = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

  
    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Kelas'
        ordering = ['id']


class Karakter(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='karakters', blank=True, null=True)
    biologi = 'biologi'
    fisika = 'fisika'
    kimia = 'kimia'
    matematika = 'matematika'
    mp_choise  = (
        (biologi, 'Biologi'),
        (fisika, 'Fisika'),
        (kimia, 'Kimia'),
        (matematika, 'Matematika'),
    )
    mata_pelajaran = models.CharField(
        max_length=10,
        choices=mp_choise,
        default=biologi,
    )
    sikap = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Karakter'
        ordering = ['id']

class Plomba(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='plombas', blank=True, null=True)
    biologi = 'biologi'
    fisika = 'fisika'
    kimia = 'kimia'
    matematika = 'matematika'
    mp_choise  = (
        (biologi, 'Biologi'),
        (fisika, 'Fisika'),
        (kimia, 'Kimia'),
        (matematika, 'Matematika'),
    )
    mata_pelajaran = models.CharField(
        max_length=10,
        choices=mp_choise,
        default=biologi,
    )

    intensitas = models.CharField(max_length=120, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Plomba'
        ordering = ['id']

class TesOlimpiade(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tesolimpiades')
    biologi = 'biologi'
    fisika = 'fisika'
    kimia = 'kimia'
    matematika = 'matematika'
    mp_choise  = (
        (biologi, 'Biologi'),
        (fisika, 'Fisika'),
        (kimia, 'Kimia'),
        (matematika, 'Matematika'),
    )
    mata_pelajaran = models.CharField(
        max_length=10,
        choices=mp_choise,
        default=biologi,
    )

    no = models.IntegerField(default=0)
    gambar = models.ImageField(upload_to=FileUploader.file_foto,
                             null=True,
                             blank=True,
                             help_text="Upload Foto Soal Anda",
                             default="../media/gambar/icon.png"
                             )

    pertayaan = models.TextField(blank=True, null=True)
    jawabanA = models.CharField(max_length=200, blank=True, null=True)
    jawabanB = models.CharField(max_length=200, blank=True, null=True)
    jawabanC = models.CharField(max_length=200, blank=True, null=True)
    jawabanD = models.CharField(max_length=200, blank=True, null=True)
    jawabanE = models.CharField(max_length=200, blank=True, null=True)
    kunci = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.pertayaan

    class Meta:
        db_table = 'TesOlimpiade'
        ordering = ['id']

class Bobot(models.Model):
    nilai_akademik = models.IntegerField(default=0)
    hasil_tes = models.IntegerField(default=0)
    kelas = models.IntegerField(default=0)
    karakter = models.IntegerField(default=0)
    plomba = models.IntegerField(default=0)

    # def __str__(self):
    #     return self

    class Meta:
        db_table = 'Bobot'
        ordering = ['id']

class SoalBiologi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama
    
  

class SoalFisika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama

class SoalKimia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama


class SoalMatematika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama
    
   