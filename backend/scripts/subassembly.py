# to populate on cmd
# python manage.py shell > scripts/populate_fabrication.py

process_assembly = [
    "Component Integration",
    "Electrical Testing",
    "Complaince",
    "Certification Standards",
    "pivot dome",
    "brake assembly",
    "module",
    "Powder Coating Process",
    "Testing and Inspection",
]

process_subassembly = [
    "Electrical Assembly",
    "Mechanical assembly",
    "Spot Weld Assembly",
    "Transmission Assembly",
    "Tub assemblies",
    "Weld Assembly",
]

items = [
    "tub",
    "pump",
    "spin tub",
    "wash tub",
    "balance ring",
    "transmission gears",
    "plastic brackets",
]
raw_materials = [
    "Sheet steel",
    "Plastics",
    "Stainless steel",
    "(Enameling iron) Porcelain coating",
    "Cast aluminum",
    "Porcelain enamel" "Plastics",
]
quantity = ["10 sqft", "10 kg", "5 kg/m3", "24 gauge", "3 kg ", "ingots—20", "2 kg"]

from manufactory.models import Assembly, SubAssembly, Fabrication, Machine
import random

# for item, raw_material, quant in zip(items, raw_materials, quantity):
#     Fabrication.objects.create(item=item, raw_material=raw_material, quantity=quant)

machines = Machine.objects.all()
total_machin_count=machines.count()-1
fabicrations = Fabrication.objects.all()
for i in range(len(process_subassembly)):

    _ = SubAssembly.objects.create(
        process=process_subassembly[i],
        machine=machines[i],
        fabrication=fabicrations[i],
    )
    Assembly.objects.create(
        process=process_assembly[random.randint(0, len(process_assembly) - 1)],
        subassembly=_,
        machine=machines[total_machin_count-i],
    )

# to populate Assembly
