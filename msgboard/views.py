from django.shortcuts import render, redirect
from msgboard.models import Message
from msgboard.forms import MessageForm


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

def post_list(request):
   blog_list = ["article1 content1","article2 content2"]
   return render(request, 'msgboard/post_list.html', {
            'blog_list': blog_list})

