from django.db import models

# TODO we can add plant_name and plane_code to expand it to multiple plants and there own multiple users

class Fabrication(models.Model):
    item_id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=255)
    raw_material = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    in_date = models.DateField(auto_now_add=True)
    out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.item


class SubAssembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    fibrication=models.ForeignKey(Fabrication, verbose_name="Related Fabrication", null=True, on_delete=models.CASCADE)
    process = models.CharField(max_length=255)   # consider adding this to foregin key and make model
    # item_id = models.CharField(max_length=50)   # change this to Foregin key after discussion
    machine_id = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.process
    def get_item_id(self):
        if self.fibrication is not None:
            return self.fibrication.item
        return None


# class Study(models.Model):

#     class Meta:
#         unique_together = (('class_id', 'student_id'),)

#     class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='classes')
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')

#     def str(self):
#         return f"{self.class_id} #### {self.student_id}" 




class Assembly(models.Model):
    machine_id = models.AutoField(primary_key=True)   
    subassembly = models.ForeignKey(SubAssembly, verbose_name="Reverse SubAssembly",on_delete=models.CASCADE, null=True)   # consider this as Foregin key
    process = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.process

    def get_process_id(self):
        if self.subassembly is not None:
            return self.subassembly.assembly_id + self.subassembly.machine_id
        return None


