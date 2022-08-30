from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from . import views

urlpatterns = [
    # ex: /alumnos/
    path('', views.index, name='index'),
    # ex: /alumnos/5/
    path('<int:alumno_id>/', views.detail, name='detail'),
    # ex: /alumnos/5/results/
    path('<int:alumno_id>/results/', views.results, name='results'),
    # ex: /alumnos/5/vote/
    path('<int:alumno_id>/vote/', views.vote, name='vote')
]