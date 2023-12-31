GLOSSARY = {
    "Призрака": "Ghost",
    "Стрелка": "Strelok",
    "Долг": "Duty",
    "Свобода": "Freedom",
    "Кишке": "Gut",
    "Меченный": "Marked One",
    "ПДА": "PDA",
    "выброса": "emission",
    "выброс": "blowout",
    "Мозговыжигатель": "Brain Scorcher",
    "Боеприпасы:": "Ammunition:",
}


def glossary_print():
    glossary_str = "GLOSSARY: "
    for key, val in GLOSSARY.items():
        glossary_str += f"{key} = {val}, "
    return glossary_str[:-2]
