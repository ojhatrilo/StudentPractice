from django.urls import path
from . import views

urlpatterns = [
    path('agent-list-plain/', views.AgentListPlainView.as_view(), name='agent-list-plain'),
    path('agent-list-encrypted/', views.AgentListEncryptedView.as_view(), name='agent-list-encrypted'),
    path('decrypt-agent-list/', views.DecryptAgentList.as_view(), name='decrypt-agent-list')
]