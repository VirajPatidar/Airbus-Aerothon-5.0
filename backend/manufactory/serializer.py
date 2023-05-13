from rest_framework import serializers
from .models import Fabrication, SubAssembly, Assembly, Machine


## TODO improve as required


class FabricationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabrication
        fields = "__all__"
        # fields = ("item_id", "item", "raw_material", "quantity", "in_date", "out_date")


class SubAssemblySerializer(serializers.ModelSerializer):
    item_id = serializers.CharField(source="get_item_id", read_only=True)
    machine_id = serializers.CharField(source="get_machine_id", read_only=True)

    class Meta:
        model = SubAssembly
        fields = "__all__"
        # fields = ['assembly_id', 'fabrication', 'item_id', 'process', 'machine_id', 'start_date', 'end_date']


class AssemblySerializer(serializers.ModelSerializer):
    subassembly_id = serializers.CharField(source="get_process_id", read_only=True)
    machine_id = serializers.CharField(source="get_machine_id", read_only=True)

    class Meta:
        model = Assembly
        fields = [
            "machine_id",
            "subassembly",
            "subassembly_id",
            "process",
            "start_date",
            "end_date",
        ]


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"
