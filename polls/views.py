# views helps to manage and maintain web requests
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, Choice 
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse

from rest_framework.decorators import APIView 
from rest_framework.response import Response
from .serializers import QuestionsSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated



# views mae function/js logic rehta hae jisse browser ko info send karte hae 

#These are fn based views
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5] 
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id) 
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

    # return HttpResponse(template.render(context, request))

    # return HttpResponse("Hello, you are looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)  
    return render(request, "polls/result.html", {"question": question})


def vote(request, question_id):
    # extracted the question
    question = get_object_or_404(Questions, pk=question_id)  
    # now try to get the user choice id to get the poll_text done by them
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])  # Fixed typo
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html", 
            {
                "question": question,
                "error_message": "You did not select a choice",  
            },
        )
    else:
        selected_choice.votes = F("votes") + 1  
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))  
    

    #     <!-- 
    #     {% for choice in question.choice_set.all %} → Loops through all choices related to the question.
    # <input type="radio" name="choice" value="{{ choice.id }}"> → Creates a radio button for each choice.
    # forloop.counter → Generates unique IDs for each choice.
    # <label> → Connects the choice with the radio button.  -->



# These are class  based views


# funcition to get all the question 


# self ka matlab hai current instance of the class.
# Jab hum class-based views (APIView) use karte hain, toh self har function me required hota hai.
class QuestionsListAPIView(APIView):
    def get(self,request):
        question=Questions.objects.all()
        serializers=QuestionsSerializer(question,many=True)
        return Response(serializers.data)

# sara data manvaya ,questions se ,
# firr usko models channelise kiya throuht serialization for 
# sending it to json,

# support only get method
# APIView DRF ka ek class hai jo API requests handle karta hai.
# get() method me humne saare Question objects nikale.
# QuestionSerializer se models ka data JSON format me convert kiya.
# Response(serializer.data) se JSON data client ko bheja.


# This uses routere funtionality
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('id') 
    serializer_class=QuestionsSerializer
    permission_classes = [IsAuthenticated]  # ✅ Sirf login kiye hue users API use kar sakte hain

def questions_web_view(request):
    return render(request, 'polls/questions_web.html')  # ✅ API se data fetch karne ke liye frontend page