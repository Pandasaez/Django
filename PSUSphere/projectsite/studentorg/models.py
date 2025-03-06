from django.db import models

# Create your models here.
class BaseModel (model.Model):
    created_at = model.DateTimeField(auto_now_add=True, db_indext=True)
    upadted_at = = model.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModel):
    collage_name = model.Charfield(max_length=150)

    def_str_(self):
        return self.college_name

class Program(Basemodel):
    prog_name = model.Charfield(max_length=150)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def_str_(self):
        return self.prog_name

