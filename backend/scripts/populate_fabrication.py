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

from manufactory.models import Assembly, SubAssembly, Fabrication
import random

for item, raw_material, quant in zip(items, raw_materials, quantity):
    Fabrication.objects.create(item=item, raw_material=raw_material, quantity=quant)


# for process in process_subassembly:

#     SubAssembly.objects.create(
#         process=process,
#         machine_id=random.randint(1, 10),
#         fabrication_id=random.randint(1, 10),
#     )
