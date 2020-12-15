from django.shortcuts import render, redirect
from msgboard.models import Message
from msgboard.forms import MessageForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def board(request):
    messages = Message.objects.order_by('-date')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board')
    else:
        form = MessageForm()
        return render(request, 'msgboard/board.html', {
            'messages': messages, 'form': form, })


def landing(request):
    return render(request, 'msgboard/landing.html')
