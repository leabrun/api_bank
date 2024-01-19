from django.shortcuts import render
from django.views import View
from .forms import TokenForm
from .parser import connect_token


class MainView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = TokenForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TokenForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            connect_token(request.user, token)

        return render(request, self.template_name, {'form': form})
