# to>>> ulate on cmd
# python manage.py shell > scripts/assembly.py
from manufactory.models import Assembly, SubAssembly, Fabrication,ItemModel
import random

from datetime import datetime, timedelta
import random

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
key=[]
for item,m in zip(items,raw_materials):
    a=ItemModel.objects.create(item=item, raw_material=m)
    key.append(a)


quantity = ["10 sqft", "10 kg", "5 kg/m3", "24 gauge", "3 kg ", "ingots—20", "2 kg"]



# Define the start date and interval range
start_date = datetime.now().date()
min_interval = timedelta(days=1)
max_interval = timedelta(days=7)

# Generate a list of 7 random in_date and out_date pairs
date_pairs = []
for i in range(7):
    interval = timedelta(days=random.randint(min_interval.days, max_interval.days))
    in_date = start_date + timedelta(days=i)
    out_date = in_date + interval
    date_pairs.append((in_date, out_date))

# # Print the date pairs
# for in_date, out_date in date_pairs:
#     print(f"In Date: {in_date}, Out Date: {out_date}")

print(date_pairs)
i=0
for item, raw_material, quant in zip(items, raw_materials, quantity):
    try:
        a=Fabrication.objects.create(item_material=key[i], quantity=quant, in_date=date_pairs[i][0], out_date=date_pairs[i][1])
        print(a.in_date)
        i+=1
    except Exception as e:
        print(e)

# for process in process_subassembly:

#     SubAssembly.objects.create(
#         process=process,
#         machine_id=random.randint(1, 10),
#         fabrication_id=random.randint(1, 10),
#     )
