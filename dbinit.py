from database.session import Base, engine
from models.bogie_checksheet import BogieChecksheet 

Base.metadata.create_all(bind=engine)
