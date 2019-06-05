from django.db import models

#Create your models here.
class Meeting(models.Model):
    objects = models.Manager()

    category = models.CharField(max_length=200) # 카테고리
    title = models.CharField(max_length=200) # 제목
    writer = models.CharField(max_length=200) # 개설자
    min_number = models.IntegerField() # 최소인원수
    max_number = models.IntegerField() # 최대인원수
    current_number = models.IntegerField(default=0) # 현재인원수
    meeting_time = models.CharField(max_length=200) # 시간
    meeting_place = models.CharField(max_length=200) # 장소
    description = models.TextField() # 설명
    writer_email = models.CharField(max_length=200) # 개설자 이메일
    password = models.CharField(max_length=200) # 비밀번호

    view_count = models.IntegerField(default=0) # 조회수

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Meeting의 key를 갖고있는 Participant를 불러온다
    # def participant(self):
    #     return Participant.objects.filter(meeting=self)


class Participant(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=200) # 참가자 이름
    email = models.CharField(max_length=200) # 참가자 이메일
    school = models.CharField(max_length=200) # 참가자 소속학교
    motive = models.TextField() # 참여동기
    
    meeting_category = models.CharField(max_length=200)
    meeting_title = models.CharField(max_length=200)
    meeting_writer = models.CharField(max_length=200)
    
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    # meetings = models.ManyToManyField(Meeting)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Board(models.Model):
    objects = models.Manager()
    
    text = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)