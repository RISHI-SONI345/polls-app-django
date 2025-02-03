# views helps to manage and maintain web requests
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, Choice 
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse

# views mae function/js logic rehta hae jisse browser ko info send karte hae 

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
