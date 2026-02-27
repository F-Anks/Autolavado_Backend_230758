from sqlalchemy import Column, Integer, String, Boolean, DateTime, event
from sqlalchemy.orm import relationship
from config.db import Base
import datetime

class Rol(Base):
    __tablename__ = "tbc_roles"

    Id = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String(15))
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    usuarios = relationship("Usuario", back_populates="rols")

# --- Lógica para insertar el primer rol automáticamente ---
@event.listens_for(Rol.__table__, 'after_create')
def insert_initial_values(target, connection, **kw):
    now = datetime.datetime.now()
    connection.execute(
        target.insert().values(
            Id=1,
            nombre_rol="Admin",
            estado=True,
            fecha_registro=now,
            fecha_actualizacion=now
        )
    )