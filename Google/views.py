from rest_framework.generics import GenericAPIView
from .serializers import GoogleIniciarSesionSerializer
from rest_framework.response import Response
from rest_framework import status


class GoogleIniciarSesionView(GenericAPIView):
    serializer_class = GoogleIniciarSesionSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response(data, status=status.HTTP_200_OK)
