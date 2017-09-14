from django.conf.urls import include, url
from messenger.views import MessengerBotView
app_name='messenger'
urlpatterns = [

	url(r'^6c4f95e373457e49f7708163f068b546392fd1e4a2c75d67f7/?$', MessengerBotView.as_view()) 
]

	
