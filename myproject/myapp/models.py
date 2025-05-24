from django.db import models

class Pengguna(models.Model):
    id_pengguna = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Bisa di-hash nanti

    def __str__(self):
        return self.nama

class Uang(models.Model):
    id_uang = models.AutoField(primary_key=True)
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    total_uang = models.DecimalField(max_digits=12, decimal_places=2)
    total_pemasukan = models.DecimalField(max_digits=12, decimal_places=2)
    total_pengeluaran = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Uang {self.pengguna.nama}"

class Catatan(models.Model):
    id_catatan = models.AutoField(primary_key=True)
    uang = models.ForeignKey(Uang, on_delete=models.CASCADE)
    jumlah_uang = models.DecimalField(max_digits=12, decimal_places=2)
    waktu_tanggal = models.DateTimeField()
    status = models.CharField(max_length=20)
    keterangan = models.CharField(max_length=100, default='Tanpa keterangan')

    def __str__(self):
        return f"Catatan {self.id_catatan} - {self.status}"

class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    judul_video = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return self.judul_video

class Menonton(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    waktu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pengguna.nama} menonton {self.video.judul_video}"
