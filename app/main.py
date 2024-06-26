from fastapi import FastAPI
from .schemas import TextRequest
from .nltk_utils import tokenize_text, pos_tag_text, ner_text

app = FastAPI()


@app.post("/tokenize")
def tokenize(request: TextRequest):
    tokens = tokenize_text(request.text)
    return {"tokens": tokens}


@app.post("/pos_tag")
def pos_tag(request: TextRequest):
    pos_tags = pos_tag_text(request.text)
    return {"pos_tags": pos_tags}


@app.post("/ner")
def ner(request: TextRequest):
    entities = ner_text(request.text)
    return {"entities": entities}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
