import openai
from django.http import JsonResponse
from django.views import View
from django.conf import settings


import requests
from .models import JejuTouristSpot

import logging

logger = logging.getLogger(__name__)

from rest_framework import generics
from .models import JejuTouristSpot
from .serializers import JejuTouristSpotSerializer

class JejuTouristSpotList(generics.ListAPIView):
    queryset = JejuTouristSpot.objects.all()
    serializer_class = JejuTouristSpotSerializer


class GPTPromptView(View):
    def get(self, request):
        
        location = request.GET.get('location', '제주도')
        days = int(request.GET.get('days', 2))  # 기본값을 2일로 설정

        # 데이터베이스에서 여행지 정보 가져오기
        tourist_spots = JejuTouristSpot.objects.all()[:]
        

     
        
        # 프롬프트 구성
        prompt = f"{location} 지역에 대한 {days}일간의 아이와 함께하는 여행지를 제안해주세요.\n"
        for spot in tourist_spots:
            prompt += f"- {spot.name} (주소: {spot.address}, 태그: {spot.tag})\n"

        prompt += "\n 여행 일정은 장소와 식당, 숙박시설의 이름만 아래 형식에 맞춰서 제공해주세요. spot에 없는 장소는 추천하지 마세요.\n"
        for day in range(1, days + 1):
            prompt += (
                f"Day {day}:\n\n"
                "오전: 장소\n\n"
                "점심: 식당\n\n"
                "오후: 장소\n\n"
                "저녁: 식당\n\n"
                "숙박: 숙박시설\n\n"
            )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "system", "content": "You are a helpful assistant. that You help me plan my trip to Jeju Island"},
                          {"role": "user", "content": prompt}],
               # max_tokens=128,000,  # 튜닝: 결과 길이 제한
               # temperature=0,  # 튜닝: 창의성 및 예측 가능성 조절
               # top_p=1,  # 튜닝: 상위 확률 분포 고려
               # frequency_penalty=1,  # 튜닝: 반복 감소
               # presence_penalty=0  # 튜닝: 독창성 증가
            )
            print(JsonResponse({'response': response['choices'][0]['message']['content']}))
            return JsonResponse({'response': response['choices'][0]['message']['content']})
       
           

        except Exception as e:
            logger.error(f"Error in GPTPromptView: {str(e)}")
            print(JsonResponse({'response': response['choices'][0]['message']['content']}))
            return JsonResponse({'error': str(e)}, status=500)
