from validators import is_valid_date, is_valid_phone, is_valid_email


def find_matching_template(data, templates):
    matching_template = None
    for template in templates:
        template_fields = set(template["fields"].keys()) - {"name"}
        template_types = set(template["fields"].values())
        data_fields = set(data.keys())
        field_types = set(guess_field_types(data).values())
        common_fields = template_fields.intersection(data_fields)
        if (
            common_fields == template_fields
            and template_types.intersection(field_types) == template_types
        ):
            matching_template = template["name"]
            break
    return matching_template


def guess_field_types(data_dict):
    field_types = {}
    for key, value in data_dict.items():
        if is_valid_date(value):
            field_types[key] = "date"
        elif is_valid_phone(value):
            field_types[key] = "phone"
        elif is_valid_email(value):
            field_types[key] = "email"
        else:
            field_types[key] = "text"
    return field_types
