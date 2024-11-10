from django.shortcuts import render, redirect 
from .forms import UserRegister, LoginForm
from .models import User

# Псевдо-список существующих пользователей
users = ['user1', 'user2', 'user3']

def choice_page(request):
    return render(request, 'fifth_task/choice_page.html')

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif User.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Создание нового пользователя
                user = User(username=username, password=password, age=age)
                user.save()
                # Перенаправление на страницу входа с сообщением об успешной регистрации
                return redirect('login')
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif User.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Создание нового пользователя
                user = User(username=username, password=password, age=age)
                user.save()
                # Перенаправление на страницу входа с сообщением об успешной регистрации
                return redirect('login')
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})

def login_view(request):
    success_message = request.GET.get('success_message')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user is not None:
                # Перенаправление на страницу успешного входа
                return render(request, 'fifth_task/login_success.html', {'username': username})
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()

    return render(request, 'fifth_task/login_page.html', {'form': form, 'success_message': success_message})