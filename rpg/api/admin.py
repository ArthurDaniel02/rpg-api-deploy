from django.contrib import admin
from .models import (
    Conta, 
    Pessoa, 
    Aluno, 
    Professor, 
    Item, 
    Disciplina, 
    Quests,  
    Personagem, 
    Guerreiro, 
    Mago, 
    Arqueiro
)


admin.site.register(Conta)
admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Item)
admin.site.register(Disciplina)
admin.site.register(Quests)
admin.site.register(Personagem)
admin.site.register(Guerreiro)
admin.site.register(Mago)
admin.site.register(Arqueiro)