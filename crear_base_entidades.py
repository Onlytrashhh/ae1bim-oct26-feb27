"""Definición de entidades ORM con SQLAlchemy y creación de la base de datos."""

from sqlalchemy import Column, Date, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=False)
Base = declarative_base()


class Clinica(Base):
    """Representa una clínica veterinaria de la red."""

    __tablename__ = "clinica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_comercial = Column(String(150), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(150), nullable=False)

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"Clinica(id={self.id}, nombre_comercial='{self.nombre_comercial}', "
            f"direccion='{self.direccion}', "
            f"veterinario_responsable='{self.veterinario_responsable}')"
        )


class Consultorio(Base):
    """Representa un consultorio perteneciente obligatoriamente a una clínica."""

    __tablename__ = "consultorio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_numero = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinica.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"Consultorio(id={self.id}, nombre_numero='{self.nombre_numero}', "
            f"especialidad='{self.especialidad}', clinica_id={self.clinica_id})"
        )


class Veterinario(Base):
    """Representa un médico veterinario asignado a un único consultorio."""

    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    numero_licencia = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey("consultorio.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica",
        back_populates="veterinario",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"Veterinario(id={self.id}, nombres='{self.nombres}', "
            f"apellidos='{self.apellidos}', correo='{self.correo}', "
            f"numero_licencia='{self.numero_licencia}', "
            f"consultorio_id={self.consultorio_id})"
        )


class HistoriaClinica(Base):
    """Representa una historia clínica elaborada obligatoriamente por un veterinario."""

    __tablename__ = "historia_clinica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(250), nullable=False)
    tratamiento = Column(String(300), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinario.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return (
            f"HistoriaClinica(id={self.id}, fecha_atencion={self.fecha_atencion}, "
            f"nombre_mascota='{self.nombre_mascota}', "
            f"diagnostico='{self.diagnostico}', "
            f"veterinario_id={self.veterinario_id})"
        )


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")