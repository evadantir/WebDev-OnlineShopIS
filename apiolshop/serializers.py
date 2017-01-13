from .models import *
from rest_framework import serializers

class BarangSerializer(serializers.ModelSerializer):
    kode_tipe = serializers.PrimaryKeyRelatedField(queryset=TipeBarang.objects.all())
    detail_barang = serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model = Barang
        fields = '__all__'

class BarangPesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangPesanan
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'

class TipeBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipeBarang
        fields = '__all__'

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = '__all__'

class KotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = '__all__'

class DetailBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailBarang
        fields = '__all__'

class DaftarAlamatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaftarAlamat
        fields = '__all__'
