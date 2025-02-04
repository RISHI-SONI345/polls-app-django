from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet
from .views import questions_web_view

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'polls'  


router=DefaultRouter()
router.register(r'questions',QuestionViewSet)




urlpatterns=[
    path("",views.index,name= "index"),
    path('<int:question_id>/',views.detail,name='details'),
    path('<int:question_id>/result/',views.results,name='result'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    
    # for new api get endpoint defining the url
    # path('api/questions',views.QuestionsListAPIView.as_view(),name='question_list'),
    path('api/',include(router.urls)),
    path('questions/web/', questions_web_view, name='questions_web'),  # ✅ Web page for paginated questions

    #  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ JWT Token Generate
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ✅ JWT Token Refresh
]



#here we save the model.py changes in the 
#managable file named migration which manupluate the db without actual query