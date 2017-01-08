from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.
class BarangViewSet(viewsets.ModelViewSet):
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer

class BarangPesananViewSet(viewsets.ModelViewSet):
    queryset = BarangPesanan.objects.all()
    serializer_class = BarangPesananSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer

class TipeBarangViewSet(viewsets.ModelViewSet):
    queryset = TipeBarang.objects.all()
    serializer_class = TipeBarangSerializer

class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer

class KotaViewSet(viewsets.ModelViewSet):
    queryset = Kota.objects.all()
    serializer_class = KotaSerializer

class DetailBarangViewSet(viewsets.ModelViewSet):
    queryset = DetailBarang.objects.all()
    serializer_class = DetailBarangSerializer

class DaftarAlamatViewSet(viewsets.ModelViewSet):
    queryset = DaftarAlamat.objects.all()
    serializer_class = DaftarAlamatSerializer
