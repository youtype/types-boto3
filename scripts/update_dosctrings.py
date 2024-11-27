#!/usr/bin/env python
"""
Update docstrings in stub files.

Copyright 2024 Vlad Emelianov
"""

import datetime
from pathlib import Path

AUTHOR_NAME = "Vlad Emelianov"
YEAR = datetime.datetime.now().year


def extract_docstring(content: str) -> str:
    result: list[str] = []
    docstring_found = False
    for line in content.splitlines():
        line = line.strip()
        if line == '"""':
            if docstring_found:
                result.append(line)
                return "\n".join(result)
            else:
                docstring_found = True

        if docstring_found:
            result.append(line)

    return ""


def get_author(docstring: str) -> str:
    for line in docstring.splitlines():
        if line.startswith("Copyright"):
            return line.split(" ", 2)[-1]

    return AUTHOR_NAME


def get_module_str(library_name: str, pyi_path: Path) -> str:
    result = [library_name, *pyi_path.parts[:-1]]
    if pyi_path.stem != "__init__":
        result.append(pyi_path.stem)

    return ".".join(result)


def create_docstring(author: str, library_name: str, pyi_path: Path) -> str:
    module_str = get_module_str(library_name, pyi_path)
    return "\n".join(
        (
            '"""',
            f"Type annotations for {module_str} module.",
            "",
            f"Copyright {YEAR} {author}",
            '"""',
        )
    )


def main() -> None:
    work_path = Path.cwd()
    for stubs_path in work_path.iterdir():
        if not stubs_path.is_dir() or not stubs_path.name.endswith("-stubs"):
            continue

        library_name = stubs_path.name.split("-")[0]
        for pyi_path in stubs_path.glob("**/*.pyi"):
            if not pyi_path.is_file() or not pyi_path.name.endswith(".pyi"):
                continue

            pyi_content = pyi_path.read_text()
            if not pyi_content.strip():
                continue
            current_docstring = extract_docstring(pyi_content)
            author = get_author(current_docstring)
            new_docstring = create_docstring(author, library_name, pyi_path.relative_to(stubs_path))
            if current_docstring:
                new_pyi_content = pyi_content.replace(current_docstring, new_docstring)
            else:
                new_pyi_content = f"{new_docstring}\n\n{pyi_content}"
            if pyi_content != new_pyi_content:
                pyi_path.write_text(new_pyi_content)
                print(f"Updated {pyi_path.relative_to(work_path)}")


if __name__ == "__main__":
    main()
