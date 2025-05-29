from dice_roller.cli import main, engine
from dice_roller.models import Base


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

main()

