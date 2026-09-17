import os
from src.DAL.database import Base, engine, Session, DB_PATH
from src.DAL.db_models.eventos_table import EventoTable
from src.DAL.db_models.user_table import UserTable
from src.tools.create_hash import hash_pass

def _get_user_and_password():
    skip = input("Deseja utilizar o usuario padrão 'joaoramos'? (y/n)").lower()
    if skip == 'y':
        # SENHA: "joaoramosadminsenha123"
        return "joaoramos", "$2b$12$Y0edcI2jzFufKRnEvwaXQuXVGMlHAg5zRvK58rVsyJOy3M0.y9LTS"

    username = input("Digite o nome do usuario admin: ").strip()
    password = input(f"Digite a senha para o usuario '{username}': ")
    password2 = input(f"Confirme sua senha: ")

    if len(username < 3):
        print("ERRO: nome de usuario deve conter pelo menos 3 caracteres")
        raise "USUARIO ADMIN COM ERRO"

    if len(password < 3):
        print("ERRO: senha deve conter pelo menos 3 caracteres")
        raise "USUARIO ADMIN COM ERRO"

    if password != password2:
        print("ERRO: As senhas fornescidas não são identicas")
        raise "USUARIO ADMIN COM ERRO"
    
    return username, hash_pass(password)

def _create_admin(username, password):
    db = Session()
    try:
        admin_user = UserTable(
            username=username,
            password=password,
            is_admin=True
        )
        db.add(admin_user)
        db.commit()
        print(f"+ usuário admin '{username}' criado")
    except Exception as e:
        print(f"+ Ocorreu um erro na criação de usuario: {e}")
    finally:
        db.close()

def _create_new_db_file():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    Base.metadata.create_all(bind=engine)

def init_db():

    try:
        username, password = _get_user_and_password()
        _create_new_db_file()
        _create_admin(username, password)

    except Exception as e:
        print(f"+ Ocorreu um erro na criação do banco: {e}")
