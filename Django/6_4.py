# views.py
from django.shortcuts import render
from django.views.decorator.http import require_http_methods


# POST method로 들어온 입력만 받겠다.
@require_POST()
def delete(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    chatting.delete()
    return redirect("chattings:index")

# GET method로 들어온 입력만 받겠다.
# GET보다는 safe를 사용하는 것이 바람직함.
@require_safe()
def detail(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    context = {
        'chatting':chatting,
    }
    return render(request,'chattings/detail.html',context)


# GET이랑 POST method로 들어온 입력만 받겠다.
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST,request.FILES)
        if form.is_valid:
            chatting = form.save()
            return redirect('chattings:detail',chatting.pk)
    else:
        form = ChatForm()
    context={
        'form':form
    }
    return render(request,'chattings/create.html',context)
