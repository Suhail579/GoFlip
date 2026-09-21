import random
from multiprocessing import context

from django.contrib.auth import authenticate, logout
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm, LoginForm, Carform, Bikeform, Mobileform, Electronicsform, Booksform, Gadgetsform, \
    Furnitureform
from users.models import Cars, Bikes, Electronicss, Bookss, Mobiles, Furniture, Gadgets
from users.models import CoustomUser


# Create your views here.
class Home(View):

    def get(self, request):

        # Check login
        if not request.user.is_authenticated:
            return redirect("Login")



        products = []

        for product in Cars.objects.all():
            product.category = "car"
            products.append(product)

        for product in Bikes.objects.all():
            product.category = "bike"
            products.append(product)

        for product in Mobiles.objects.all():
            product.category = "mobile"
            products.append(product)

        for product in Electronicss.objects.all():
            product.category = "electronics"
            products.append(product)

        for product in Bookss.objects.all():
            product.category = "book"
            products.append(product)

        for product in Gadgets.objects.all():
            product.category = "gadgets"
            products.append(product)

        for product in Furniture.objects.all():
            product.category = "furniture"
            products.append(product)

        products.sort(
            key=lambda x: x.created_at,
            reverse=True
        )

        return render(request, "home.html", {
            "products": products
        })


class Register(View):
    def get(self, request):
        form_instance = RegisterForm()
        context = {"form": form_instance}
        return render(request, "index.html", context)

    def post(self, request):
        form_instance = RegisterForm(request.POST, request.FILES)
        if form_instance.is_valid():
            v = form_instance.save(commit=False)
            v.is_active = False

            o = random.randint(10000, 999999)
            v.otp = o
            v.save()

            send_mail(
                "Django Auth OTP",
                f"Your OTP is {v.otp}",
                "suhailnasim579@gmail.com",
                [v.email],
                fail_silently=False,
            )
            return redirect("Otp")

        return render(request, "index.html", {"form": form_instance})




from django.contrib.auth import login

class Otp(View):

    def get(self, request):
        return render(request, "otp.html")

    def post(self, request):

        otp = request.POST.get("otp")

        try:
            user = CoustomUser.objects.get(otp=otp)

            user.is_active = True
            user.verified = True
            user.otp = None
            user.save()
            login(request, user)
            return redirect("Choose")

        except CoustomUser.DoesNotExist:
            return render(request, "otp.html", {
                "error": "Invalid OTP"
            })

class Choose(View):
    def get(self,request):
        return render(request,"choose.html")


class Profile(View):
    def get(self,request):
        return render(request,"profile.html",context={})

class Editprofiles(View):
    def get(self, request):
        return render(request,"editprofile.html")

    def post(self, request):

        user = request.user

        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.address = request.POST.get("address")
        user.pincode = request.POST.get("pincode")
        user.Location = request.POST.get("Location")
        user.phone = request.POST.get("phone")
        if request.FILES.get("profile_image"):
            user.profile_image = request.FILES.get("profile_image")

        user.save()

        return redirect("Profile")

class Addproduct(View):
    def get(self,request):
        return render(request,"addproduct.html")


class Car(View):

    def get(self, request):
        form = Carform()
        context = {"car": form}
        return render(request, "car.html", context)

    def post(self, request):
        form = Carform(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            car.seller = request.user # Logged-in user becomes the seller
            car.save()
            return redirect("Addproduct")


class Bike(View):
    def get(self,request):
        form = Bikeform
        context = {"bikes":form}
        return render(request,"bike.html",context)

    def post(self,request):
        form = Bikeform(request.POST,request.FILES)
        if form.is_valid():
            bike = form.save()
            bike.seller = request.user  # Logged-in user becomes the seller
            bike.save()
            return redirect("Addproduct")

class Mobile(View):
    def get(self, request):
        form = Mobileform
        context = {"mobiles": form}
        return render(request, "mobile.html", context)

    def post(self, request):
        form = Mobileform(request.POST, request.FILES)
        if form.is_valid():
            mobile = form.save()
            mobile.seller = request.user  # Automatically identify logged-in user
            mobile.save()
            return redirect("Addproduct")


class Electronics(View):

    def get(self, request):
        form = Electronicsform()
        context = {"Electronics": form}
        return render(request, "electronics.html", context)

    def post(self, request):
        form = Electronicsform(request.POST, request.FILES)

        if form.is_valid():

            electronics = form.save()

            # Save the logged-in user as seller
            electronics.seller = request.user
            electronics.save()

            return redirect("Addproduct")

        context = {"Electronics": form}
        return render(request, "electronics.html", context)

class Furnitures(View):
    def get(self,request):
        form = Furnitureform
        context = {"Furniture":form}
        return render(request,"furniture.html",context)

    def post(self,request):
        form = Furnitureform(request.POST,request.FILES)
        if form.is_valid():
            Furniture = form.save()
            Furniture.seller = request.user  # Automatically identify logged-in user
            Furniture.save()
            return redirect("Addproduct")

class Books(View):
    def get(self, request):
        form = Booksform
        context = {"Books": form}
        return render(request, "books.html", context)

    def post(self, request):
        form = Booksform(request.POST,request.FILES)
        if form.is_valid():
            book = form.save()
            book.seller = request.user  # Automatically identify logged-in user
            book.save()
            return redirect("Addproduct")

class Gadgetss(View):
    def get(self, request):
        form = Gadgetsform
        context = {"Gadgets": form}
        return render(request, "gadget.html", context)

    def post(self, request):
        form = Gadgetsform(request.POST,request.FILES)
        if form.is_valid():
            gadget = form.save()
            gadget.seller = request.user  # Automatically identify logged-in user
            gadget.save()
            return redirect("Addproduct")

class CategoryProducts(View):

    def get(self, request, category):

        products = []

        if category == "cars":
            for product in Cars.objects.all():
                product.category = "car"
                products.append(product)

        elif category == "bike":
            for product in Bikes.objects.all():
                product.category = "bike"
                products.append(product)

        elif category == "mobile":
            for product in Mobiles.objects.all():
                product.category = "mobile"
                products.append(product)

        elif category == "electronics":
            for product in Electronicss.objects.all():
                product.category = "electronics"
                products.append(product)

        elif category == "book":
            for product in Bookss.objects.all():
                product.category = "book"
                products.append(product)

        elif category == "gadgets":
            for product in Gadgets.objects.all():
                product.category = "gadgets"
                products.append(product)

        elif category == "furniture":
            for product in Furniture.objects.all():
                product.category = "furniture"
                products.append(product)

        products.sort(
            key=lambda x: x.created_at,
            reverse=True
        )

        context = {
            "products": products,
            "category": category
        }

        return render(request, "category.html", context)


class Viewprodect(View):
    def get(self, request):

# ---------------------------------------------------------------------#
        # five = timezone.now() - timedelta(minutes=1)
        # products = []
        #
        #
        # for product in Cars.objects.filter(created_at__gte=five):
        #     product.category = "car"
        #     products.append(product)
# ---------------------------------------------------------------------#

        products = []
        for product in Cars.objects.all():
            product.category = "car"
            products.append(product)

        for product in Bikes.objects.all():
            product.category = "bike"
            products.append(product)

        for product in Mobiles.objects.all():
            product.category = "mobile"
            products.append(product)

        for product in Electronicss.objects.all():
            product.category = "electronics"
            products.append(product)

        for product in Bookss.objects.all():
            product.category = "book"
            products.append(product)

        for product in Furniture.objects.all():
            product.category = "furniture"
            products.append(product)

        for product in Gadgets.objects.all():
            product.category = "gadgets"
            products.append(product)

        products.sort(key=lambda product: product.created_at,reverse=True)

        context={"products": products}

        return render(request, "viewproduct.html", context)

    # You Have to any change in the Viewprodect. Also must have change the latest...

class Latest(View):
    def get(self,request):
        products = []
        for product in Cars.objects.all():
            product.category = "car"
            products.append(product)

        for product in Bikes.objects.all():
            product.category = "bike"
            products.append(product)

        for product in Mobiles.objects.all():
            product.category = "mobile"
            products.append(product)

        for product in Electronicss.objects.all():
            product.category = "electronics"
            products.append(product)

        for product in Bookss.objects.all():
            product.category = "book"
            products.append(product)

        for product in Furniture.objects.all():
            product.category = "furniture"
            products.append(product)

        for product in Gadgets.objects.all():
            product.category = "gadgets"
            products.append(product)

        products.sort(key=lambda product: product.created_at, reverse=True)

        context = {"products": products}

        return render(request, "latest.html", context)



class Book_Details(View):
    def get(self,request,product):
        book = Bookss.objects.get(id=product)
        form_instance = Booksform(instance=book)
        context = {"form":form_instance, "book":book}
        return render(request,'book_details.html',context)

class Mobile_Details(View):
    def get(self,request,product):
        mobile = Mobiles.objects.get(id=product)
        form_instance = Mobileform(instance=mobile)
        context = {"form":form_instance,"mobile":mobile}
        return render(request,'mobile_details.html',context)

class Bike_Details(View):
    def get(self,request,product):
        bike = Bikes.objects.get(id=product)
        form_instance = Bikeform(instance=bike)
        context = {"form":form_instance,"bike":bike}
        return render(request,'bike_detail.html',context)

class Electronics_Details(View):
    def get(self, request, product):
        electronics = Electronicss.objects.get(id=product)
        form_instance = Electronicsform(instance=electronics)
        context = {"form": form_instance,"electronics": electronics}
        return render(request,"electronics_Details.html",context)


class Car_Details(View):
    def get(self, request, product):
        car = Cars.objects.get(id=product)
        form_instance = Carform(instance=car)
        context = {"form": form_instance,"car": car}
        return render(request, "Car_Details.html", context)

class Furniture_Details(View):
    def get(self, request, product):
        Furnitures = Furniture.objects.get(id=product)
        form_instance = Furnitureform(instance=Furnitures)  # use Electronicsform here
        context = {"form": form_instance,"furniture":Furnitures}
        return render(request, 'furniture_Details.html', context)


class Gadgets_Details(View):
    def get(self, request, product):
        gadget = Gadgets.objects.get(id=product)
        form_instance = Furnitureform(instance=gadget)  # use Electronicsform here
        context = {"form": form_instance,"gadget":gadget}
        return render(request, 'gadgets_Details.html', context)


class Search(View):
    def get(self, request):
        query = request.GET.get("q", "").strip()


        # CAR

        car = Cars.objects.filter(
            Q(Brand__icontains=query) |
            Q(Model__icontains=query) |
            Q(year__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # BIKE

        bike = Bikes.objects.filter(
            Q(Brand__icontains=query) |
            Q(Model__icontains=query) |
            Q(year__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # MOBILE

        mobile = Mobiles.objects.filter(
            Q(Brand__icontains=query) |
            Q(Model__icontains=query) |
            Q(year__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # FURNITURE

        furniture = Furniture.objects.filter(
            Q(Item__icontains=query) |
            Q(Brand__icontains=query) |
            Q(Material__icontains=query) |
            Q(Condition__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # BOOKS

        books = Bookss.objects.filter(
            Q(Book_name__icontains=query) |
            Q(Author__icontains=query) |
            Q(year__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # ELECTRONICS

        electronics = Electronicss.objects.filter(
            Q(Items__icontains=query) |
            Q(Brand__icontains=query) |
            Q(year__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # GADGETS

        gadget = Gadgets.objects.filter(
            Q(Brand__icontains=query) |
            Q(Item__icontains=query) |
            Q(year__icontains=query) |
            Q(Title__icontains=query) |
            Q(Description__icontains=query) |
            Q(Price__icontains=query)
        )

        # LATEST PRODUCTS
        products = []


        for product in car:
            product.category = "car"
            products.append(product)


        for product in bike:
            product.category = "bike"
            products.append(product)


        for product in mobile:
            product.category = "mobile"
            products.append(product)


        for product in furniture:
            product.category = "furniture"
            products.append(product)


        for product in books:
            product.category = "books"
            products.append(product)


        for product in electronics:
            product.category = "electronics"
            products.append(product)


        for product in gadget:
            product.category = "gadget"
            products.append(product)

        # SORT NEWEST FIRST

        products.sort(
            key=lambda product: product.created_at,reverse=True)

        context = {"d": products,"query": query}

        return render(request, "search.html", context)


class Login(View):
    def get(self,request):
        form = LoginForm
        context = {"form":form}
        return render(request,"login.html",context)

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)

            u = data["username"]
            p = data["password"]

            user = authenticate(username=u , password=p)

            if user:    
                login(request,user)
                return redirect("Home")
            else:
                return redirect("Login")

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect("Login")


