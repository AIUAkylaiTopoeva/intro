from django.urls import path
from .views import get_sapros, get_sap, post_chela, izmena, delete_chel

urlpatterns = [
    path('vse_ludi/', get_sapros),
    path('chelovek/<int:pk>/', get_sap),
    path('chel/', post_chela),
    path('izmena/<int:pk>/', izmena),
    path('kill/<int:pk>/', delete_chel)
]