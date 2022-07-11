from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        # 화면에서 입력한 데이터로 사용자를 생성함.
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # form.cleaned_data.get: 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용함.
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 신규 사용자를 생성한 후에 자동 로그인이 될 수 있도록
            # authenticate: 사용자 인증을 담당(사용자명과 비밀번호가 정확한지 검증)
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login: 로그인(사용자 세션을 생성)
            login(request, user)  # 로그인
            return redirect('dsl_app/')
    else:
        # 회원가입 화면을 보여줌.
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# @login_required: 로그인이 필요한 함수
# request.user는 현재 로그인한 계정의 User 모델 객체