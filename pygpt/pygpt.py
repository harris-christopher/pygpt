from pathlib import Path
from io import TextIOWrapper

from openai import OpenAI

from pygpt.glossary import glossary_print


class PyGPT:
    def __init__(self, infile: Path, line_start: int, outfile: Path):
        self.infile = infile
        self.outfile = outfile

        self.client = OpenAI()
        self.cursor_in: TextIOWrapper = open(self.infile, "r", encoding="utf-8")
        self.cursor_out: TextIOWrapper = open(self.outfile, "a", encoding="utf-8")

        self.static_system_prompt = (
            "Translate Russian to English.\n"
            "Do not modify strings starting with REPL_\n"
            "Keep the formatting identical to the prompt.\n"
            + glossary_print()
        )

        self.line_to_process = line_start

        # Seek to line offset
        print(f"Seeking to LineNo: {line_start}")
        for idx in range(self.line_to_process - 1):
            self.cursor_in.readline()
        print("Seeking complete.")

    def process_file(self):
        print(f"Processing LineNo: {self.line_to_process}")
        self.process_line()

    def process_line(self):
        line_raw = self.cursor_in.readline()
        print(f"RAW: {line_raw}")

        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": self.static_system_prompt},
                {"role": "user", "content": line_raw},
            ]
        )

        line_translate = response.choices[0].message.content
        print(f"TRANSLATE: {line_translate}")

        self.cursor_out.writelines(line_translate)
