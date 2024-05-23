

from django.shortcuts import render




# from library.applibrary.forms import LoginForm

# def welcome(request):
#     loginForm = LoginForm()
    # return render(request, 'login.html', {"form": loginForm})
def welcome(request):
    return render(request, 'index.html')