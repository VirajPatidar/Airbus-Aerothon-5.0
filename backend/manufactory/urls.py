from django.urls import path
from .views import (
    AssemblyDataView,
    SubAssemblyDataView,
    FabricationDataView,
    ApprovedDataView,
    MachineListView,
)

urlpatterns = [
    path("fabrication/", FabricationDataView.as_view(), name="Fabrication-data"),
    path("subassembly/", SubAssemblyDataView.as_view(), name="SubAssembly-data"),
    path("assembly/", AssemblyDataView.as_view(), name="Assembly-data"),
    path("approved", ApprovedDataView.as_view(), name="Approved-data"),
    path("machine", MachineListView.as_view(), name="Machine-data"),
]
