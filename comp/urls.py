from django.urls import path

from .views import CreateRetriaveAll, GetOneUpdDelete

urlpatterns = [
    path('', CreateRetriaveAll.as_view(), name='comp_list_create'),
    path('<int:pk>/', GetOneUpdDelete.as_view(), name='comp_update_getById_delete'),

]