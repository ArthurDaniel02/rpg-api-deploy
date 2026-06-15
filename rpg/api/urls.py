from django.urls import path
from . import views

urlpatterns = [
    # 1. CONTA
    path('conta/', views.conta_list, name='conta_list'),
    path('conta/<int:pk>/', views.conta_detail, name='conta_detail'),
    path('conta/login/', views.conta_login, name='conta_login'),
    
    # 2. PESSOA
    path('pessoa/', views.pessoa_list, name='pessoa_list'),
    path('pessoa/<int:pk>/', views.pessoa_detail, name='pessoa_detail'),
    
    # 3. ALUNO
    path('aluno/', views.aluno_list, name='aluno_list'),
    path('aluno/<int:pk>/', views.aluno_detail, name='aluno_detail'),
    path('aluno/comprar/', views.aluno_comprar, name='aluno_comprar'),
    path('aluno/<int:pk>/itens/', views.aluno_itens),
    
    # 4. PROFESSOR
    path('professor/', views.professor_list, name='professor_list'),
    path('professor/<int:pk>/', views.professor_detail, name='professor_detail'),
    path('professor/<int:pk>/disciplinas/', views.professor_disciplinas),
    
    # 5. PERSONAGEM
    path('personagem/', views.personagem_list, name='personagem_list'),
    path('personagem/<int:pk>/', views.personagem_detail, name='personagem_detail'),
    
    # 6. DISCIPLINA
    path('disciplina/', views.disciplina_list, name='disciplina_list'),
    path('disciplina/<int:pk>/', views.disciplina_detail, name='disciplina_detail'),
    path('disciplina/matricular/', views.disciplina_matricular, name='disciplina_matricular'),
    path('disciplina/<int:pk>/alunos/', views.disciplina_alunos),
    
    # 7. QUESTS
    path('quests/', views.quests_list, name='quests_list'),
    path('quests/<int:pk>/', views.quests_detail, name='quests_detail'),
    path('quests/responder/', views.quests_responder, name='quests_responder'),
    
    # 8. ITEM
    path('item/', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
]