
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'

with open(DATA_DIR / 'torymps.json', 'r') as f:
	toryMpsJson = json.loads(f.read())

with open(DATA_DIR / 'payroll-vote.json', 'r') as f:
	payrollVote = json.loads(f.read())

