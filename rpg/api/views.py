import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from .config import inject

# --- SCHEMAS ---
conta_schema = {"application/json": {"type": "object", "properties": {"login": {"type": "string"}, "senha": {"type": "string"}, "email": {"type": "string"}, "tipo_conta": {"type": "string", "enum": ["aluno", "professor"]}}}}
pessoa_schema = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "cpf": {"type": "string"}, "conta_id": {"type": "integer"}}}}
aluno_schema = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "cpf": {"type": "string"}, "moedas": {"type": "integer"}, "conta_id": {"type": "integer"}}}}
professor_schema = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "cpf": {"type": "string"}, "conta_id": {"type": "integer"}}}}
personagem_schema_create = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "classe": {"type": "string", "enum": ["Mago", "Guerreiro", "Arqueiro"]}, "aluno_id": {"type": "integer"}}}}
personagem_schema_update = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "nivel": {"type": "integer"}, "aluno_id": {"type": "integer"}}}}
disciplina_schema = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "codigo": {"type": "string"}, "professor_id": {"type": "integer"}}}}
quest_schema = {"application/json": {"type": "object", "properties": {"titulo": {"type": "string"}, "descricao": {"type": "string"}, "alternativa_a": {"type": "string"}, "alternativa_b": {"type": "string"}, "alternativa_c": {"type": "string"}, "alternativa_d": {"type": "string"}, "resposta_correta": {"type": "string", "enum": ["A", "B", "C", "D"]}, "recompensa": {"type": "integer"}, "disciplina_id": {"type": "integer"}}}}
item_schema = {"application/json": {"type": "object", "properties": {"nome": {"type": "string"}, "preco": {"type": "integer"}, "descricao": {"type": "string"}}}}

# ==========================================
# 1. CONTA
# ==========================================
@extend_schema(summary="Listar/Criar Contas", tags=['Contas'], request=conta_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def conta_list(request):
    dao = inject('IContaDAO')
    ctrl = inject('IContaController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Conta", tags=['Contas'], request=conta_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def conta_detail(request, pk):
    dao = inject('IContaDAO')
    ctrl = inject('IContaController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Realizar Login", tags=['Contas'], request={"application/json": {"type": "object", "properties": {"email": {"type": "string"}, "senha": {"type": "string"}}}})
@api_view(['POST'])
@csrf_exempt
def conta_login(request):
    dao = inject('IContaDAO')
    ctrl = inject('IContaController', dao_instance=dao)
    res = ctrl.realizarLogin(request)
    return JsonResponse(res['data'], status=res['status'])

# ==========================================
# 2. PESSOA
# ==========================================
@extend_schema(summary="Listar/Criar Pessoas", tags=['Pessoas'], request=pessoa_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def pessoa_list(request):
    dao = inject('IPessoaDAO')
    ctrl = inject('IPessoaController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Pessoa", tags=['Pessoas'], request=pessoa_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def pessoa_detail(request, pk):
    dao = inject('IPessoaDAO')
    ctrl = inject('IPessoaController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)

# ==========================================
# 3. ALUNO
# ==========================================
@extend_schema(summary="Listar/Criar Alunos", tags=['Alunos'], request=aluno_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def aluno_list(request):
    dao = inject('IAlunoDAO')
    ctrl = inject('IAlunoController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Aluno", tags=['Alunos'], request=aluno_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def aluno_detail(request, pk):
    dao = inject('IAlunoDAO')
    ctrl = inject('IAlunoController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Comprar Item", tags=['Alunos'], request={"application/json": {"type": "object", "properties": {"aluno_id": {"type": "integer"}, "item_id": {"type": "integer"}}}})
@api_view(['POST'])
@csrf_exempt
def aluno_comprar(request):
    dao_a = inject('IAlunoDAO')
    dao_i = inject('IItemDAO')
    ctrl = inject('IAlunoController', dao_instance=dao_a)
    ctrl._item_dao = dao_i
    res = ctrl.comprarItem(request)
    return JsonResponse(res['data'], status=res['status'])
@extend_schema(summary="Itens do Aluno", tags=['Alunos'])
@api_view(['GET'])
@csrf_exempt
def aluno_itens(request, pk):
    dao = inject('IAlunoDAO')
    ctrl = inject('IAlunoController', dao_instance=dao)
    res = ctrl.consultarItens(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)
# ==========================================
# 4. PROFESSOR
# ==========================================
@extend_schema(summary="Listar/Criar Professores", tags=['Professores'], request=professor_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def professor_list(request):
    dao = inject('IProfessorDAO')
    ctrl = inject('IProfessorController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Professor", tags=['Professores'], request=professor_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def professor_detail(request, pk):
    dao = inject('IProfessorDAO')
    ctrl = inject('IProfessorController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)
@extend_schema(summary="Disciplinas do Professor", tags=['Professores'])
@api_view(['GET'])
@csrf_exempt
def professor_disciplinas(request, pk):
    dao = inject('IProfessorDAO')
    ctrl = inject('IProfessorController', dao_instance=dao)
    res = ctrl.consultarDisciplinas(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)
# ==========================================
# 5. PERSONAGEM
# ==========================================
@extend_schema(summary="Listar/Criar Personagens", tags=['Personagens'], request=personagem_schema_create)
@api_view(['GET', 'POST'])
@csrf_exempt
def personagem_list(request):
    dao = inject('IPersonagemDAO')
    ctrl = inject('IPersonagemController', dao_instance=dao)
    
    ctrl._mago_dao = inject('IMagoDAO')
    ctrl._guerreiro_dao = inject('IGuerreiroDAO')
    ctrl._arqueiro_dao = inject('IArqueiroDAO')
    
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Personagem", tags=['Personagens'], request=personagem_schema_update)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def personagem_detail(request, pk):
    dao = inject('IPersonagemDAO')
    ctrl = inject('IPersonagemController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)

# ==========================================
# 6. DISCIPLINA
# ==========================================
@extend_schema(summary="Listar/Criar Disciplinas", tags=['Disciplinas'], request=disciplina_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def disciplina_list(request):
    dao = inject('IDisciplinaDAO')
    ctrl = inject('IDisciplinaController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Disciplina", tags=['Disciplinas'], request=disciplina_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def disciplina_detail(request, pk):
    dao = inject('IDisciplinaDAO')
    ctrl = inject('IDisciplinaController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Matricular Aluno", tags=['Disciplinas'], request={"application/json": {"type": "object", "properties": {"aluno_id": {"type": "integer"}, "disciplina_id": {"type": "integer"}}}})
@api_view(['POST'])
@csrf_exempt
def disciplina_matricular(request):
    dao = inject('IDisciplinaDAO')
    ctrl = inject('IDisciplinaController', dao_instance=dao)
    res = ctrl.matricularAluno(request)
    return JsonResponse(res['data'], status=res['status'])
@extend_schema(summary="Alunos da Disciplina", tags=['Disciplinas'])
@api_view(['GET'])
@csrf_exempt
def disciplina_alunos(request, pk):
    dao = inject('IDisciplinaDAO')
    ctrl = inject('IDisciplinaController', dao_instance=dao)
    res = ctrl.consultarAlunos(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)
# ==========================================
# 7. QUESTS
# ==========================================
@extend_schema(summary="Listar/Criar Quests", tags=['Quests'], request=quest_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def quests_list(request):
    dao = inject('IQuestsDAO')
    ctrl = inject('IQuestsController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Quest", tags=['Quests'], request=quest_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def quests_detail(request, pk):
    dao = inject('IQuestsDAO')
    ctrl = inject('IQuestsController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Responder Quest", tags=['Quests'], request={"application/json": {"type": "object", "properties": {"quest_id": {"type": "integer"}, "aluno_id": {"type": "integer"}, "resposta": {"type": "string"}}}})
@api_view(['POST'])
@csrf_exempt
def quests_responder(request):
    dao = inject('IQuestsDAO')
    ctrl = inject('IQuestsController', dao_instance=dao)
    ctrl._aluno_dao = inject('IAlunoDAO')
    res = ctrl.responderQuest(request)
    return JsonResponse(res['data'], status=res['status'])

# ==========================================
# 8. ITEM
# ==========================================
@extend_schema(summary="Listar/Criar Itens", tags=['Itens'], request=item_schema)
@api_view(['GET', 'POST'])
@csrf_exempt
def item_list(request):
    dao = inject('IItemDAO')
    ctrl = inject('IItemController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@extend_schema(summary="Detalhes Item", tags=['Itens'], request=item_schema)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def item_detail(request, pk):
    dao = inject('IItemDAO')
    ctrl = inject('IItemController', dao_instance=dao)
    if request.method == 'PUT': res = ctrl.alterar(request, pk)
    elif request.method == 'DELETE': res = ctrl.deletar(request, pk)
    else: res = ctrl.consultarbyId(request, pk)
    return JsonResponse(res['data'], status=res['status'], safe=False)