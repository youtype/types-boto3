#!/usr/bin/env python
"""
Update docstrings in stub files.

Copyright 2024 Vlad Emelianov
"""

import argparse
import datetime
import logging
from dataclasses import dataclass
from pathlib import Path

AUTHOR_NAME = "Vlad Emelianov"
YEAR = datetime.datetime.now().year
LOGGER_NAME = "docstrings"


def print_path(path: Path) -> str:
    """
    Get path as a string relative to current workdir.
    """
    if path.is_absolute():
        cwd = Path.cwd()
        if path == cwd or path.parts <= cwd.parts:
            return path.as_posix()

        try:
            path = path.relative_to(cwd)
        except ValueError:
            return str(path)

    if len(path.parts) == 1:
        return f"./{path.as_posix()}"

    return path.as_posix()


@dataclass
class CLINamespace:
    """
    CLI arguments.
    """

    path: Path
    dry_run: bool


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument(
        "-p",
        "--path",
        type=Path,
        default=Path.cwd(),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
    )
    args = parser.parse_args()
    return CLINamespace(
        path=args.path,
        dry_run=args.dry_run,
    )


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Returns:
        Overriden Logger.
    """

    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(name)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S"
    )
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


def extract_docstring(content: str) -> str:
    """
    Extract docstring from PYI content.
    """
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
    """
    Get author from docstring.
    """
    for line in docstring.splitlines():
        if line.startswith("Copyright"):
            return line.split(" ", 2)[-1]

    return AUTHOR_NAME


def get_module_str(library_name: str, pyi_path: Path) -> str:
    """
    Get module import string.
    """
    result = [library_name, *pyi_path.parts[:-1]]
    if pyi_path.stem != "__init__":
        result.append(pyi_path.stem)

    return ".".join(result)


def create_docstring(author: str, library_name: str, pyi_path: Path) -> str:
    """
    Create new docstring.
    """
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
    """
    Main function.
    """
    args = parse_args()
    setup_logging(logging.INFO)
    logger = logging.getLogger(LOGGER_NAME)
    for stubs_path in args.path.iterdir():
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
                if not args.dry_run:
                    pyi_path.write_text(new_pyi_content)
                logger.info(f"Updated {print_path(pyi_path)}")


if __name__ == "__main__":
    main()
