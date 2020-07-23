from fastapi import APIRouter
from GenderClassifier import GenderClassifier
from starlette.responses import JSONResponse,PlainTextResponse

router = APIRouter()


@router.post('/predict_gender')
def predict_gender(gender_questions: dict):
    gender_classifier = GenderClassifier()
    # json_res = JSONResponse(gender_classifier.gender_predict(gender_questions))
    text_res = PlainTextResponse(gender_classifier.gender_predict(gender_questions))
    return text_res
