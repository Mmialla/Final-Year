from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
          return render(request, 'senti/index.html')
def admincontacts(request):
          return render(request, 'senti/admincontacts.html')          
def adminprofile(request):
          return render(request, 'senti/adminprofile.html')
def adminstrator(request):
          return render(request, 'senti/adminstrator.html')
def adminuseraccounts(request):
          return render(request, 'senti/adminuseraccounts.html')
def bursar(request):
          return render(request, 'senti/bursar.html')
def bursaraccounts(request):
          return render(request, 'senti/bursaraccounts.html')
def bursarcontacts(request):
          return render(request, 'senti/bursarcontacts.html')
def bursarprofile(request):
          return render(request, 'senti/bursarprofile.html')
def login(request):
          return render(request, 'senti/login.html')
def contact(request):
          return render(request, 'senti/pages-contact.html')
def resetPwd(request):
          return render(request, 'senti/resetPwd.html')
def skcontact(request):
          return render(request, 'senti/sk-pages-contact.html')
def skdashboard(request):
          return render(request, 'senti/admin-skDashboard.html')
def skaccounts(request):
          return render(request, 'senti/sk-user-accounts.html')
def skdashboard(request):
          return render(request, 'senti/skDashboard.html')
def useraccounts(request):
          return render(request, 'senti/user-accounts.html')
def userprofile(request):
          return render(request, 'senti/users-profile.html')
def createaccount(request):
          return render(request, 'senti/createAccount.html')
def demo(request):
          return render(request, 'senti/demo.html')
