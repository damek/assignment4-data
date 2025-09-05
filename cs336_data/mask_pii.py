def mask_email(text: str) -> str:
    new_string = text.split("@")[0]
    nb_masked = 0
    for char in new_string:
        if char == "@":
            nb_masked += 1
    return text.replace(text.split("@")[0], "|||EMAIL_ADDRESS|||"), nb_masked

