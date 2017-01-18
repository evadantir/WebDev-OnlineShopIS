# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Barang(models.Model):
    bahan = models.CharField(db_column='BAHAN', max_length=20)  # Field name made lowercase.
    kode_barang = models.CharField(db_column='KODE_BARANG', primary_key=True, max_length=5)  # Field name made lowercase.
    kode_tipe = models.ForeignKey('TipeBarang', models.DO_NOTHING, db_column='KODE_TIPE')  # Field name made lowercase.
    nama_barang = models.CharField(db_column='NAMA_BARANG', max_length=15)  # Field name made lowercase.
    deskripsi_barang_field = models.CharField(db_column='DESKRIPSI_BARANG_', max_length=1024)  # Field name made lowercase. Field renamed because it ended with '_'.
    harga_barang = models.DecimalField(db_column='HARGA_BARANG', max_digits=8, decimal_places=0)  # Field name made lowercase.
    waktu_datang_katalog = models.DateTimeField(db_column='WAKTU_DATANG_KATALOG')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barang'

    def __str__(self):
        return self.nama_barang


class BarangPesanan(models.Model):
    id_detail = models.ForeignKey('DetailBarang', models.DO_NOTHING, db_column='ID_DETAIL')  # Field name made lowercase.
    kode_transaksi = models.ForeignKey('Transaksi', models.DO_NOTHING, db_column='KODE_TRANSAKSI')  # Field name made lowercase.
    id_barang_pesanan = models.CharField(db_column='ID_BARANG_PESANAN', primary_key=True, max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barang_pesanan'

    def __str__(self):
        return self.id_barang_pesanan

class Customer(models.Model):
    email = models.CharField(db_column='EMAIL', primary_key=True, max_length=20)  # Field name made lowercase.
    nama_customer = models.CharField(db_column='NAMA_CUSTOMER', max_length=30)  # Field name made lowercase.
    telp_customer = models.CharField(db_column='TELP_CUSTOMER', max_length=12)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.email

class DaftarAlamat(models.Model):
    id_alamat = models.CharField(db_column='ID_ALAMAT', primary_key=True, max_length=6)  # Field name made lowercase.
    email = models.ForeignKey(Customer, models.DO_NOTHING, db_column='EMAIL')  # Field name made lowercase.
    id_kota = models.ForeignKey('Kota', models.DO_NOTHING, db_column='ID_KOTA')  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=25)  # Field name made lowercase.
    kode_pos = models.CharField(db_column='KODE_POS', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daftar_alamat'

    def __str__(self):
        return self.id_alamat

class DetailBarang(models.Model):
    kode_barang = models.ForeignKey(Barang, models.DO_NOTHING, db_column='KODE_BARANG')  # Field name made lowercase.
    id_detail = models.CharField(db_column='ID_DETAIL', primary_key=True, max_length=3)  # Field name made lowercase.
    warna = models.CharField(db_column='WARNA', max_length=50)  # Field name made lowercase.
    foto_barang = models.ImageField(db_column='FOTO_BARANG', upload_to = "image/fotobarang")  # Field name made lowercase.
    stock = models.SmallIntegerField(db_column='STOCK', blank=True, null=True)  # Field name made lowercase.
    ukuran = models.CharField(db_column='UKURAN', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detail_barang'

    def __str__(self):
        return '%s: %s: %s: %s' % (self.warna,self.bahan,self.foto_barang,self.stock)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Kota(models.Model):
    id_kota = models.CharField(db_column='ID_KOTA', primary_key=True, max_length=5)  # Field name made lowercase.
    id_provinsi = models.ForeignKey('Provinsi', models.DO_NOTHING, db_column='ID_PROVINSI')  # Field name made lowercase.
    nama_kota = models.CharField(db_column='NAMA_KOTA', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kota'

    def __str__(self):
        return self.nama_kota


class Provinsi(models.Model):
    id_provinsi = models.CharField(db_column='ID_PROVINSI', primary_key=True, max_length=2)  # Field name made lowercase.
    nama_provinsi = models.CharField(db_column='NAMA_PROVINSI', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provinsi'

    def __str__(self):
        return self.nama_provinsi

class TipeBarang(models.Model):
    kode_tipe = models.CharField(db_column='KODE_TIPE', primary_key=True, max_length=5)  # Field name made lowercase.
    tipe_barang = models.CharField(db_column='TIPE_BARANG', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipe_barang'

    def __str__(self):
        return self.tipe_barang

class Transaksi(models.Model):
    kode_transaksi = models.CharField(db_column='KODE_TRANSAKSI', primary_key=True, max_length=10)  # Field name made lowercase.
    id_alamat = models.ForeignKey(DaftarAlamat, models.DO_NOTHING, db_column='ID_ALAMAT')  # Field name made lowercase.
    email = models.ForeignKey(Customer, models.DO_NOTHING, db_column='EMAIL')  # Field name made lowercase.
    waktu_pemesanan = models.DateTimeField(db_column='WAKTU_PEMESANAN')  # Field name made lowercase.
    kuantitas_barang = models.SmallIntegerField(db_column='KUANTITAS_BARANG', blank=True, null=True)  # Field name made lowercase.
    waktu_dibayar = models.DateTimeField(db_column='WAKTU_DIBAYAR', blank=True, null=True)  # Field name made lowercase.
    bank_tujuan_bayar = models.CharField(db_column='BANK_TUJUAN_BAYAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rek_pengirim = models.CharField(db_column='REK_PENGIRIM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    status_konfirmasi = models.IntegerField(db_column='STATUS_KONFIRMASI')  # Field name made lowercase.
    total_pembelian = models.DecimalField(db_column='TOTAL_PEMBELIAN', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaksi'

    def __str__(self):
        return self.kode_transaksi
