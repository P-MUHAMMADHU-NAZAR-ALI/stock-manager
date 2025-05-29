from django.db import models

class Login(models.Model):
  username = models.CharField(max_length=255,blank=False,null=False)
  password = models.CharField(max_length=255,blank=False,null=False)
  

class Category(models.Model):
  name = models.CharField(max_length=255,blank=False,null=False)
  
class Subcategory(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  subcategory = models.CharField(max_length=255,blank=False,null=False)
  
class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
  productname = models.CharField(max_length=255,blank=False,null=False)
  price = models.IntegerField()
  stock = models.IntegerField()
  
class Doctor(models.Model):
  doctorname = models.CharField(max_length=255,blank=False,null=False)
  regno = models.IntegerField()
  gstno = models.CharField(max_length=255,blank=False,null=False)
  phoneno = models.IntegerField()
  gmail = models.CharField(max_length=255,blank=False,null=False)
  address = models.CharField(max_length=255,blank=False,null=False)
  
class Doctorwisesales(models.Model):
  doctorname = models.ForeignKey(Doctor,on_delete=models.CASCADE)
  productname = models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity = models.IntegerField()
  price=models.IntegerField()
  
  
class Medical(models.Model):
  medicalname =models.CharField(max_length=255,blank=False,null=False)
  gstno = models.CharField(max_length=255,blank=False,null=False)
  phoneno = models.IntegerField()
  gmail = models.CharField(max_length=255,blank=False,null=False)
  address = models.CharField(max_length=255,blank=False,null=False)
  
class Medicalwisesales(models.Model):
  medicalname = models.ForeignKey(Medical,on_delete=models.CASCADE)
  productname = models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity = models.IntegerField()
  price=models.IntegerField()
  
  
  
  
  