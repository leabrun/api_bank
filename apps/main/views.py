from django.shortcuts import render
from django.views import View
from .forms import TokenForm


class MainView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = TokenForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TokenForm(request.POST)
        if form.is_valid():
            pass

        return render(request, self.template_name, {'form': form})
