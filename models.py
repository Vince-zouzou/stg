from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class FAQ:
    similarity: int
    question: str
    date: str
    customer: str
    status: str
    stg: str
    image: Optional[str | List[str]]
    questions: str

@dataclass
class EQ:
    id: str
    eqStatus: str
    prodData: str
    paste: str
    last: str
    changed: str
    pn: str
    techClass: str
    spe: str
    customer: str
    endCustomer: str
    customerPN: str
    project: str
    factory: str
    selected: bool
    image: str

@dataclass
class TranslationResult:
    source_text: str
    translated_text: str
    source_lang: str
    target_lang: str