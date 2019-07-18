from django.shortcuts import render,redirect,reverse
from .models import Board
from django.core.paginator import Paginator

# Create your views here.
def home (request):
       return render(request, 'mainsite/mainsite.html')

def newBoard(request):
    content={}
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            username = request.POST.get('username')
            contents = request.POST.get('contents')
            image = request.FILES['image']
            board = Board(
                title = title,
                username = username,
                contents = contents,
                image = image
                
            )
            board.save()
            content = {'board':board}
    except:
            error = "dd"
            content={'error':error}
            print("error")
    return redirect(reverse('list'))
    
def list(request):
    content = {}
    try:
        boards = Board.objects.all()
        paginator = Paginator(boards, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        
        content={'boards':boards, 'posts':posts}
    except:
        error = "오류"
        content ={'error':error}
    return render(request, 'mainsite/list.html', content)

def view(request,id):
    content ={}
    try:
        board = Board.objects.get(id = id)
        content = {'board':board}
    except:
        error = "error"
        content ={'error':error}
    return render(request, 'mainsite/view.html', content)

def updateDelete(request,id):
    contant={}
    if request.POST.get('updateDelete'):
        board = Board.objects.get(id=id)
        title = request.POST.get('title')
        username = request.POST.get('username')
        contents = request.POST.get('contents')

        board.title = title
        board.username = username
        board.contant = contant
        board.save()

        contant = {'board':board}
        return render(request, 'mainsite/view.html',contant)
    else:
        board = Board.objects.get(id=id)
        board.delete()

        return redirect('list')

def updatepage(request,id):
        board = Board.objects.get(id=id)
        contant = {'board':board}
        return render(request, 'mainsite/update.html', contant)