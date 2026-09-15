from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

password = input("Senha: ")
hashed = pwd_context.hash(password)

print("\nHash:")
print('"' + hashed + '"')
joaoramosadminsenha123