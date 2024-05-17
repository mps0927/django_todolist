from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

#내가 저장한 메모들을 뜨게 할 메인메뉴이자 메모장
def index(request):
    items = Todo.objects.all() #db에 있는 내용 전부 items에 넣기
    print("From DB:", items) #쉘에서 확인할 수 있음
    content = {'items' : items}
    return render(request, "ToDoList/index.html", content)

#메모 추가하기
def create(request):
    input_content = request.POST['todoContent'] #입력을 받으면 받은 str값 저장
    new_content = Todo(content = input_content )
    new_content.save() #db에 저장
    return HttpResponseRedirect(reverse('index')) #인덱스로 돌아가기
#메모 DB에서 삭제하기
def delete(request):
    item_Num = request.GET['todoNum'] #완료 버튼을 누른 아이템의 번호를 가져옴
    print('삭제한 todo의 id', item_Num)
    todo = Todo.objects.get(id = item_Num)#DB에서 삭제함
    todo.delete()
    return HttpResponseRedirect(reverse('index'))#인덱스로 돌아가기