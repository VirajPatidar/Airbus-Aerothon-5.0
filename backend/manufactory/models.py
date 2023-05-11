from django.db import models

# TODO we can add plant_name and plane_code to expand it to multiple plants and there own multiple users

class Fabrication(models.Model):
    item_id = models.AutoField(primary_key=True)
    # subassembly=model.models.ForeignKey("SubAssembly", verbose_name=_("Related SubAssembly"), on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    raw_material = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    in_date = models.DateField(auto_now_add=True)
    out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.item


class SubAssembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    process = models.CharField(max_length=255)   # consider adding this to foregin key and make model
    item_id = models.CharField(max_length=50)   # change this to Foregin key after discussion
    machine_id = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.assembly_id


class Assembly(models.Model):
    process_id = models.AutoField(primary_key=True)
    process = models.CharField(max_length=255)
    machine_id = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.process

