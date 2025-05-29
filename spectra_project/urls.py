from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('category/', views.category, name='category'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctorlist/', views.doctorlist, name='doctorlist'),
    path('doctorwisesales/', views.doctorwisesales, name='doctorwisesales'),
    path('doctorwisesaleslist/', views.doctorwisesaleslist, name='doctorwisesaleslist'),
    path('medical/', views.medical, name='medical'),
    path('medicallist/', views.medicallist, name='medicallist'),
    path('medicalwisesales/', views.medicalwisesales, name='medicalwisesales'),
    path('medicalwisesaleslist/', views.medicalwisesaleslist, name='medicalwisesaleslist'),
    path('product/', views.product, name='product'),
    path('productlist/', views.productlist, name='productlist'),                                                 
    path('nav/', views.nav, name='nav'),
    path('cat/',views.cat,name='cat'),
    path('sub/',views.sub,name='sub'),
    path('delete/<int:id>',views.category_delete),
    path('subdelete/<int:id>',views.subcategory_delete),
    path('proddelete/<int:id>',views.product_delete),
    path('Doctordelete/<int:id>',views.doctor_delete),
    path('medicaldelete/<int:id>',views.medical_delete),
    path('doctorwisesalesdelete/<int:id>',views.doctorwisesales_delete),
    path('medicalwisesalesdelete/<int:id>',views.medicalwisesales_delete),
    path('category_edit/<int:id>/', views.category_edit),
    path('category_update/<int:id>/', views.category_update),
    path('subcategory_edit/<int:id>/', views.subcategory_edit),
    path('subcategory_update/<int:id>/', views.subcategory_update),
    path('prod_edit/<int:id>/', views.productlist_edit),
    path('prod_update/<int:id>/', views.productlist_update),
    path('doctor_edit/<int:id>/', views.doctor_edit),
    path('doctor_update/<int:id>/', views.doctor_update),
    path('medical_edit/<int:id>/', views.medical_edit),
    path('medical_update/<int:id>/', views.medical_update),
    path('doctorwisesales_edit/<int:id>/', views.doctorwisesales_edit),
    path('doctorwisesales_update/<int:id>/', views.doctorwisesales_update),
    path('medicalwisesales_edit/<int:id>/', views.medicalwisesales_edit),
    path('medicalwisesales_update/<int:id>/', views.medicalwisesales_update),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
]