from django.shortcuts import render
from django.views import View
from .forms import TokenForm
from .tasks import connect_token_async


class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        form = TokenForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TokenForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            connect_token_async.delay(request.user.id, token)

        return render(request, self.template_name, {'form': form})
