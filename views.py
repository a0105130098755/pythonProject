from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import TouristAttraction, Visit
from django.contrib.auth.decorators import login_required
from .forms import VisitForm  # 가정: 방문 기록을 위한 폼

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('attraction_list')  # 관광 명소 목록 페이지로 리다이렉트
        else:
            # 로그인 실패 메시지 처리
            return render(request, 'login.html', {'error': '사용자 이름 또는 비밀번호가 잘못되었습니다.'})
    else:
        return render(request, 'login.html')

@login_required
def attraction_list(request):
    attractions = TouristAttraction.objects.all()
    return render(request, 'attractions/list.html', {'attractions': attractions})

@login_required
def add_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.user = request.user
            visit.save()
            return redirect('attraction_list')
    else:
        form = VisitForm()
    return render(request, 'visits/add.html', {'form': form})
