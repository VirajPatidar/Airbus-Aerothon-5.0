from django.utils import timezone
from .models import SubAssembly, Fabrication

from django.http import HttpResponse

def check_sucdbassembly_dates(request):
    subassemblies = SubAssembly.objects.all()

    for subassembly in subassemblies:
        fabrication_out_date = subassembly.fabrication.out_date
        subassembly_start_date = subassembly.start_date

        if subassembly_start_date >= fabrication_out_date or subassembly.fabrication.redundent is True:
            # Perform your desired logic here
            # For example, you can send an email notification or update a flag on the subassembly
            subassembly.redundent = True

    return HttpResponse("SubAssembly dates checked successfully.")

def check_assembly_dates(request):
    subassemblies = Assembly.objects.all()

    for assembly in subassemblies:
        subassembly_out_date = assembly.subassembly.end_date
        assembly_start_date = assembly.start_date

        if assembly_start_date >= subassembly_out_date or assembly.subassembly.redundent is True:
            # Perform your desired logic here
            # For example, you can send an email notification or update a flag on the assembly
            assembly.redundent = True

    return HttpResponse("SubAssembly dates checked successfully.")

def remove_redundant_entries_cron_job(request):

    SubAssembly.objects.filter(redundent=True).delete()
    Fabrication.objects.filter(redundent=True).delete()
    Assembly.objects.filter(redundent=True).delete()

    return HttpResponse("Redundant entries removed successfully.")