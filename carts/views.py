from django.shortcuts import render

# Create your views here.
def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:  #and isinstance(cart_id, int):
        print("Create new cart")
        request.session['card_id'] = 12 #storing a session variable
        pass
    else:
        print("Cart ID exists")
    return render(request, "carts/home.html", {})