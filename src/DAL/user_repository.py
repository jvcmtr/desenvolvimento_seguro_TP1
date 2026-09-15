from src.models.user_model import User

# Mock de usuários. A senha é 'senha123'
usuarios_db = [
    User(
        id=1,
        username="joaoramos",
        # Hash bcrypt gerado para "joaoramosadminsenha123"
        # Para gerar um hash execute: `python3 src/tools/create_hash.py`
        password="$2b$12$Y0edcI2jzFufKRnEvwaXQuXVGMlHAg5zRvK58rVsyJOy3M0.y9LTS",
        is_admin=True
    )
]

def find_by_username(username: str):
    result = [x for x in usuarios_db if x.username == username]
    if len(result) < 1 : return None
    return result[0]