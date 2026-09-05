from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

class EstudanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BaseAuthentication]
    permission_classes =[IsAuthenticated]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BaseAuthentication]
    permission_classes =[IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BaseAuthentication]
    permission_classes =[IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    authentication_classes = [BaseAuthentication]
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    authentication_classes = [BaseAuthentication]
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
           queryset = Matricula.objects.filter(Curso_id=self.kwargs['pk'])
           return queryset
    serializer_class = ListaMatriculasCursoSerializer