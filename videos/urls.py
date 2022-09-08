from django.urls import path

from videos.views import Curso

urlpatterns = [

    path('curso/', Curso.as_view(), name="curso"),

]