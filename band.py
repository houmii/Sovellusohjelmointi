class Band:
    """A simple attempt to model a band."""
    def __init__(self, band_name, music_genre, active): #3)Make a class called Band. The __init__( ) method for Band should store two attributes: a band_name and a music_genre.
        self.band_name = band_name
        self.music_genre = music_genre
        self.active = active
        self.home_awards = 0 ## 6)Add two new attributes called home_awards and international_awards, both with a default value of 0. Create an instance called band from this class.
        self.international_awards = 0 ## Print the number of awards the band has won, and then change this value and print it again. (1 point) ok#

    def describe_band(self): #Make a method called describe_band( ) #that prints these two pieces of information, and a method called is_active( ) that prints a message indicating that whether the band is active. (1 point) ok
        print(f"{self.band_name} {self.music_genre}")

    def is_active(self):
        print(f"Band is {self.active}")

    #7) Add a method called set_home_awards( ) and that lets you set the number of awards that the band has won in its home country.
    #Call this method with a new number and print the value again. Add a method called set_international_awards() that lets you set the number of awards that the band has won worldwide.
    #Call this method with any number you like that could represent how many awards the band has won internationally. (1p) ok
    
    def set_home_awards(self, home_awards): 
        """Set the home award to the given value"""
        self.home_awards = home_awards

    def set_international_awards(self, international_awards):
        self.international_awards = international_awards  

band = Band('Paskoja Vihanneksia', 'Punk', 'active') #4)Make an instance called band from your class. Print the two attributes individually, and then call both methods. (1 point) ok
first_band = Band('Laihian Viulistit', 'Classic', 'nonactive')#5)Create three different instances from the class and call describe_band( ) for each instance. (1 point) ok
second_band = Band('Turun Karjujat', 'Death Metal', 'active')#5)Create three different instances from the class and call describe_band( ) for each instance. (1 point) ok
third_band = Band('Hittaajat', 'Hiphop', 'active')#5)Create three different instances from the class and call describe_band( ) for each instance. (1 point) ok

print(f"Band name is {band.band_name} and genre is {band.music_genre} ")
print(f"Band name is {first_band.band_name} and genre is {first_band.music_genre} ")
print(f"Band name is {second_band.band_name} and genre is {second_band.music_genre} ")
print(f"Band name is {third_band.band_name} and genre is {third_band.music_genre} ")

band = Band('Hyviä vihanneksia', 'Punk', 'active')
print(f"Band named {band.band_name} has won {band.home_awards} homeawards and {band.international_awards} international awards")
band.home_awards = 3

band.international_awards = 2
print(f"Band named {band.band_name} has won {band.home_awards} homeawards and {band.international_awards} international awards")

band.set_home_awards(23)
print(f"Band named {band.band_name} has won {band.home_awards} homeawards and {band.international_awards} international awards")

band.set_international_awards(66)
print(f"Band named {band.band_name} has won {band.home_awards} homeawards and {band.international_awards} international awards")

RockBand = Band('SpessuTyypit', 'Psytrance', 'active')


#8) A rock band is a specific kind of band. Write a class called RockBand, that inherits the class Band.
#Add an attribute called rock_concert_movements that stores a list of rock concert movements to this rock band
#(to give some possible examples: The basic head bob, the one-armed fist pump, the up and down jumping motion, ..). ok
class RockBand(Band):
    def __init__(self, rock_concert_movements):
        self.rock_concert_movements = ["The basic head bob", "the one-armed fist pump", "the up and down jumping motion"]

    def movements(self):
        print(f"Band named {self.rock_concert_movements} has special movements like {band.rock_concert_movements}")


#8) A rock band is a specific kind of band. Write a class called RockBand, that inherits the class Band.
#Add an attribute called rock_concert_movements that stores a list of rock concert movements to this rock band
#(to give some possible examples: The basic head bob, the one-armed fist pump, the up and down jumping motion, ..). ok

#Write a method that displays these movements. Create an instance of RockBand and call its method.
#If you want to use a dictionary instead of a list, please try. How about the super class’ attribute music_genre? 
#Is it still valid, or should you remove it? (2 points) ??????????????????

#9)A choir is also a specific kind of band. Write a class Choir with the needed attributes and methods. Is there a need for overriding a meth """ ???????????