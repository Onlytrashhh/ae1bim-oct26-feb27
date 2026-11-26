"""Consulta con filter(): filtra consultorios por especialidad principal."""

from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Consultorio, engine


def consultar_consultorios_cirugia():
    """Obtiene los consultorios cuya especialidad principal es Cirugía."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        consultorios = (
            session.query(Consultorio)
            .filter(Consultorio.especialidad == "Cirugía")
            .all()
        )

        print("=== Consultorios de Cirugía (uso de filter) ===")
        for consultorio in consultorios:
            print(
                f"Consultorio: {consultorio.nombre_numero} | "
                f"Especialidad: {consultorio.especialidad} | "
                f"Clínica: {consultorio.clinica.nombre_comercial}"
            )
    finally:
        session.close()


if __name__ == "__main__":
    consultar_consultorios_cirugia()