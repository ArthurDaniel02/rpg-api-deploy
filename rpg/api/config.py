import importlib

CONFIG = {
    'IContaDAO': 'api.persistence.ContaDAO_Mysql.ContaDAOMysql',
    'IPessoaDAO': 'api.persistence.PessoaDAO_Mysql.PessoaDAOMysql',
    'IAlunoDAO': 'api.persistence.AlunoDAO_Mysql.AlunoDAOMysql',
    'IProfessorDAO': 'api.persistence.ProfessorDAO_Mysql.ProfessorDAOMysql',
    
    'IPersonagemDAO': 'api.persistence.PersonagemDAO_Mysql.PersonagemDAOMysql',
    'IGuerreiroDAO': 'api.persistence.GuerreiroDAO_Mysql.GuerreiroDAOMysql',
    'IMagoDAO': 'api.persistence.MagoDAO_Mysql.MagoDAOMysql',
    'IArqueiroDAO': 'api.persistence.ArqueiroDAO_Mysql.ArqueiroDAOMysql',
    
    'IDisciplinaDAO': 'api.persistence.DisciplinaDAO_Mysql.DisciplinaDAOMysql',
    'IQuestsDAO': 'api.persistence.QuestsDAO_Mysql.QuestsDAOMysql',
    'IItemDAO': 'api.persistence.ItemDAO_Mysql.ItemDAOMysql',

    'IContaController': 'api.controllers.ContaController.ContaControllerImpl',
    'IPessoaController': 'api.controllers.PessoaController.PessoaControllerImpl',
    'IAlunoController': 'api.controllers.AlunoController.AlunoControllerImpl',
    'IProfessorController': 'api.controllers.ProfessorController.ProfessorControllerImpl',
    
    'IPersonagemController': 'api.controllers.PersonagemController.PersonagemControllerImpl',
    'IGuerreiroController': 'api.controllers.GuerreiroController.GuerreiroControllerImpl',
    'IMagoController': 'api.controllers.MagoController.MagoControllerImpl',
    'IArqueiroController': 'api.controllers.ArqueiroController.ArqueiroControllerImpl',
    
    'IDisciplinaController': 'api.controllers.DisciplinaController.DisciplinaControllerImpl',
    'IQuestsController': 'api.controllers.QuestsController.QuestsControllerImpl',
    'IItemController': 'api.controllers.ItemController.ItemControllerImpl',
}

def inject(interface_name: str, dao_instance=None): 
    if interface_name not in CONFIG:
        raise ValueError(f"Interface {interface_name} não mapeada no config.py")

    class_path = CONFIG[interface_name]
    module_path, class_name = class_path.rsplit('.', 1)

    modulo = importlib.import_module(module_path)
    classe = getattr(modulo, class_name)

    if dao_instance:
        return classe(dao_instance)
    return classe()