
def tagVerify(tags_expected, tags_actual):
    for tag in tags_actual:
        if tag in tags_expected:
            return True
    return False
