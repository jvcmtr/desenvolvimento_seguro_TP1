from typing import Optional
from sqlalchemy.orm import Session

from src.DAL.db_models.user_table import UserTable

# UM USUARIO ADMIN FOI CRIADO NO BANCO DE DADOS COM AS SEGUINTES CREDENCIAIS:
# username: "joaoramos"
# password: "joaoramosadminsenha123"


def find_by_username(db, username) -> Optional[UserTable]:
    return db.query(UserTable).filter(UserTable.username == username).first()


def create(db, username, password_hash, is_admin= True):
    user = UserTable(
        username=username,
        password=password_hash,
        is_admin=is_admin
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user