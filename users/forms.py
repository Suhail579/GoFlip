from traceback import format_exc

from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CoustomUser, Bikes, Cars , Mobiles , Electronicss , Bookss , Book_Detail ,Furniture , Gadgets


class RegisterForm(UserCreationForm):
    location = (
        ("", "Select District"),
        ("Thiruvananthapuram", "Thiruvananthapuram,Kerala"),
        ("Kollam", "Kollam"),
        ("Pathanamthitta", "Pathanamthitta,Kerala"),
        ("Alappuzha", "Alappuzha,Kerala"),
        ("Kottayam", "Kottayam,Kerala"),
        ("Idukki", "Idukki,Kerala"),
        ("Ernakulam", "Ernakulam,Kerala"),
        ("Thrissur", "Thrissur,Kerala"),
        ("Palakkad", "Palakkad,Kerala"),
        ("Malappuram", "Malappuram,Kerala"),
        ("Kozhikode", "Kozhikode,Kerala"),
        ("Wayanad", "Wayanad,Kerala"),
        ("Kannur", "Kannur,Kerala"),
        ("Kasaragod", "Kasaragod,Kerala"),
        ("Kasaragod", "Kasaragod,Kerala")
    )
    Location = forms.ChoiceField(choices=location,widget=forms.Select())

    class Meta:
        model = CoustomUser
        fields = ("username","password1","password2","email","address","pincode","profile_image","phone","Location")


class Carform(forms.ModelForm):
    brand = (
        ("Popular Brands", (
            ("maruti_suzuki", "Maruti Suzuki"),
            ("hyundai", "Hyundai"),
            ("tata_motors", "Tata Motors"),
            ("mahindra", "Mahindra"),
            ("toyota", "Toyota"),
            ("kia", "Kia"),
            ("honda", "Honda"),
            ("mg_motor", "MG Motor"),
            ("skoda", "Skoda"),
            ("volkswagen", "Volkswagen"),
        )),

        ("All Brands", (
            ("renault", "Renault"),
            ("nissan", "Nissan"),
            ("citroen", "Citroën"),
            ("jeep", "Jeep"),
            ("isuzu", "Isuzu"),
            ("force_motors", "Force Motors"),

            # Luxury
            ("mercedes_benz", "Mercedes-Benz"),
            ("bmw", "BMW"),
            ("audi", "Audi"),
            ("volvo", "Volvo"),
            ("jaguar", "Jaguar"),
            ("land_rover", "Land Rover"),
            ("lexus", "Lexus"),
            ("mini", "MINI"),
            ("porsche", "Porsche"),

            # Premium / Performance
            ("volkswagen", "Volkswagen"),
            ("byd", "BYD"),
            ("tesla", "Tesla"),

            # Other
            ("aston_martin", "Aston Martin"),
            ("bentley", "Bentley"),
            ("rolls_royce", "Rolls-Royce"),
            ("lamborghini", "Lamborghini"),
            ("ferrari", "Ferrari"),
            ("maserati", "Maserati"),
            ("lotus", "Lotus"),
            ("mclaren", "McLaren"),

            ("other", "Other"),
        )),
    )

    TRANSMISSION = (
        ("manual", "Manual"),
        ("automatic", "Automatic")
    )
    year = forms.TypedChoiceField(
        choices=[(year, year) for year in range(2026, 1999, -1)],
        empty_value=None,
        widget=forms.Select(attrs={
    
            }))
    fuel = (("petrol", "Petrol"), ("diesel", "Diesel"), ("electric", "Electric"))
    Fuel = forms.ChoiceField(choices=fuel, widget=forms.RadioSelect)
    Brand = forms.ChoiceField(choices=brand, widget=forms.Select)
    Transmission = forms.ChoiceField(choices=TRANSMISSION, widget=forms.Select)


    class Meta:
        model = Cars
        fields = ["Brand","Model","year","Fuel","Transmission","KM_drive","Title","Description","Price","Images"]


class Bikeform(forms.ModelForm):
    BRAND_CHOICES = [
        ("Popular Brands", [
            ("Hero", "Hero"),
            ("Honda", "Honda"),
            ("TVS", "TVS"),
            ("Bajaj", "Bajaj"),
            ("Yamaha", "Yamaha"),
            ("Royal Enfield", "Royal Enfield"),
            ("Suzuki", "Suzuki"),
            ("KTM", "KTM"),
        ]),

        ("All Brands", [
            ("Jawa", "Jawa"),
            ("Yezdi", "Yezdi"),
            ("Mahindra", "Mahindra"),
            ("BMW Motorrad", "BMW Motorrad"),
            ("Kawasaki", "Kawasaki"),
            ("Triumph", "Triumph"),
            ("Harley-Davidson", "Harley-Davidson"),
            ("Aprilia", "Aprilia"),
            ("Vespa", "Vespa"),
            ("Piaggio", "Piaggio"),
            ("Ola Electric", "Ola Electric"),
            ("Ather", "Ather"),
            ("Ultraviolette", "Ultraviolette"),
            ("Vida", "Vida"),
            ("Revolt", "Revolt"),
            ("Oben", "Oben"),
            ("Ampere", "Ampere"),
            ("Simple Energy", "Simple Energy"),
            ("Other", "Other"),
        ]),
    ]
    year = forms.TypedChoiceField(
    choices=[(year, year) for year in range(2026, 1999, -1)],
    empty_value=None,
    widget=forms.Select(attrs={

        })
    )

    ownership = (
        ("1st", "1st Owner"),
        ("2nd", "2nd Owner"),
        ("3rd", "3rd Owner"),
        ("4th", "4th Owner"),
        ("5th", "5th Owner"),
    )
    Ownership = forms.ChoiceField(choices=ownership,widget=forms.Select)
    fuel = (("petrol", "Petrol"),("diesel", "Diesel"),("electric", "Electric"))
    Fuel = forms.ChoiceField(choices=fuel,widget=forms.RadioSelect)
    Brand = forms.ChoiceField(choices=BRAND_CHOICES,widget=forms.Select)
    class Meta:
        model = Bikes
        fields = ["Brand","Model","Fuel","year","Title","KM_drive","Description","Price","Images","Ownership"]


class Mobileform(forms.ModelForm):
    mobile_brand = (
        ("Popular Brands", (
            ("samsung", "Samsung"),
            ("apple", "Apple"),
            ("oppo", "OPPO"),
            ("honor", "HONOR"),
            ("xiaomi", "Xiaomi"),
            ("oneplus", "OnePlus"),
            ("vivo", "Vivo"),
            ("oppo", "Oppo"),
            ("realme", "Realme"),
            ("motorola", "Motorola"),
            ("iqoo", "iQOO"),
            ("nothing", "Nothing"),
        )),

        ("All Brands", (
            ("google", "Google Pixel"),
            ("poco", "POCO"),
            ("infinix", "Infinix"),
            ("tecno", "Tecno"),
            ("honor", "HONOR"),
            ("nokia", "Nokia"),
            ("cmf", "CMF"),
            ("lava", "Lava"),
            ("jio", "Jio"),
            ("other", "Other"),
        )),
    )
    year = forms.TypedChoiceField(
        choices=[(year, year) for year in range(2026, 1999, -1)],
        empty_value=None,
        widget=forms.Select(attrs={
    
            })
        )
    Brand = forms.ChoiceField(choices=mobile_brand, widget=forms.Select)
    class Meta:
        model = Mobiles
        fields = ["Brand","Model","year","Title","Description","Price","Images"]



class Electronicsform(forms.ModelForm):
    brands = (
        ("Popular Brands", (
            ("samsung", "Samsung"),
            ("lg", "LG"),
            ("sony", "Sony"),
            ("whirlpool", "Whirlpool"),
            ("haier", "Haier"),
            ("godrej", "Godrej"),
            ("voltas", "Voltas"),
            ("bosch", "Bosch"),
            ("panasonic", "Panasonic"),
            ("ifb", "IFB"),
            ("philips", "Philips"),
            ("havells", "Havells"),
            ("bajaj", "Bajaj"),
            ("crompton", "Crompton"),
            ("prestige", "Prestige"),
        )),

        ("All Brands", (
            ("tcl", "TCL"),
            ("mi", "MI"),
            ("oneplus", "OnePlus"),
            ("realme", "Realme"),
            ("acer", "Acer"),
            ("onida", "Onida"),
            ("videocon", "Videocon"),
            ("sansui", "Sansui"),
            ("vu", "VU"),
            ("kodak", "Kodak"),
            ("toshiba", "Toshiba"),
            ("sharp", "Sharp"),
            ("hitachi", "Hitachi"),
            ("blue_star", "Blue Star"),
            ("usha", "Usha"),
            ("jbl", "JBL"),
            ("boat", "boAt"),
            ("zebronics", "Zebronics"),
            ("portronics", "Portronics"),
            ("noise", "Noise"),
            ("fire_boltt", "Fire-Boltt"),
            ("other", "Other"),
        )),
    )
    items = (
        ("Popular Items", (
            ("tv", "TV"),
            ("refrigerator", "Refrigerator"),
            ("washing_machine", "Washing Machine"),
            ("fan", "Fan"),
            ("air_conditioner", "Air Conditioner"),
            ("air_cooler", "Air Cooler"),
            ("microwave_oven", "Microwave Oven"),
            ("mixer_grinder", "Mixer Grinder"),
            ("water_purifier", "Water Purifier"),
            ("water_heater", "Water Heater"),
            ("vacuum_cleaner", "Vacuum Cleaner"),
        )),

        ("All Items", (
            ("ceiling_fan", "Ceiling Fan"),
            ("table_fan", "Table Fan"),
            ("exhaust_fan", "Exhaust Fan"),
            ("air_purifier", "Air Purifier"),
            ("home_theater", "Home Theater"),
            ("soundbar", "Soundbar"),
            ("speaker", "Speaker"),
            ("headphones", "Headphones"),
            ("earbuds", "Earbuds"),
            ("set_top_box", "Set Top Box"),
            ("streaming_device", "Streaming Device"),
            ("router", "Wi-Fi Router"),
            ("modem", "Modem"),
            ("inverter", "Inverter"),
            ("ups", "UPS"),
            ("other", "Other"),
        )),
    )
    Items = forms.ChoiceField(choices=items,widget=forms.Select)
    Brand = forms.ChoiceField(choices=brands,widget=forms.Select)
    class Meta:
        model = Electronicss
        fields = ["Brand","Items","year","Title","Description","Price","Images"]


class Booksform(forms.ModelForm):
    class Meta:
        model = Bookss
        fields = ["Book_name","Author","Title","year","Description","Price","Images"]

class Gadgetsform(forms.ModelForm):
    brand = (
        ("Popular Brands", (
            ("apple", "Apple"),
            ("samsung", "Samsung"),
            ("oneplus", "OnePlus"),
            ("xiaomi", "Xiaomi"),
            ("realme", "Realme"),
            ("sony", "Sony"),
            ("boat", "boAt"),
            ("jbl", "JBL"),
            ("noise", "Noise"),
            ("motorola", "Motorola"),
        )),

        ("All Brands", (
            ("vivo", "Vivo"),
            ("oppo", "Oppo"),
            ("nothing", "Nothing"),
            ("google", "Google"),
            ("poco", "POCO"),
            ("iqoo", "iQOO"),
            ("asus", "ASUS"),
            ("lenovo", "Lenovo"),
            ("hp", "HP"),
            ("dell", "Dell"),
            ("logitech", "Logitech"),
            ("zebronics", "Zebronics"),
        )),
    )

    items = (
        ("earbuds", "Earbuds"),
        ("tablet", "Tablet"),
        ("smartwatch", "Smart Watch"),
        ("headphones", "Headphones"),
        ("bluetooth_speaker", "Bluetooth Speaker"),
        ("power_bank", "Power Bank"),
        ("charger", "Charger"),
        ("smart_band", "Smart Band"),
        ("camera", "Camera"),
        ("action_camera", "Action Camera"),
        ("drone", "Drone"),
        ("projector", "Projector")
    )
    year = forms.TypedChoiceField(
            choices=[(year, year) for year in range(2026, 1999, -1)],
            empty_value=None,
            widget=forms.Select(attrs={
        
                }))
    Brand = forms.ChoiceField(choices=brand,widget=forms.Select)
    Item = forms.ChoiceField(choices=items,widget=forms.Select)
    class Meta:
        model = Gadgets
        fields = ["Brand","Item","year","Title","Description","Price","Images"]



class Furnitureform(forms.ModelForm):

    items = (("sofa", "Sofa"),
            ("bed", "Bed"),
            ("wardrobe", "Wardrobe"),
            ("dining_table", "Dining Table"),
            ("chair", "Chair"),
            ("study_table", "Study Table"),
            ("coffee_table", "Coffee Table"),
            ("shoe_rack", "Shoe Rack"),
            ("dressing_table", "Dressing Table"))
    
    Item = forms.ChoiceField(choices=items,widget=forms.Select)
    class Meta:
        model = Furniture
        fields = ["Brand","Item","Material","Condition","Title","Description","Price","Images"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
