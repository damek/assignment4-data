def mask_email(text: str) -> str:
    new_string = text.split("@")[0]
    # need to replace string before and after @ with a single ||| EMAIL_ADDRESS |||
    # So you @ me.com or @someone@me.com or @someone@me.com@someone@me.com becomes
    # |||EMAIL_ADDRESS|||
    new_string = new_string.replace("@", "|||EMAIL_ADDRESS|||")
    text = text.replace(text.split("@")[0], new_string)
    text = text.replace(text.split("@")[1], new_string)

    nb_masked = 0
    for char in new_string:
        if char == "@":
            nb_masked += 1
    return text, nb_masked

