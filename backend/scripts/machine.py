from manufactory.models import Assembly, SubAssembly, Fabrication, Machine
import random

machine_parts = [
    ('MC001', 'Agitator', 'Agitator for washing machine', 'AG123', 'Washing Machine Part'),
    ('MC002', 'Bearing', 'Bearing for washing machine drum', 'BR456', 'Washing Machine Part'),
    ('MC003', 'Belt', 'Belt for washing machine motor', 'BL789', 'Washing Machine Part'),
    ('MC004', 'Control Board', 'Control board for washing machine', 'CB321', 'Washing Machine Part'),
    ('MC005', 'Door Lock', 'Door lock mechanism for washing machine', 'DL654', 'Washing Machine Part'),
    ('MC006', 'Drain Pump', 'Drain pump for washing machine', 'DP987', 'Washing Machine Part'),
    ('MC007', 'Drive Belt', 'Drive belt for washing machine', 'DB234', 'Washing Machine Part'),
    ('MC008', 'Drum', 'Drum for washing machine', 'DR567', 'Washing Machine Part'),
    ('MC009', 'Gasket', 'Gasket for washing machine door', 'GS890', 'Washing Machine Part'),
    ('MC010', 'Hose', 'Hose for washing machine water inlet', 'HS123', 'Washing Machine Part'),
]

random_parts = random.sample(machine_parts, k=5)  # Generate a list of 5 random machine parts

print(random_parts)



def generate_machine_code():
    random_number = random.randint(100, 999)  # Generate a random three-digit number
    return f"WM{random_number}"

def generate_machine_name():
    adjectives = ['Smart', 'Eco', 'Advanced', 'High-Performance', 'Efficient']
    nouns = ['Washer', 'Laundry Machine', 'Washing Appliance', 'Washing Unit']
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

def generate_machine_description():
    descriptions = ['Powerful washing machine with multiple features.',
                    'Energy-efficient and environmentally friendly washer.',
                    'Advanced technology for superior cleaning results.',
                    'Spacious drum capacity for large loads.',
                    'User-friendly controls and intuitive interface.']
    return random.choice(descriptions)

def generate_machine_model_number():
    random_number = random.randint(1000, 9999)  # Generate a random four-digit number
    return f"WM-{random_number}"

def generate_machine_type():
    types = ['Front Load', 'Top Load', 'Compact', 'Portable']
    return random.choice(types)

washing_machines = []

for _ in range(10):
    machine_code = generate_machine_code()
    machine_name = generate_machine_name()
    machine_description = generate_machine_description()
    machine_model_number = generate_machine_model_number()
    machine_type = generate_machine_type()
    washing_machine = (machine_code, machine_name, machine_description, machine_model_number, machine_type);washing_machines.append(washing_machine)

print(washing_machines)


# for machine_code, name, description, model_number, machine_type in machine_parts:
#     Machine.objects.create(machine_code=machine_code, name=name, description=description, model_number=model_number, machine_type=machine_type)


for machine_code, name, description, model_number, machine_type in washing_machines:
    Machine.objects.create(machine_code=machine_code, name=name, description=description, model_number=model_number, machine_type=machine_type)




