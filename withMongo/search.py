from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from models import User, Address

engine = create_engine("sqlite:///db_with_mongo.sqlite")

with Session(engine) as session:
    # Verificando os dados persistidos
    stmt = select(User).where(User.name.in_(['philipe', 'mike']))
    for user in session.scalars(stmt):
        print(user)
    print("=========================================")

    # Inner Join para obter todos os endereços com seus respectivos usuários
    stmt_two = select(Address).join(Address.user)
    for address in session.scalars(stmt_two):
        print(f"Address: {address.email_address}, User: {address.user.name}")
    print("=========================================")

    # Contar o número de endereços por usuário
    stmt_three = select(User.name, func.count(Address.id)).join(User.address).group_by(User.name)
    for name, address_count in session.execute(stmt_three):
        print(f"User: {name}, Number of addresses: {address_count}")
    print("=========================================")

    # Selecionar usuários com mais de um endereço
    stmt_four = select(User).join(User.address).group_by(User.id).having(func.count(Address.id) > 1)
    for user in session.scalars(stmt_four):
        print(f"User: {user.name}, Number of addresses: {len(user.address)}")
    print("=========================================")

    # Selecionar endereços de um usuário específico
    stmt_five = select(Address).join(Address.user).where(User.name == 'philipe')
    for address in session.scalars(stmt_five):
        print(f"Address: {address.email_address}, User: {address.user.name}")
    print("=========================================")

    # Inner Join detalhado para obter informações completas
    stmt_six = select(User, Address).join(Address.user)
    for user, address in session.execute(stmt_six):
        print(f"User: {user.name} ({user.fullname}), Address: {address.email_address}")
    print("=========================================")

    # Left Outer Join para obter endereços sem usuário
    stmt_seven = select(Address).outerjoin(Address.user).where(User.id.is_(None))
    for address in session.scalars(stmt_seven):
        print(f"Address without user: {address.email_address}")
