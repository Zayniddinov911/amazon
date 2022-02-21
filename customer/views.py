from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.utils.translation import gettext_lazy as _
from .form import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate


class CreateAccountView(View):
    # template_name = 'main/registration.html'

    def setup(self, request, *args, **kwargs):
        super(CreateAccountView, self).setup(request, *args, **kwargs)
        request.save_button = _('Continue')
        request.title = _('Create Account')

    def get(self, request):
        return render(request, 'customer/registration.html', context={
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=self.request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('')
        return render(request, 'customer/registration.html', context={
            'form': form
        })


class LoginView(View):

    def setup(self, request, *args, **kwargs):
        super(LoginView, self).setup(request, *args, **kwargs)

        request.title = 'Sign-In'

    def get(self, request):
        return render(request, 'customer/login.html', context={
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if not user is None:
                login(request, user)

                form.add_error('password', 'Incorrect Login or Password!')
            return render(request, 'customer/login.html', context={
                'form': form
            })


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('acc:login')