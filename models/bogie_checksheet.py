from sqlalchemy import Column, String, Date, Text
from database.session import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_forms"

    formNumber = Column(String, primary_key=True, index=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)

    # Bogie Details
    bogieNo = Column(String)
    makerYearBuilt = Column(String)
    incomingDivAndDate = Column(String)
    deficitComponents = Column(String)
    dateOfIOH = Column(Date)

    # Bogie Checksheet
    bogieFrameCondition = Column(String)
    bolster = Column(String)
    bolsterSuspensionBracket = Column(String)
    lowerSpringSeat = Column(String)
    axleGuide = Column(String)

    # BMBC Checksheet
    cylinderBody = Column(String)
    pistonTrunnion = Column(String)
    adjustingTube = Column(String)
    plungerSpring = Column(String)
