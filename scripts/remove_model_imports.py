from pathlib import Path
import re

for path in Path('backend/app/models').glob('*.py'):
    text = path.read_text(encoding='utf-8')
    new_text = re.sub(r'^from backend\.app\.models\.[a-zA-Z0-9_]+ import .*\n', '', text, flags=re.M)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')

print('removed eager cross-model imports from backend/app/models')
