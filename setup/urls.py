from django.contrib import admin
from django.urls import path,include
from escola.views import EstudanteViewSet,CursoViewSet,MatriculaViewSet,ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

# definindo as rotas
#Metodo HTTP
router = routers.DefaultRouter()
router.register('estudantes',EstudanteViewSet, basename = 'Estudantes')
router.register('cursos',CursoViewSet, basename = 'Cursos')
router.register('matriculas',MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudante/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('estudante/<int:pk>/Curso/',ListaMatriculaCurso.as_view())
]
