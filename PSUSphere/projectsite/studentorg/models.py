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

class Organization (BaseModel):
    name = models.CharField(max_length=250)
    college = models. ForeignKey(
        College, null=True, blank-True, on_delete models.CASCADE)
    description = models.CharField(max_length=500)

    def_str_(self):
        return self.name

class Student(BaseModel):
    student_id= models. CharField(max_length=15)
    lastname models.CharField(max_length=25)
    firstname models.CharField(max_length=25)
    middlename models.CharField(max_length=25, blank True, null-True)
    program models.ForeignKey (Program, on_delete models.CASCADE)

    def_str_(self):
        return f"(self.lastname), (self.firstname)"

class OrgMember(BaseModel):
    student = models. ForeignKey (Student, on delete models.CASCADE)
    organization = models. ForeignKey(Organization, on_delete models.CASCADE)
    data_joined = models. DateField()