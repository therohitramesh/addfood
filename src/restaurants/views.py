import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
# def home(request):
#     html_var = 'f strings'
#     html_ = f"""<!DOCTYPE html>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>Hello World!</h1>
#     <p>Dis is {html_var} cmng thru</p>
#     </body>
#     </html>
#     """
#     #f strings
#     return HttpResponse(html_)
#     #return render(request, "home.html", {})#response

def home(request):
    num = random.randint(0,1000)
    return render(request, "base.html", {"html_var" : "context variable", "num" : num})
