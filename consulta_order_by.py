"""Consulta con order_by(): ordena historias clínicas por fecha de atención descendente."""

from sqlalchemy.orm import sessionmaker

from crear_base_entidades import HistoriaClinica, engine


def consultar_historias_ordenadas():
    """Lista las historias clínicas ordenadas de la más reciente a la más antigua."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        historias = (
            session.query(HistoriaClinica)
            .order_by(HistoriaClinica.fecha_atencion.desc())
            .all()
        )

        print("=== Historias Clínicas ordenadas por fecha descendente (uso de order_by) ===")
        for historia in historias:
            vet = historia.veterinario
            print(
                f"Fecha: {historia.fecha_atencion} | "
                f"Mascota: {historia.nombre_mascota} | "
                f"Diagnóstico: {historia.diagnostico} | "
                f"Veterinario: {vet.nombres} {vet.apellidos}"
            )
    finally:
        session.close()


if __name__ == "__main__":
    consultar_historias_ordenadas()