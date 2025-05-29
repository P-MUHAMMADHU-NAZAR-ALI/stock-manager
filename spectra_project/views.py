from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Category, Subcategory, Doctor, Medical, Product, Doctorwisesales, Medicalwisesales


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


@login_required
def category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
        return redirect('category')

    category = Category.objects.all()
    context = {"category": category}
    return render(request, "category.html", context)


@login_required
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("category")


@login_required
def category_edit(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'edit.html', {'category': category})


@login_required
def category_update(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        category.name = name
        category.save()
        return redirect('category')
    return render(request, "edit.html")


@login_required
def subcategory(request):
    if request.method == "POST":
        subcategory = request.POST.get("subcategory")
        id = request.POST.get("category")
        category = Category.objects.get(id=id)
        Subcategory.objects.create(subcategory=subcategory, category=category)
        return redirect('subcategory')

    subcategory = Subcategory.objects.all()
    category = Category.objects.all()
    context = {"Subcategory": subcategory, "category": category}
    return render(request, "subcategory.html", context)


@login_required
def subcategory_delete(request, id):
    subcategory = Subcategory.objects.get(id=id)
    subcategory.delete()
    return redirect("subcategory")


@login_required
def subcategory_edit(request, id):
    subcategory = Subcategory.objects.get(id=id)
    category = Category.objects.all()
    context = {"category": category, 'subcategory': subcategory}
    return render(request, 'editsub.html', context)


@login_required
def subcategory_update(request, id):
    subcategory = Subcategory.objects.get(id=id)
    if request.method == "POST":
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id)
        subcategory_name = request.POST.get("subcategory")
        subcategory.category = category
        subcategory.subcategory = subcategory_name
        subcategory.save()
        return redirect('subcategory')
    return render(request, "editsub.html")


@login_required
def dashboard(request):
    category = Category.objects.count()
    subcategory_id = Subcategory.objects.count()
    return render(request, "dashboard.html", {'cat': category, 'subcategory': subcategory_id})


@login_required
def doctor(request):
    if request.method == "POST":
        doctorname = request.POST.get("doctorname")
        registernumber = request.POST.get("regno")
        gstnumber = request.POST.get("gstno")
        phonenumber = request.POST.get("phoneno")
        gmailid = request.POST.get("gmail")
        address = request.POST.get("address")
        Doctor.objects.create(
            doctorname=doctorname, regno=registernumber, gstno=gstnumber,
            phoneno=phonenumber, gmail=gmailid, address=address)
    return render(request, "doctor.html")


@login_required
def doctorlist(request):
    doctor = Doctor.objects.all()
    context = {"doctor": doctor}
    return render(request, "doctorlist.html", context)


@login_required
def doctor_delete(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect("doctorlist")


@login_required
def doctor_edit(request, id):
    doctor = Doctor.objects.get(id=id)
    context = {"doctor": doctor}
    return render(request, 'doctoredit.html', context)


@login_required
def doctor_update(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == "POST":
        doctor.doctorname = request.POST.get("doctorname")
        doctor.regno = request.POST.get("regno")
        doctor.gstno = request.POST.get("gstno")
        doctor.phoneno = request.POST.get("phoneno")
        doctor.gmail = request.POST.get("gmail")
        doctor.address = request.POST.get("address")
        doctor.save()
        return redirect("doctorlist")
    return render(request, "doctoredit.html")


@login_required
def doctorwisesales(request):
    doctor = Doctor.objects.all()
    product = Product.objects.all()
    context = {"doctor": doctor, "product": product}

    if request.method == "POST":
        doctorname = Doctor.objects.get(id=request.POST.get("doctorname"))
        productname = Product.objects.get(id=request.POST.get("productname"))
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        Doctorwisesales.objects.create(
            doctorname=doctorname, productname=productname, quantity=quantity, price=price)
        return redirect("doctorwisesaleslist")
    return render(request, "doctorwisesales.html", context)


@login_required
def doctorwisesaleslist(request):
    doctorwisesales = Doctorwisesales.objects.all()
    return render(request, "doctorwisesaleslist.html", {"doctorwisesales": doctorwisesales})


@login_required
def doctorwisesales_delete(request, id):
    doctorsales = Doctorwisesales.objects.get(id=id)
    doctorsales.delete()
    return redirect("doctorwisesaleslist")


@login_required
def doctorwisesales_edit(request, id):
    doctorname = Doctor.objects.all()
    productname = Product.objects.all()
    doctor = Doctorwisesales.objects.get(id=id)
    return render(request, "doctorwiseedit.html", {
        "doctorname": doctorname,
        "productname": productname,
        "doctorwisesales": doctor
    })


@login_required
def doctorwisesales_update(request, id):
    doctor = Doctorwisesales.objects.get(id=id)
    if request.method == "POST":
        doctor.doctorname = Doctor.objects.get(id=request.POST.get("doctorname"))
        doctor.productname = Product.objects.get(id=request.POST.get("productname"))
        doctor.quantity = request.POST.get("quantity")
        doctor.price = request.POST.get("price")
        doctor.save()
        return redirect("doctorwisesaleslist")
    return render(request, "doctorwiseedit.html")


@login_required
def medical(request):
    if request.method == "POST":
        Medical.objects.create(
            medicalname=request.POST.get("medicalname"),
            gstno=request.POST.get("gstno"),
            phoneno=request.POST.get("phoneno"),
            gmail=request.POST.get("gmail"),
            address=request.POST.get("address")
        )
    return render(request, "medical.html")


@login_required
def medicallist(request):
    medical = Medical.objects.all()
    return render(request, "medicallist.html", {"medical": medical})


@login_required
def medical_edit(request, id):
    medical = Medical.objects.get(id=id)
    return render(request, "medicaledit.html", {"medical": medical})


@login_required
def medical_update(request, id):
    medical = Medical.objects.get(id=id)
    if request.method == "POST":
        medical.medicalname = request.POST.get("medicalname")
        medical.gstno = request.POST.get("gstno")
        medical.phoneno = request.POST.get("phoneno")
        medical.gmail = request.POST.get("gmail")
        medical.address = request.POST.get("address")
        medical.save()
        return redirect("medicallist")
    return render(request, "medicaledit.html")


@login_required
def medical_delete(request, id):
    medical = Medical.objects.get(id=id)
    medical.delete()
    return redirect("medicallist")


@login_required
def medicalwisesales(request):
    medicalname = Medical.objects.all()
    productname = Product.objects.all()
    context = {"medical": medicalname, "product": productname}

    if request.method == "POST":
        medical = Medical.objects.get(id=request.POST.get("medicalname"))
        product = Product.objects.get(id=request.POST.get("productname"))
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        Medicalwisesales.objects.create(
            medicalname=medical, productname=product, quantity=quantity, price=price)
        return redirect("medicalwisesaleslist")
    return render(request, "medicalwisesales.html", context)


@login_required
def medicalwisesaleslist(request):
    medicalwisesales = Medicalwisesales.objects.all()
    return render(request, "medicalwisesaleslist.html", {"medicalwisesales": medicalwisesales})


@login_required
def medicalwisesales_delete(request, id):
    medicalwisesales = Medicalwisesales.objects.get(id=id)
    medicalwisesales.delete()
    return redirect("medicalwisesaleslist")


@login_required
def medicalwisesales_edit(request, id):
    medicalname = Medical.objects.all()
    productname = Product.objects.all()
    medical = Medicalwisesales.objects.get(id=id)
    context = {"medical": medicalname, "product": productname, "medicalwisesales": medical}
    return render(request, "medicalwiseedit.html", context)


@login_required
def medicalwisesales_update(request, id):
    medical = Medicalwisesales.objects.get(id=id)
    if request.method == "POST":
        medical.medicalname = Medical.objects.get(id=request.POST.get("medicalname"))
        medical.productname = Product.objects.get(id=request.POST.get("productname"))
        medical.quantity = request.POST.get("quantity")
        medical.price = request.POST.get("price")
        medical.save()
        return redirect("medicalwisesaleslist")
    return render(request, "medicalwiseedit.html")


@login_required
def product(request):
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {"category": category, "subcategory": subcategory}

    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get("category"))
        subcategory = Subcategory.objects.get(id=request.POST.get("subcategory"))
        productname = request.POST.get("productname")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        Product.objects.create(
            category=category, subcategory=subcategory,
            productname=productname, price=price, stock=stock)
        return redirect("productlist")
    return render(request, "product.html", context)


@login_required
def productlist(request):
    product = Product.objects.all()
    return render(request, "productlist.html", {"product": product})


@login_required
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("productlist")


@login_required
def productlist_edit(request, id):
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    productname = Product.objects.get(id=id)
    context = {"category": category, "subcategory": subcategory, "productname": productname}
    return render(request, 'prodedit.html', context)


@login_required
def productlist_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.category = Category.objects.get(id=request.POST.get("category"))
        product.subcategory = Subcategory.objects.get(id=request.POST.get("subcategory"))
        product.productname = request.POST.get("productname")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        product.save()
        return redirect('productlist')
    return render(request, "prodedit.html")


@login_required
def nav(request):
    return render(request, "nav.html")


@login_required
def cat(request):
    return render(request, "cat.html")


@login_required
def sub(request):
    category = Category.objects.all()
    return render(request, "sub.html", {"category": category})


def logout_view(request):
    logout(request)
    return redirect('login')
