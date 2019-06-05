from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting, Participant, Board

# Create your views here.
# 모임 개설
def create(request):
    if request.method == "POST":
        category = request.POST.get('category')
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        min_number = request.POST.get('min_number')
        max_number = request.POST.get('max_number')
        meeting_time = request.POST.get('meeting_time')
        meeting_place = request.POST.get('meeting_place')
        description = request.POST.get('description')
        writer_email = request.POST.get('writer_email')
        password = request.POST.get('password')
        
        meeting = Meeting(category = category, title = title, writer = writer, min_number = min_number, max_number = max_number, meeting_time = meeting_time, meeting_place = meeting_place, description = description, writer_email = writer_email, password=password)
        meeting.save()
        return redirect('meetings:list')
        
    return render(request, 'meetings/create.html')


# 모임 목록
def list(request):
    meetings = Meeting.objects.all().order_by('-id')
    return render(request, 'meetings/list.html', {'meetings': meetings})
    
# 모임 참여 페이지로 넘어가는 것 - id 받아서 다시 넘겨야 함
def join_page(request, id):
    meeting = Meeting.objects.get(pk=id)
    title = meeting.title
    return render(request, 'meetings/join.html', {'meeting':meeting})
    # return render(request, 'meetings/join.html', {'title': title})
    # title을 보내면 다시 meeting의 id를 보내야해서 객체를 바로보낼께용
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# 모임 참여 신청
def join(request, id):
    if request.method == "POST":
        meeting = Meeting.objects.get(pk=id)
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        school = request.POST.get('school')
        motive = request.POST.get('motive')
        meeting_category = meeting.category
        meeting_title = meeting.title
        meeting_writer = meeting.writer
        participant = Participant(name=name, email=email, school=school, motive=motive, meeting_category=meeting_category, meeting_title=meeting_title, meeting_writer=meeting_writer, meeting=meeting)
        participant.save()
        
        current_num = meeting.current_number
        meeting.current_number = current_num + 1
        meeting.save()
        
        # participant.meetings.add(meeting)
        return redirect('meetings:list')
        

# 모임 수정 페이지 띄우기
def edit(request, id):
        meeting = get_object_or_404(Meeting, pk=id)
        return render(request, 'meetings/edit.html', {'meeting':meeting})


# 모임 수정
def update(request, id):
    if request.method == "POST":
        meeting = get_object_or_404(Meeting, pk=id)
        category = request.POST.get('category')
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        min_number = request.POST.get('min_number')
        max_number = request.POST.get('max_number')
        meeting_time = request.POST.get('meeting_time')
        meeting_place = request.POST.get('meeting_place')
        description = request.POST.get('description')
        writer_email = request.POST.get('writer_email')

        meeting.category = category
        meeting.title = title
        meeting.writer = writer
        meeting.min_number = min_number
        meeting.max_number = max_number
        meeting.meeting_time = meeting_time
        meeting.meeting_place = meeting_place
        meeting.description = description
        meeting.writer_email = writer_email

        meeting.save()

        return redirect('meetings:read', meeting.pk)

# 모임 삭제하기
def delete(request, id):
    meeting = Meeting.objects.get(pk=id)
    meeting.delete()
    return redirect('meetings:list')
        
        
# 모임 상세보기
def read(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    default_view_count = meeting.view_count
    meeting.view_count = default_view_count + 1
    meeting.save()
    return render(request, 'meetings/read.html', {'meeting': meeting})


#fail
def fail(request):
    return render(request, 'meetings/fail.html')

# 비밀번호 입력 창
def verification(request):
    return render(request, 'meetings/verification.html')
    
# 참가자 목록
def participants(request, id):
    meeting = Meeting.objects.get(pk=id)
    title = meeting.title
    participants = Participant.objects.all().filter(meeting=meeting)
    return render(request, 'meetings/participants.html', {'participants':participants, 'title': title})
    
# 내가 신청한 모임 누르면 email치는 html로 넘어가는 함수
# def show(request):
#     return render(request, 'meetings/joined_meetings.html')

# 참여한 목록 확인
def joined_meetings(request):
    if request.method == "POST":
        input_email = request.POST.get('email')
        participant = Participant.objects.filter(email=input_email)
        return render(request, 'meetings/my_list.html', {'participant': participant, 'email': input_email})
    return render(request, 'meetings/joined_meetings.html')
    
# 검색하기   
def search(request):
    search = request.GET.get('search')
    search_result = Meeting.objects.filter(title__contains=search)
    
    return render(request, 'meetings/search_result.html', {'search_result': search_result, 'search_keyword': search})


# 비밀번호 체크
def check_pwd(request):
    id = request.POST.get('id')
    meeting = get_object_or_404(Meeting, pk=id)
    
    pwd = request.POST.get('password')
    
    if pwd == meeting.password:
        if request.POST.get('action') == "show_participants":
            
            return redirect('meetings:participants', id)
            
        if request.POST.get('action') == "edit":
            return redirect('meetings:edit', id)
        
        else:
            return redirect('meetings:delete', id)
            
    else:
        return redirect('meetings:fail')
        
# 개설요청 페이지
def board(request):
    print(request.method)
    if request.method == "POST":
        text = request.POST.get('text')
        Board(text=text).save()
        return redirect('meetings:board')
    boards = Board.objects.all().order_by('-id')
    return render(request, 'meetings/board.html', {'boards': boards})