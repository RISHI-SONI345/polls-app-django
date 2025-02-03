from django.urls import path
from . import views

app_name = 'polls'  

urlpatterns=[
    path("",views.index,name= "index"),
    path('<int:question_id>/',views.detail,name='details'),
    path('<int:question_id>/result/',views.results,name='result'),
    path('<int:question_id>/vote/',views.vote,name='vote')
]

#here we save the model.py changes in the 
#managable file named migration which manupluate the db without actual query