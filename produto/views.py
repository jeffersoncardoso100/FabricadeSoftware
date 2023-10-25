from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Contato
# Importe a função send_mail
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils import timezone
# ...

def salvar_contato(request):
    mensagem_enviada = False

    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')
        data_envio = request.POST.get('data_envio', None)  # Obtenha a data e hora do formulário

        try:
            if data_envio:
                data_envio = timezone.datetime.strptime(data_envio, '%Y-%m-%dT%H:%M')
            else:
                data_envio = timezone.now()

            contato = Contato(nome=nome, email=email, mensagem=mensagem, data_envio=data_envio)
            contato.save()

            subject = 'Nova Mensagem do SITE'
            message = f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}'
            from_email = 'jeffguitarrista1@gmail.com'
            recipient_list = ['jeffguitarrista1@gmail.com']

            send_mail(subject, message, from_email, recipient_list)

            mensagem_enviada = True
        except Exception as e:
            print(f"Erro ao salvar o contato: {e}")

    # Restante do código...


    return render(request, 'home.html', {'mensagem_enviada': mensagem_enviada})



from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_superuser)
def listar_contatos(request):
    # Retrieve all contacts from the database
    contatos = Contato.objects.all()

    # Pass the list of contacts to the template
    return render(request, 'listar.html', {'contatos': contatos})
