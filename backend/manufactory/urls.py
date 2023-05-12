from django.urls import path
from .views import AssemblyDataView, SubAssemblyDataView, FabricationDataView

urlpatterns = [
    path('fabrication/', FabricationDataView.as_view(), name='Fabrication-data'),
    path('subAssembly/', SubAssemblyDataView.as_view(), name='SubAssembly-data'),
    path('assembly/', AssemblyDataView.as_view(), name='assembly-data'),
]