from django.db import models

class Conta(models.Model):
    TIPO_CONTA_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]
    login = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo_conta = models.CharField(
        max_length=20, 
        choices=TIPO_CONTA_CHOICES, 
        default='aluno' 
    )

    class Meta:
        db_table = 'conta'

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'pessoa'



class Professor(Pessoa):

    class Meta:
        db_table = 'professor'

class Item(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    descricao = models.TextField()

    class Meta:
        db_table = 'item'
        
class Aluno(Pessoa):
    moedas = models.IntegerField(default=0)
    itens = models.ManyToManyField(Item, related_name='alunos', blank=True)
    class Meta:
        db_table = 'aluno'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    alunos = models.ManyToManyField(Aluno, related_name='disciplinas')

    class Meta:
        db_table = 'disciplina'

class Quests(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    alternativa_a = models.CharField(max_length=255, default="")
    alternativa_b = models.CharField(max_length=255, default="")
    alternativa_c = models.CharField(max_length=255, default="")
    alternativa_d = models.CharField(max_length=255, default="")
    recompensa = models.IntegerField(default=50)
    resposta_correta = models.CharField(max_length=1) 
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        db_table = 'quests'

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'personagem'

class Guerreiro(Personagem):
    forca = models.IntegerField()

    class Meta:
        db_table = 'guerreiro'

class Mago(Personagem):
    inteligencia = models.IntegerField()

    class Meta:
        db_table = 'mago'

class Arqueiro(Personagem):
    destreza = models.IntegerField()

    class Meta:
        db_table = 'arqueiro'