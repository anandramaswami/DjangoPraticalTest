from django.db import models

# Create your models here.

class StudentsDataModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    class_name = models.CharField(max_length=10)
    roll_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
    
    def total_students(self):
        return self.student_id


class FeeCategoriesModel(models.Model):
    category_id = models.AutoField(primary_key=True)
    fee_name = models.CharField(max_length=25)
    fee_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.fee_name


class StudentFeesModel(models.Model):
    student = models.ForeignKey(StudentsDataModel,on_delete=models.CASCADE)
    fee_category = models.ForeignKey(FeeCategoriesModel,on_delete=models.CASCADE)
    status = models.CharField(max_length=5)
    due_date = models.DateField()
    paid_date = models.DateField()
    amount_paid = models.IntegerField()
    

    def __str__(self):
        return f'{self.student.first_name} {self.student.second_name} {self.fee_category.fee_name}'
    
    def remaining_amount(self):
        return self.fee_category.amount - self.amount_paid