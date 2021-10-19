from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .serializers import BillsSerializers


class BillsViewSet(viewsets.ModelViewSet):
    serializer_class = BillsSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        bills_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(bills_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Venta creada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            bills_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if bills_serializer.is_valid():
                bills_serializer.save()
                return Response(bills_serializer.data, status=status.HTTP_200_OK)
            return Response(bills_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk=None):
        bills = self.get_queryset().filter(id=pk)
        if bills:
            bills.delete()
            return Response({'message':'Venta eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe una Venta con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)