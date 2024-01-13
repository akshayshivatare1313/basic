import datetime
from datetime import date


class Employee:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display_emp(self):
        print("Employee ID :", self.eid)
        print("Employee name :", self.ename)

employee_add = Employee(9001, "Akshay Shiv", 130000)
employee_add.display_emp()

class Movie:
    def __init__(self, mname, genre, lang, rating):
        self.mname = mname
        self.genre = genre
        self. lang = lang
        self.rating = rating

    def disp_movie(self):
        print("Movie name :", self.mname)
        print("Movie Language :", self.lang)
        print("Movie Genre :", self.genre)

movie_1 = Movie("KGF-2", "Action", "Hindi", 9.6)
movie_1.disp_movie()

class Student:
    def __init__(self, sid, sname, std, marks):
        self.sid = sid
        self.sname = sname
        self.std = std
        self.marks = marks

    def show_student_info(self):
        print(f"Student is : {self.sid}\nstudent name is {self.sname} \nstd is {self.std}\nstudent marks are : {self.marks} ")

student_1 = Student(9, "sandip", "12th", 97)
student_1.show_student_info()

class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def show_car(self):
        print(f"car model is {self.model}\ncar company is {self.company}\nmanufacturing year is {self.year}")

car_1 = Car("Ford","Musatang", 1968)
car_1.show_car()

class BankAccount:
    def __init__(self, name, acnumber, balance):
        self.name = name
        self.balance = balance
        self.acnumber = acnumber

    def show_ac_info(self):
        print(f"account holder name :{self.name}\naccount balance :{self.balance}\naccount number :{self.acnumber}")

bank_ac_1 = BankAccount("Sachin Salunkhe", 1029384765, 200)
bank_ac_1.show_ac_info()

class Animal:
    def __init__(self, species, name, colour ):
        self.species = species
        self.name = name
        self.colour = colour

    def show_animal_info(self):
        print(f"Animal specie :{self.species}\nanimal name is :{self.name}\nhaving color :{self.colour}")

    def update_animal_info(self, newname):
        self.name = newname

    def check_health(self, health):
        self.health = health
        if self.health == "good".lower():
            print(f"{self.name}'s health is good!!")
        else:
            print(f"{self.name}'s health is Not good!!")

animal_1 = Animal("Dog","Rocky","brown")
animal_1.show_animal_info()
animal_1.update_animal_info("panda")

animal_1.show_animal_info()
animal_1.check_health("good")

class Book:
    def __init__(self, bname, author, pubyear):
        self.bname = bname
        self.author = author
        self.pubyear = pubyear

    def show_book_info(self):
        print(f"Book name :{self.bname} Book author :{self.author} year of publishing :{self.pubyear}")

book_1 = Book("Gita","Shri-Krishna!","Unknown")
book_1.show_book_info()


class Water_Bottle:
    def __init__(self, type, capacity, brand):
        self.type = type
        self.brand = brand
        self.capacity = capacity

    def bottle_details(self):
        print(f"bottle type is {self.type}, having capacity of {self.capacity} from {self.brand} brand!")

bottle_1 = Water_Bottle("plastic","1 litre","Bislary")
bottle_2 = Water_Bottle("fibre","500 ml","TRITAN")
bottle_1.bottle_details()
bottle_2.bottle_details()

class Human:
    def __init__(self, gender, name, nationality):
        self.gender = gender
        self.name = name
        self.nationality = nationality

    def show_human(self):
        print(f"Gender is {self.gender} having name {self.name} with {self.nationality} nationality!!")
human_1 = Human("Female","MAyuri","Indian")
human_1.show_human()

class Wood:
    def __init__(self, type, color, obtained):
        self.type =type
        self.color = color
        self.obtained = obtained

    def wood_details(self):
        print(f"the wood type is {self.type} having color {self.color} obtained from {self.obtained}")

wood_1 = Wood("hard","red","Brazil")
wood_1.wood_details()

class Hospital:
    def __init__(self, pid, pname, bill, disease):
        self.pid = pid
        self.pname = pname
        self.bill = bill
        self.disease = disease

    def show_patient_info(self):
        print(f"pationt name is '{self.pname}' have id '{self.pid}' was diagnosed with '{self.disease}'. The total Bill amount {self.bill}rs.")

pationt_1 = Hospital(41,"nilam katke",20000, "Arthriti")
pationt_1.show_patient_info()

class PaymentInfo:
    def __init__(self, mode, amount, date ):
        self.mode = mode
        self.amount = amount
        self.date = date

    def show_payment_info(self):
        print(f"mode of payment :{self.mode}\namount :{self.amount}rs\nDate :{self.date}")
payment_1 = PaymentInfo("Online",13000, date.today())
payment_1.show_payment_info()

class Forest:
    def __init__(self, fname, location, type, area):
        self.fname = fname
        self.location = location
        self.type = type
        self. area = area

    def forest_info(self):
        print(f"{self.fname} is {self.type} forest having large are of {self.area}sq.km in {self.location}")

forest_1 = Forest("Amazon","South-America","Tropical",6000000)
forest_1.forest_info()

class Sports:
    def __init__(self, name, category, players, duration):
        self.name = name
        self.category =category
        self.players = players
        self.duration = duration

    def show_sports_details(self):
        print(f"{self.name} is {self.category} sport can be played with {self.players} players for {self.duration} minutes")

sport_1 = Sports("Football","Team",11,90)
sport_1.show_sports_details()

class Airplane:
    def __init__(self, name, manufacturer, capacity, speed):
        self.name = name
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.speed = speed

    def plane_info(self):
        print(f"{self.name} is palne having speed {self.speed}km/h with capacity of {self.capacity} seats manufacture by {self.manufacturer} company")

boeing_747 = Airplane("Boeing 747","Boeing",416,460)
boeing_747.plane_info()

class Casino:
    def __init__(self,name ,location, games_availabe, opening_hour):
        self.name = name
        self.location = location
        self.games_available = games_availabe
        self.opening_hour = opening_hour

    def casino_details(self):
        print(f"casino name :{self.name}\nlocation :{self.location}\n with games availabe {self.games_available} open for {self.opening_hour}")

casino_1 = Casino("Casino Royal","london",['Poker','Blackjack'],"24/7")

casino_1.casino_details()

class Library:
    def __init__(self, name, location, books_available, librarian):
        self.name = name
        self.location = location
        self.books_available = books_available
        self.librarian = librarian

    def display_info(self):
        print(f"Library: {self.name}")
        print(f"Location: {self.location}")
        print(f"Librarian: {self.librarian}")
        print(f"Books Available: {', '.join(self.books_available)}")

city_library = Library(name="City Library", location="Downtown", books_available=["Fiction", "Non-fiction"], librarian="Alice Johnson")

city_library.display_info()

class Cafe:
    def __init__(self, name, location, menu, capacity):
        self.name = name
        self.location = location
        self.menu = menu
        self.capacity = capacity

    def display_info(self):
        print(f"Cafe: {self.name}")
        print(f"Location: {self.location}")
        print(f"Capacity: {self.capacity} people")
        print(f"Menu: {', '.join(self.menu)}")

coffee_shop = Cafe(name="Cool Royal Cafe", location="Main Street", menu=["Coffee", "Pastries", "Sandwiches"], capacity=30)

coffee_shop.display_info()

class University:
    def __init__(self, name, location, programs_offered, students_enrolled):
        self.name = name
        self.location = location
        self.programs_offered = programs_offered
        self.students_enrolled = students_enrolled

    def display_info(self):
        print(f"University: {self.name}")
        print(f"Location: {self.location}")
        print(f"Programs Offered: {', '.join(self.programs_offered)}")
        print(f"Students Enrolled: {self.students_enrolled}")


pune_university = University(name="Pune University", location="Pune", programs_offered=["Computer Science", "Business Administration"], students_enrolled=5000)
pune_university.display_info()

class Hospital:
    def __init__(self, name, location, departments, doctors_available):
        self.name = name
        self.location = location
        self.departments = departments
        self.doctors_available = doctors_available

    def display_info(self):
        print(f"Hospital: {self.name}")
        print(f"Location: {self.location}")
        print(f"Departments: {', '.join(self.departments)}")
        print(f"Doctors Available: {', '.join(self.doctors_available)}")

city_hospital = Hospital(name="City Hospital", location="Mumbai", departments=["Cardiology", "Orthopedics"], doctors_available=["Dr. salunke", "Dr. strange"])
city_hospital.display_info()

class Gym:
    def __init__(self, name, location, equipment_available, trainers_available):
        self.name = name
        self.location = location
        self.equipment_available = equipment_available
        self.trainers_available = trainers_available

    def display_info(self):
        print(f"Gym: {self.name}")
        print(f"Location: {self.location}")
        print(f"Equipment Available: {', '.join(self.equipment_available)}")
        print(f"Trainers Available: {', '.join(self.trainers_available)}")


fitness_center = Gym(name="Golds Gym", location="Fitness Street Nagpur", equipment_available=["Treadmills", "Weights"], trainers_available=["Tripple H", "John Cena"])

fitness_center.display_info()



class ArtGallery:
    def __init__(self, name, location, artworks, opening_hours):
        self.name = name
        self.location = location
        self.artworks = artworks
        self.opening_hours = opening_hours

    def display_info(self):
        print(f"Art Gallery: {self.name}")
        print(f"Location: {self.location}")
        print(f"Artworks: {', '.join(self.artworks)}")
        print(f"Opening Hours: {self.opening_hours}")


modern_art_gallery = ArtGallery(name="Modern Impressions", location="Camp Pune", artworks=["Paintings", "Sculptures"], opening_hours="10 AM to 6 PM")
modern_art_gallery.display_info()

class Zoo:
    def __init__(self, name, location, animals, opening_hours ):
        self.name = name
        self.location = location
        self.animals = animals
        self.opening_hours = opening_hours

    def zoo_details(self):
        print(f"zoo name :{self.name}\nlocated in {self.location}\nanimals are:{self.animals}\n open for {self.opening_hours}")

zoo_1 = Zoo("Fortune ZOO!!","Mumbai",['tigers','snakes','rhinos'],"10 AM to 6 PM")
zoo_1.zoo_details()

class MovieTheater:
    def __init__(self, name, location, movies_playing, screens_available):
        self.name = name
        self.location = location
        self.movies_playing = movies_playing
        self.screens_available = screens_available

    def display_info(self):
        print(f"Movie Theater: {self.name}")
        print(f"Location: {self.location}")
        print(f"Movies Playing: {self.movies_playing}")
        print(f"Screens Available: {self.screens_available}")


cinema_plex = MovieTheater(name="PVR", location="Kumar Pacific Mall,Pune", movies_playing=["Avengers: Endgame", "Animal"], screens_available=5)
cinema_plex.display_info()

class Hotel:
    def __init__(self, name, location, rooms_available, amenities):
        self.name = name
        self.location = location
        self.rooms_available = rooms_available
        self.amenities = amenities

    def display_info(self):
        print(f"Hotel: {self.name}")
        print(f"Location: {self.location}")
        print(f"Rooms Available: {self.rooms_available}")
        print(f"Amenities: {self.amenities}")


luxury_hotel = Hotel(name="Haytt", location="Satara", rooms_available=100, amenities=["Swimming Pool", "Fitness Center", "Sports ground"])
luxury_hotel.display_info()

class Bank:
    def __init__(self, name, location, accounts, services_offered):
        self.name = name
        self.location = location
        self.accounts = accounts
        self.services_offered = services_offered

    def display_info(self):
        print(f"Bank: {self.name}")
        print(f"Location: {self.location}")
        print(f"Services Offered: {self.services_offered}")
        print(f"Number of Accounts: {len(self.accounts)}")


city_bank = Bank(name="Pune City Bank", location="Financial District", accounts=["Savings", "Checking"], services_offered=["Loans", "Investments"])

city_bank.display_info()


class MusicStudio:
    def __init__(self, name, location, instruments_available, recording_engineers):
        self.name = name
        self.location = location
        self.instruments_available = instruments_available
        self.recording_engineers = recording_engineers

    def display_info(self):
        print(f"Music Studio: {self.name}")
        print(f"Location: {self.location}")
        print(f"Instruments Available: {self.instruments_available}")
        print(f"Recording Engineers: {self.recording_engineers}")

sound_city_studio = MusicStudio(name="Sony Studio", location="Uk", instruments_available=["Piano", "Guitar", "Drums"], recording_engineers=["sammy", "sandy"])
sound_city_studio.display_info()

class Supermarket:
    def __init__(self, name, location, products_available):
        self.name = name
        self.location = location
        self.products_available = products_available


    def display_info(self):
        print(f"Supermarket: {self.name}")
        print(f"Location: {self.location}")
        print(f"Products Available: {self.products_available}")


freshmart = Supermarket(name="D-mart", location="Suburban Plaza", products_available=["Groccery", "Vegetables", "Dairy"])

freshmart.display_info()

class LawFirm:
    def __init__(self, name, location, lawyers, legal_cases):
        self.name = name
        self.location = location
        self.lawyers = lawyers
        self.legal_cases = legal_cases

    def display_info(self):
        print(f"Law Firm: {self.name}")
        print(f"Location: {self.location}")
        print(f"Number of Lawyers: {len(self.lawyers)}")
        print(f"Legal Cases: {', '.join(self.legal_cases)}")


legal_aces_lawfirm = LawFirm(name="Legal Aces", location="Law District", lawyers=["John Smith", "Emma Watson"], legal_cases=["Smith vs. Jones", "Doe's Estate"])
legal_aces_lawfirm.display_info()

class PoliceStation:
    def __init__(self, name, location, officers):
        self.name = name
        self.location = location
        self.officers = officers


    def Police_station_display(self):
        print(f"police station name:{self.name}\nlocated {self.location} having {self.officers} officers")

police_station_info = PoliceStation("Bhor","pune",13)
police_station_info.Police_station_display()

class Language:
    def __init__(self, lname, place, difficulty):
        self.lname = lname
        self.place = place
        self.difficulty = difficulty

    def language_details(self):
        print(f"in {self.place} {self.lname} language is spoken often which difficulty level is {self.difficulty}")

language_1 = Language("Marathi","maharahtra","Medium")
language_1.language_details()