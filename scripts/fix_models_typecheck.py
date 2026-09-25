from pathlib import Path
import re

model_dir = Path('g:/Projets/EGest/backend/app/models')
files = sorted(model_dir.glob('*.py'))

class_to_file = {}
for f in files:
    text = f.read_text(encoding='utf-8')
    for match in re.finditer(r'^class\s+([A-Za-z0-9_]+)\(Base\):', text, flags=re.M):
        class_to_file[match.group(1)] = f.stem

for f in files:
    text = f.read_text(encoding='utf-8')
    # Only string references that appear in a Mapped[...] annotation in the file
    refs = set(re.findall(r'Mapped\["([A-Za-z0-9_]+)"\]', text))
    # Keep only cross-file references, and avoid re-importing the same file.
    imports = []
    for cls in sorted(refs):
        if cls in class_to_file and class_to_file[cls] != f.stem:
            imports.append(f'from backend.app.models.{class_to_file[cls]} import {cls}')

    if not imports:
        continue

    # Ensure there is a TYPE_CHECKING import header at the top
    lines = text.splitlines()
    # Keep runtime imports before TYPE_CHECKING block
    # Find first class definition line and insert the TYPE_CHECKING block before it.
    insert_line = 0
    for idx, line in enumerate(lines):
        if line.startswith('class '):
            insert_line = idx
            break

    # Prepare new TYPE_CHECKING block
    type_block = []
    type_block.append('from typing import TYPE_CHECKING')
    type_block.append('')
    type_block.append('if TYPE_CHECKING:')
    for imp in imports:
        type_block.append(f'    {imp}')
    type_block.append('')

    # Add block only once.
    if 'if TYPE_CHECKING:' not in text:
        lines = lines[:insert_line] + type_block + lines[insert_line:]
        f.write_text('\n'.join(lines) + '\n', encoding='utf-8')

print(f'normalized type-checking imports across {len(files)} model files')
