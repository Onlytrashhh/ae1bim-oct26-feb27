"""Consulta con or_(): obtiene consultorios de Dermatología o Cirugía."""

from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Consultorio, engine


def consultar_consultorios_or():
    """Lista consultorios cuya especialidad sea Dermatología o Cirugía."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        consultorios = (
            session.query(Consultorio)
            .filter(
                or_(
                    Consultorio.especialidad == "Dermatología",
                    Consultorio.especialidad == "Cirugía",
                )
            )
            .all()
        )

        print("=== Consultorios de Dermatología o Cirugía (uso de or_) ===")
        for consultorio in consultorios:
            print(
                f"Consultorio: {consultorio.nombre_numero} | "
                f"Especialidad: {consultorio.especialidad} | "
                f"Clínica: {consultorio.clinica.nombre_comercial}"
            )
    finally:
        session.close()


if __name__ == "__main__":
    consultar_consultorios_or()