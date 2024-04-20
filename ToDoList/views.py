from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

#내가 저장한 메모들을 뜨게 할 메인메뉴이자 메모장
def index(request):
    items = Todo.objects.all() #db에 있는 내용 전부 items에 넣기
    print("From DB:", items)
    content = {'items' : items}
    return render(request, "ToDoList/index.html", content)


def create(request):
    input_content = request.POST['todoContent'] #입력을 받으면 받은 str값 저장
    new_content = Todo(content = input_content )
    new_content.save() #db에 저장
    return HttpResponseRedirect(reverse('index'))
    
def delete(request):
    item_Num = request.GET['todoNum']
    print('삭제한 todo의 id', item_Num)
    todo = Todo.objects.get(id = item_Num)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))