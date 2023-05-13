from django.db import models
from datetime import date

# TODO we can add plant_name and plane_code to expand it to multiple plants and there own multiple users


class ItemModel(models.Model):
    item = models.CharField(max_length=255)
    raw_material = models.CharField(max_length=255)


class Fabrication(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_material = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    in_date = models.DateField(default=date.today)
    out_date = models.DateField(null=True, blank=True)
    redundent = models.BooleanField(default=False)
    is_available = models.BooleanField(
        default=True, help_text="Is available for use by Sub-Assembly"
    )
    stamped = models.BooleanField(
        default=False, help_text="Is available for use by Sub-Assembly"
    )

    class Meta:
        unique_together = ["item_material", "quantity", "in_date", "out_date"]

    def __str__(self):
        return self.item


class Machine(models.Model):
    machine_code = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    model_number = models.CharField(max_length=50, null=True, blank=True)
    machine_type = models.CharField(max_length=50, null=True, blank=True)

class Process(models.Model):
    process_id = models.AutoField(primary_key=True)
    process_name = models.CharField(max_length=255)
    process_description = models.TextField(null=True, blank=True)
    process_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.process_name

class SubAssembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    fabrication = models.ForeignKey(
        Fabrication,
        verbose_name="Related Fabrication",
        null=True,
        on_delete=models.CASCADE,
    )
    process = models.models.ForeignKey(Process, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True, blank=True)

    # Fields used by Assembly Model to create entry
    redundent = models.BooleanField(default=False)
    is_available = models.BooleanField(
        default=True, help_text="Is available for use by ssembly"
    )

    class Meta:
        unique_together = [
            "fabrication",
            "process",
            "machine",
            "start_date",
            "end_date",
        ]

    def __str__(self):
        return self.process

    def get_item_id(self):
        if self.fabrication is not None:
            return self.fabrication.item
        return None

    def get_machine_id(self):
        if self.machine is not None:
            return self.machine.machine_code
        return None





class Assembly(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    subassembly = models.ForeignKey(
        SubAssembly,
        verbose_name="Reverse SubAssembly",
        on_delete=models.CASCADE,
        null=True,
    )  # consider this as Foregin key
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=date.today)
    end_date = models.DateTimeField(null=True, blank=True)
    redundent = models.BooleanField(default=False)

    class Meta:
        unique_together = [
            "machine",
            "subassembly",
            "process",
            "start_date",
            "end_date",
        ]

    def __str__(self):
        return self.process

    def get_process_id(self):
        if self.subassembly is not None:
            return (
                "SAW"
                + str(self.subassembly.assembly_id)
                + self.subassembly.get_machine_id()
            )
        return None

    def get_machine_id(self):
        if self.machine is not None:
            return self.machine.machine_code
        return None
