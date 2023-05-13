from django.core.management.base import BaseCommand
from manufactory.models import SubAssembly

class Command(BaseCommand):
    help = 'Checks the dates of subassemblies'

    def handle(self, *args, **options):
        subassemblies = SubAssembly.objects.all()

        for subassembly in subassemblies:
            # Perform your desired logic here
            # For example, you can compare dates and update a flag on the subassembly
            fabrication_out_date = subassembly.fabrication.out_date
            subassembly_start_date = subassembly.start_date

            if subassembly_start_date >= fabrication_out_date or subassembly.fabrication.redundent:
                subassembly.redundent = True
                subassembly.save()

        self.stdout.write(self.style.SUCCESS('SubAssembly dates checked successfully.'))
