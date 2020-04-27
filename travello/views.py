from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
   
   """dest1 = Destination()
   dest1.name = 'Mumbai'
   dest1.desc = 'The city that never sleeps'
   dest1.img = 'destination_1.jpg'
   dest1.price = 700
   dest1.offer = False

   dest2 = Destination()
   dest2.name = 'Chennai'
   dest2.desc = 'The beach city'
   dest2.img = 'destination_2.jpg'
   dest2.price = 600
   dest2.offer = True

   dest3 = Destination()
   dest3.name = 'Banglore'
   dest3.desc = 'IT hub of the country'
   dest3.img = 'destination_3.jpg'
   dest3.price = 650
   dest3.offer = False

   dests = [dest1, dest2, dest3]"""

   dests = Destination.objects.all()

   return render(request,'index.html',{'dests': dests})