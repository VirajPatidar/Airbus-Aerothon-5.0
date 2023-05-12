from rest_framework import serializers
from .models import Fabrication, SubAssembly, Assembly


## TODO improve as required


class FabricationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabrication
        fields = ("item_id", "item", "raw_material", "quantity", "in_date", "out_date")


class SubAssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAssembly
        fields = (
            "assembly_id",
            "process",
            "item_id",
            "machine_id",
            "start_date",
            "end_date",
        )


class AssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = Assembly
        fields = ("process_id", "process", "machine_id", "start_date", "end_date")
