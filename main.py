from tinydb import TinyDB
from fastapi import FastAPI, Request
from utils import parse_template_data, find_matching_template, guess_field_types

db = TinyDB("./database/forms.json")
app = FastAPI()

templates = db.all()


@app.post("/get_form")
async def get_form(request: Request):
    query = await request.json()
    template_name = find_matching_template(query, templates)
    if template_name:
        return {"template_name": template_name}
    else:
        field_types = guess_field_types(query)
        return field_types


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)

