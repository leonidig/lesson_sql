from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


engine = create_engine("sqlite://", echo=True)


class Base(DeclarativeBase):
    unit_id: Mapped[int] = mapped_column(primary_key=True)


#OUR MODELS
class Human(Base):
    __tablename__ = "humans"
    name: Mapped[str] = mapped_column(String(30), unique=True)
    def __repr__(self) -> str:
        return f"<Human: {self.name}"


# ~ OUR MODELS
Base.metadata.create_all(engine)

indictator = True

with Session(engine) as session:
    batman = Human(name="Batman")
    session.add(batman)
    session.flush()
    batman2 = Human(name="Batman")
    if session.scalars(select(Human).where(Human.name == batman2.name)).one():
        session.rollback()
    else:
        session.add(batman2)
        session.flush()
    zorro = Human(name = "Zorro")
    session.add(zorro)
    session.commit()
    print(f"{session.scalars(select(Human)).all()=}")
