from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.bogie_checksheet import BogieChecksheet
from schemas.bogie_checksheet import BogieChecksheetCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/bogie-checksheet")
def create_bogie_form(form: BogieChecksheetCreate, db: Session = Depends(get_db)):
    # Check for duplicate formNumber
    if db.query(BogieChecksheet).filter_by(formNumber=form.formNumber).first():
        raise HTTPException(status_code=400, detail="Form already exists.")

    new_form = BogieChecksheet(
        formNumber=form.formNumber,
        inspectionBy=form.inspectionBy,
        inspectionDate=form.inspectionDate,

        # Bogie Details
        bogieNo=form.bogieDetails.bogieNo,
        makerYearBuilt=form.bogieDetails.makerYearBuilt,
        incomingDivAndDate=form.bogieDetails.incomingDivAndDate,
        deficitComponents=form.bogieDetails.deficitComponents,
        dateOfIOH=form.bogieDetails.dateOfIOH,

        # Bogie Checksheet
        bogieFrameCondition=form.bogieChecksheet.bogieFrameCondition,
        bolster=form.bogieChecksheet.bolster,
        bolsterSuspensionBracket=form.bogieChecksheet.bolsterSuspensionBracket,
        lowerSpringSeat=form.bogieChecksheet.lowerSpringSeat,
        axleGuide=form.bogieChecksheet.axleGuide,

        # BMBC Checksheet
        cylinderBody=form.bmbcChecksheet.cylinderBody,
        pistonTrunnion=form.bmbcChecksheet.pistonTrunnion,
        adjustingTube=form.bmbcChecksheet.adjustingTube,
        plungerSpring=form.bmbcChecksheet.plungerSpring
    )

    db.add(new_form)
    db.commit()

    return {
        "success": True,
        "message": "Bogie checksheet submitted successfully.",
        "data": {
            "formNumber": form.formNumber,
            "inspectionBy": form.inspectionBy,
            "inspectionDate": form.inspectionDate,
            "status": "Saved"
        }
    }
