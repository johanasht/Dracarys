from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import  HttpResponseRedirect, JsonResponse
from django.urls import reverse
from user_auth.forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('user_auth:login')  
    context = {'form':form}
    if request.user.is_authenticated :
        return redirect("recommended:show_page")
    else :
        return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get("next")
            if next_page is None:
                response = redirect("recommended:show_page")
            else:
                response = redirect(next_page)
            response.set_cookie("user_logged_in", user)
            return response
        else:
            messages.info(
                request, "Sorry, incorrect username or password. Please try again.")
    context = {}
    if request.user.is_authenticated:
        return redirect('recommended:show_page')
    else:
        return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('recommended:show_page'))
    return response

@csrf_exempt
def login_flutter (request) :
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "id": user.id,
                "type": user.userprofile.user_type,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    

@csrf_exempt
def logout_flutter(request):
    username = request.user.username
    try:
        logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)