from django.shortcuts import render

# Create your views here.
def cart_home(request):
    print("!!!!!!!!!!!! S T A R T !!!!!!!!!!!")
    #print(request.session) # on the request
    #print(dir(request.session))
    #key = request.session.session_key
    #print(key)
    request.session['card_id'] = 12 #storing a session variable
    return render(request, "carts/home.html", {})