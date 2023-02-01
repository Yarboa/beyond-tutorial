from django.shortcuts import render, redirect
from msgboard.models import Message
from msgboard.forms import MessageForm
from django.contrib.auth.decorators import login_required


#@login_required(login_url='/accounts/login/')
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
    #blog_list = ["article1 content1", "article2, content2"]

    blog_list = [ 
       {'subject':'Blog1 Title', 'content':'BlogContent1', 'date':'Dec 7, 2017'},
       {'subject':'Blog2 Title', 'content':'BlogContent2', 'date':'Jul 17, 2019'},
       ]   
    return render(request, 'msgboard/post_list.html', {
        'blog_list': blog_list})


