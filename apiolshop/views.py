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

class DetailBarangViewSet(viewsets.ModelViewSet):
    queryset = DetailBarang.objects.all()
    serializer_class = DetailBarangSerializer

class DaftarAlamatViewSet(viewsets.ModelViewSet):
    queryset = DaftarAlamat.objects.all()
    serializer_class = DaftarAlamatSerializer

class KotaViewSet(viewsets.ModelViewSet):
    queryset = Kota.objects.all()
    serializer_class = KotaSerializer

class LoginViewSet(APIView):
    def get(self,request,format=None):
        queryset = Customer.objects.all()
        email = self.request.query_params.get('email',None)
        password = self.request.query_params.get('password',None)
        queryset = Customer.objects.filter(email = email).filter(password = password)
		#queryset = Pelanggan.objects.filter(password = field_pass) kalo OR
		#serializer_class = LoginSerializer()
		#return Response({'received data': request.data}, status=status.HTTP_201_CREATED)
        c = queryset.count()
        if c > 0:
            return HttpResponse(serializer_class.serialize(queryset))
        else:
            return Response({'username dan password salah'})
		#return Response({'username': username})

class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer

class TipeBarangViewSet(viewsets.ModelViewSet):
    queryset = TipeBarang.objects.all()
    serializer_class = TipeBarangSerializer

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
