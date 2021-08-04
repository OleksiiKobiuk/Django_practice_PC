#Создаем модель Computer

# поля:
# - бренд
# - модель
# - объем оперативной памяти
# - частота процессора
# - монитор (дюймы)
#
# реализовать все CRUD операции
# добаваить валидацию

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializer import ComputerSerializer
from .models import ComputerModel

class CreateRetriaveAll(APIView):
    def get(self, *args, **kwargs):
        qs = ComputerModel.objects.all()
        serializer = ComputerSerializer(qs, many=True).data
        return Response(serializer, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        body = self.request.data
        serializer = ComputerSerializer(data=body)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

class GetOneUpdDelete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data=ComputerModel.objects.get(pk=pk)
        except Exception as e:
            return Response(f'No data with id {pk}')
        serializer = ComputerSerializer(data).data
        return Response(serializer)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(ComputerModel, pk=pk)
        # try:
        #     data = ComputerModel.objects.get(pk=pk)
        # except Exception as e:
        #     return Response(f'No data with id {pk}')
        serializer = ComputerSerializer(instance, self.request.data,
                                        partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(ComputerModel, pk=pk)
        instance.delete()
        return Response(f'data with id {pk} is deleted')





