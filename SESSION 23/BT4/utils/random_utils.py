import random
import string


def generate_assignment_code():

    code = "".join(
        random.choices(
            string.ascii_uppercase +
            string.digits,
            k=4
        )
    )

    return f"PY-{code}"