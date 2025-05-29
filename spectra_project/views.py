from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.shortcuts import redirect
from .models import Category,Subcategory,Doctor,Medical,Product,Doctorwisesales,Medicalwisesales
from django.contrib.auth import logout


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    


def category(request):
    print(request)
    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
        return redirect('category')
    
    category = Category.objects.all()
    context= {"category" : category}
    
    return render(request,"category.html", context)

def category_delete(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    return redirect("category")

def category_edit(request, id):  
    category=Category.objects.get(id=id)
    return render(request, 'edit.html', {'category': category})

def category_update(request, id):    
    category = Category.objects.get(id=id)  
    if request.method=="POST":
        name = request.POST.get("name")
        category.name = name
        category.save()
        print('success')
        return redirect('category')
    return render(request,"edit.html")
          

# View to render the form
def subcategory(request):
     print(request)
     if request.method == "POST":
        # print(request.POST.get("subcategory"),)
        subcategory = request.POST.get("subcategory")
        id = request.POST.get("category")
        category=Category.objects.get(id=id)
        Subcategory.objects.create(subcategory=subcategory,category=category)
        return redirect('subcategory')
        
    
     subcategory = Subcategory.objects.all()
     category=Category.objects.all()
     
     context= {"Subcategory" : subcategory,"category" : category}
    
     return render(request,"subcategory.html", context)
 
def subcategory_delete(request,id):
    subcategory=Subcategory.objects.get(id=id)
    subcategory.delete()
    return redirect("/subcategory")

def subcategory_edit(request, id):  
    subcategory =Subcategory.objects.get(id=id)
    category = Category.objects.all()
    context = {"category":category,'subcategory': subcategory}
    return render(request, 'editsub.html',context)


def subcategory_update(request, id):    
    subcategory = Subcategory.objects.get(id=id)  
    print(subcategory)
   
    if request.method=="POST":
        category_id = request.POST.get("category")
        category=Category.objects.get(id=category_id)
        subcategory_id= request.POST.get("subcategory")

        subcategory.category = category
        subcategory.subcategory = subcategory_id
        subcategory.save()
        print('success')
        return redirect('subcategory')
    return render(request,"editsub.html")
          
         
def dashboard(request):
    category=Category.objects.count()
    subcategory_id=Subcategory.objects.count()
    return render(request,"dashboard.html",{'cat':category,'subcategory':subcategory_id})
    
def doctor(request):
    print(request)
    if request.method == "POST":
        doctorname = request.POST.get("doctorname")
        registernumber = request.POST.get("regno")
        gstnumber = request.POST.get("gstno")
        phonenumber = request.POST.get("phoneno")
        gmailid = request.POST.get("gmail")
        address = request.POST.get("address")
        
        Doctor.objects.create(doctorname=doctorname,regno=registernumber,gstno=gstnumber,phoneno=phonenumber,gmail=gmailid,address=address)
        
    return render(request,"doctor.html")

def doctorlist(request):
    doctor = Doctor.objects.all()
    context = {"doctor": doctor}
    return render(request,"doctorlist.html",context)

def doctor_delete(request,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect("/doctorlist")

def doctor_edit(request, id):  
    doctor = Doctor.objects.get(id=id)
    context = {"doctor":doctor}
    return render(request, 'doctoredit.html',context)

def doctor_update(request, id):    
    doctor = Doctor.objects.get(id=id)  
    print(doctor)
   
    if request.method=="POST":
        doctorname_id = request.POST.get("doctorname")
        regno_id = request.POST.get("regno")
        gstno_id = request.POST.get("gstno")
        phoneno_id = request.POST.get("phoneno")
        gmailid_id = request.POST.get("gmail")
        address_id = request.POST.get("address")
        
        doctor.doctorname = doctorname_id
        doctor.regno = regno_id
        doctor.gstno = gstno_id
        doctor.phoneno = phoneno_id
        doctor.gmail = gmailid_id
        doctor.address = address_id
        doctor.save()
        return redirect("doctorlist")
    return render(request,"doctoredit.html")

def doctorwisesales(request):
    doctor = Doctor.objects.all()
    product = Product.objects.all()
    context = {"doctor": doctor,"product":product}
    
    
    print(request.POST)
    if request.method == "POST":
        doc_id = request.POST.get("doctorname")
        doctorname = Doctor.objects.get(id=doc_id)
        prod_id = request.POST.get("productname")
        productname = Product.objects.get(id = prod_id)
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        Doctorwisesales.objects.create(doctorname=doctorname,productname=productname,quantity=quantity,price=price)
        return redirect("doctorwisesaleslist")
    return render(request,"doctorwisesales.html",context)
        

def doctorwisesaleslist(request):
    doctorwisesales = Doctorwisesales.objects.all()
    context = {"doctorwisesales":doctorwisesales}
    return render(request,"doctorwisesaleslist.html",context)


def doctorwisesales_delete(request,id):
    doctorsales=Doctorwisesales.objects.get(id=id)
    doctorsales.delete()
    return redirect("/doctorwisesaleslist")

def doctorwisesales_edit(request,id):
    doctorname = Doctor.objects.all()
    productname = Product.objects.all()
    doctor = Doctorwisesales.objects.get(id=id)
    context = {"doctorname":doctorname,"productname":productname,"doctorwisesales":doctor}
    return render(request,"doctorwiseedit.html",context)

def doctorwisesales_update(request,id):
    doctor= Doctorwisesales.objects.get(id=id)
    print(doctor)
    
    if request.method == "POST":
        doctorname = request.POST.get("doctorname")
        doctorname_id = Doctor.objects.get(id = doctorname)
        productname = request.POST.get("productname")
        productname_id = Product.objects.get(id=productname)
        quantity_id = request.POST.get("quantity")
        price_id = request.POST.get("price")
        
        doctor.doctorname = doctorname_id
        doctor.productname = productname_id
        doctor.quantity = quantity_id
        doctor.price = price_id
        doctor.save()
        return redirect("doctorwisesaleslist")
    return render(request,"doctorwiseedit.html")

    
def medical(request):
    if request.method=="POST":
        medname= request.POST.get("medicalname")
        gstnumber = request.POST.get("gstno")
        phonenumber = request.POST.get("phoneno")
        gmailid = request.POST.get("gmail")
        address = request.POST.get("address")
        Medical.objects.create(medicalname=medname,gstno=gstnumber,phoneno=phonenumber,gmail=gmailid,address=address)
        
    return render(request,"medical.html")

def medicallist(request):
    medical = Medical.objects.all()
    context = {"medical": medical}
    return render(request,"medicallist.html",context)

def medical_edit(request,id):
    medical = Medical.objects.get(id=id)
    context = {"medical":medical}
    return render(request,"medicaledit.html",context)

def medical_update(request,id):
    medical = Medical.objects.get(id=id)
    print(medical)
    
    if request.method == "POST":
        medicalname_id = request.POST.get("medicalname")
        gstno_id = request.POST.get("gstno")
        phoneno_id = request.POST.get("phoneno")
        emailid_id = request.POST.get("gmail")
        address_id = request.POST.get("address")
        
        medical.medicalname = medicalname_id
        medical.gstno = gstno_id
        medical.phoneno = phoneno_id
        medical.gmail = emailid_id
        medical.address = address_id
        medical.save()
        return redirect("medicallist")
    return render(request,"medicaledit.html")
        

def medical_delete(request,id):
    medical=Medical.objects.get(id=id)
    medical.delete()
    return redirect("/medicallist")

def medicalwisesales(request):
    medicalname = Medical.objects.all()
    productname = Product.objects.all()
    context = {"medical" : medicalname,"product":productname}
    
    print(request.POST)
    if request.method == "POST":
        med_id = request.POST.get("medicalname")
        medicalname = Medical.objects.get(id = med_id)
        prod_id = request.POST.get("productname")
        productname = Product.objects.get(id = prod_id)
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        Medicalwisesales.objects.create(medicalname=medicalname,productname=productname,quantity=quantity,price=price)
        return redirect("medicalwisesaleslist")
    return render(request,"medicalwisesales.html",context)

def medicalwisesaleslist(request):
    medicalwisesales = Medicalwisesales.objects.all()
    context = {"medicalwisesales":medicalwisesales}
    return render(request,"medicalwisesaleslist.html",context)

def medicalwisesales_delete(request,id):
    medicalwisesales=Medicalwisesales.objects.get(id=id)
    medicalwisesales.delete()
    return redirect("/medicalwisesaleslist")

def medicalwisesales_edit(request,id):
    medicalname = Medical.objects.all()
    productname = Product.objects.all()
    medical = Medicalwisesales.objects.get(id=id)
    context = {"medical":medicalname,"product":productname,"medicalwisesales":medical}
    return render(request,"medicalwiseedit.html",context)

def medicalwisesales_update(request,id):
    medical = Medicalwisesales.objects.get(id=id)
    print(medical)
    
    if request.method == "POST":
        med_name = request.POST.get("medicalname")
        medicalname = Medical.objects.get(id=med_name)
        prod_name = request.POST.get("productname")
        productname = Product.objects.get(id = prod_name)
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        
        medical.medicalname = medicalname
        medical.productname = productname
        medical.quantity = quantity
        medical.price = price
        medical.save()
        return redirect("medicalwisesaleslist")
    return render(request,"medicalwiseedit.html")


def product(request):
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context= {"category" : category,"subcategory":subcategory}
    
    print(request.POST)
    if request.method == "POST":
      
        cate_id = request.POST.get("category")
        print(cate_id)
        category = Category.objects.get(id=cate_id)
        sub_id = request.POST.get("subcategory")
        subcategory = Subcategory.objects.get(id=sub_id)
        productname = request.POST.get("productname")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        Product.objects.create(category=category,subcategory=subcategory,productname=productname,price=price,stock=stock)
        return redirect("productlist")
    return render(request,"product.html",context)


def productlist(request):
    product = Product.objects.all()
    
    context = {"product":product}
    
    return render(request,"productlist.html",context)

def product_delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect("/productlist")

def productlist_edit(request, id):  
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    productname = Product.objects.get(id=id)
    context = {"category":category,"subcategory": subcategory,"productname":productname}
    
    return render(request, 'prodedit.html',context)

def productlist_update(request,id):
    productname = Product.objects.get(id=id)
    print(productname)
    
    if request.method == "POST":
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id)
        subcategory_id = request.POST.get("subcategory")
        subcategory = Subcategory.objects.get(id=subcategory_id)
        product_name = request.POST.get("productname")
        price_id = request.POST.get("price")
        stock_id = request.POST.get("stock")
        
        productname.category = category
        productname.subcategory = subcategory
        productname.productname = product_name
        productname.price = price_id
        productname.stock = stock_id
        productname.save()
        return redirect('productlist')
    return render(request,"prodedit.html")

def nav(request):
    return render(request,"nav.html")

def cat(request):
    return render(request,"cat.html")

def sub(request):
    category= Category.objects.all() 
    context = {
        'category': category 
    }
    return render(request, "sub.html",context)

def logout_view(request):
    logout(request)
    return redirect('login')


