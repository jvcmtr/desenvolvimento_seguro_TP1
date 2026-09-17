from typing import Optional, List
from sqlalchemy.orm import Session

from src.DAL.db_models.user_table import UserTable

# UM USUARIO ADMIN FOI CRIADO NO BANCO DE DADOS COM AS SEGUINTES CREDENCIAIS:
# username: "joaoramos"
# password: "joaoramosadminsenha123"

def get_all(db: Session) -> List[UserTable]:
    return db.query(UserTable).all()

def get_by_id(db: Session, user_id: int) -> Optional[UserTable]:
    return db.query(UserTable).filter(UserTable.id == user_id).first()

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