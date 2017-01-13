from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.
class BarangViewSet(viewsets.ModelViewSet):
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer

    #edited module from @triayudapurnama
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Barang.objects.all()
        tipeBarang = self.request.query_params.get('kode_tipe',None)
        if tipeBarang is not None:
            queryset = queryset.filter(kode_tipe=tipeBarang)
        kodeBarang = self.request.query_params.get('kode_barang',None)
        if kodeBarang is not None:
            queryset = queryset.filter(kode_barang=kodeBarang)
        return queryset

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
