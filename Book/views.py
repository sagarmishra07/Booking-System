from django.shortcuts import render, redirect
import datetime
from Book import models
from django.contrib import messages
from django.http import HttpResponse
from .models import Book, Menu, Table, Special







def book(request):
    
    if request.method == 'POST':
        username = request.user
      
        table = request.POST['table']
        number_of_people = request.POST['number']
        occasion =request.POST['occasion']
        phone =request.POST['phone']
        date = request.POST['date']
        msg = None
        time = request.POST['time']
       
     
        books = Book.objects.all()
  
        for book in books:
            if str(book.date) == request.POST['date'] and str(book.time) == request.POST['time'] and str(book.table) == request.POST['table']:
                msg = messages.warning(request, 'Booking not available')
                books = Book.objects.filter(date=datetime.datetime.today())
         
                return render(request, 'book.html',{'books':books,'msg': msg}) 
            
            else:
               
                continue
                
        else:      
            book = Book(username=username, table=table, number_of_people= number_of_people, occasion=occasion, phone=phone, date=date,time=time)
            book.save()
            msg = messages.warning(request, 'Booked')
            books = Book.objects.filter(date=datetime.datetime.today())
            return render(request, 'book.html',{'books':books,'msg': msg})   
    
               
               
        return redirect('/')    
          

    
    else:
        books = Book.objects.filter(date=datetime.datetime.today())
        return render(request, 'book.html',{'books':books}) 
          
         
        
            
            

        
    


def menu(request):
    

     
    menu = Menu.objects.all()
  
    
    
    return render(request, 'menu.html',{'menu':menu})
    


def showhome(request):

    table = Table.objects.all()
    special = Special.objects.all()

    return render(request, 'index.html',{'table':table,'special':special})



