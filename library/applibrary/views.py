from datetime import date, timedelta

from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import User, Book, Category, Barrowed_book

def add_person(request):
    if request.method == "POST":
        first_name_value = request.POST.get("fname")
        last_name_value = request.POST.get("lname")
        birth_date = request.POST.get("birth_date")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        p = User(first_name = first_name_value, last_name = last_name_value,birth_date=birth_date,address=address,phone=phone,password=password)
        p.save()
        return redirect('login')
    return render(request, 'register.html')
# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            phone_num = loginForm.cleaned_data["phone"]
            pswd = loginForm.cleaned_data["password"]
            # user = authenticate(request, phone = phone_num, password= pswd)
            user = User.objects.filter( phone = phone_num , password= pswd)
            if user:
                request.session['password'] = pswd
                request.session['phone'] = phone_num
                return redirect('allBooks')
    else:
        loginForm = LoginForm()

    return render(request, "login.html", {"form": loginForm})


def sign_out(request):
    logout(request)
    return redirect('index')


def allBooks(request):
    password = request.session.get('password')
    phone = request.session.get('phone')
    if password and phone:
              user = User.objects.filter(password=password , phone=phone).first()
              if user:
                         age = (int)(date.today().year - (user.birth_date.year))
                         categories = Category.objects.filter(age_from__lte=age, age_until__gte=age)
                         if categories:
                             books = Book.objects.filter(category__in=categories)
                             data = {
                                 "books": books,
                                 "user":True
                             }
                         else:
                             books=[]
              else:
                    return redirect('login')

    else:
        books = Book.objects.all()
        data = {
            "books": books,
            "user": False

        }


    return render(request, 'allBooks.html', data)


def lend(request, b):
        password = request.session.get('password')
        phone = request.session.get('phone')

        if password and phone:
            user = User.objects.filter(password=password, phone=phone).first()
            if user:
                book = Book.objects.filter(id=b).first()
                if book:
                    category = Category.objects.filter(category_name=book.category.category_name).first()

                    during = date.today() + timedelta(days=book.category.lending_time)

                    borrowedBook = Barrowed_book(user_id=user, book_id=book, date_barrowed=date.today(),
                                                 date_required_return=during)
                    borrowedBook.save()
                    book.is_lend = True
                    book.save()

        return redirect('allBooks')

def showLending(request):
    password = request.session.get('password')
    phone = request.session.get('phone')

    if password and phone:
            user = User.objects.filter(password=password , phone=phone).first()
            if user:
                user_lends = Barrowed_book.objects.filter(user_id_id=user.pk)
            data = {
                "lending": user_lends,
                "user":user
            }

    return render(request, "lending.html", data)

def return_book(request, lend_id):
    lending = Barrowed_book.objects.filter(id=lend_id).first()
    # pdb.set_trace()

    lending.book_id.is_lend = False
    lending.book_id.save()
    Barrowed_book.objects.filter(id=lend_id).delete()

    return redirect('lending')

def reports(request):
    password = request.session.get('password')
    phone = request.session.get('phone')
    ifUser=False

    if password and phone:

              user = User.objects.filter(password=password , phone=phone).first()
              report_books = []
              if user:
                  if user.password == "s" and user.phone == "0":
                      lending=Barrowed_book.objects.all()

                  else:
                        lending=Barrowed_book.objects.filter(user_id_id=user.pk)

                  ifUser = True

                  report_books = []

                  for lend in lending:
                        if lend.date_required_return<date.today():
                            report_books.append(lend)
              else:
                  report_books=[]
                  ifUser = False

    else:
        report_books=[]

    data = {
        "report": report_books,
        "ifUserr": ifUser
    }

    return render(request, 'report.html', data)
