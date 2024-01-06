from typing import Optional


def print_dict_as_prompt(dict_raw: dict, prefix: Optional[str] = None):
    prompt: str = prefix
    for key, val in dict_raw.items():
        prompt += f"{key} = {val}, "
    return prompt[:-2] + "\n"
