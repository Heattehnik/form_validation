from tinydb import TinyDB
from fastapi import FastAPI
from utils import parse_template_data, find_matching_template, guess_field_types

db = TinyDB("./database/forms.json")
app = FastAPI()

templates = db.all()


@app.post("/get_form")
async def get_form(template_data: str):
    template_data = parse_template_data(template_data)
    template_name = find_matching_template(template_data, templates)
    if template_name:
        return {"template_name": template_name}
    else:
        field_types = guess_field_types(template_data)
        return field_types


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=80,
    )
