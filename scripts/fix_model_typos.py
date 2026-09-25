from pathlib import Path
import re

for path in Path('backend/app/models').glob('*.py'):
    text = path.read_text(encoding='utf-8')

    # collapse duplicate SQLAlchemy keyword arguments caused by generated model stubs
    text = text.replace('unique=True, index=True, unique=True, nullable=False', 'unique=True, index=True, nullable=False')
    text = text.replace('unique=True, unique=True', 'unique=True')

    # repair broken FK targets from the models generated in the route experiment
    text = text.replace('mapped_column(ForeignKey("teacher.id"))', 'mapped_column(ForeignKey("teachers.id"))')
    text = text.replace('mapped_column(ForeignKey("subject.id"))', 'mapped_column(ForeignKey("subjects.id"))')

    # repair relation target type typo from generated skeleton
    text = text.replace('payment: Mapped["Invoice"] = relationship(back_populates="student")', 'payment: Mapped["Payment"] = relationship(back_populates="student")')

    # keep the file consistent regardless of model-level stub generation
    text = re.sub(r'\bMapped\[\"Invoice\"\]\s*=\s*relationship\(back_populates="student"\)', 'payment: Mapped["Payment"] = relationship(back_populates="student")', text)

    path.write_text(text, encoding='utf-8')

print('model typo normalization script applied')
