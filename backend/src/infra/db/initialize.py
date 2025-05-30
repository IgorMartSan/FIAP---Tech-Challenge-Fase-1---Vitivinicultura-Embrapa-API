from sqlalchemy.exc import OperationalError
from infra.db.database import Base, engine, SessionLocal
from infra.db.models import User
from utils.auth import AuthUtils


def create_database():
    """Cria todas as tabelas do banco de dados."""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Banco de dados verificado/criado")
    except OperationalError as e:
        print(f"❌ Erro ao conectar/criar banco: {e}")


def create_admin_user():
    """Cria um usuário admin padrão se não existir."""
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.user_type == "admin").first()

        if not admin:
            admin_user = User(
                username="admin",
                email="admin@example.com",
                hashed_password=AuthUtils.get_password_hash("automate123."),
                is_active=True,
                user_type="admin"
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print(f"✅ Usuário admin criado: {admin_user.email}")
        else:
            print(f"ℹ️ Usuário admin já existe: {admin.email}")
    except Exception as e:
        print(f"❌ Erro ao criar usuário admin: {e}")
    finally:
        db.close()


def initialize():
    """Executa os processos de inicialização: criar banco e admin."""
    create_database()
    create_admin_user()
