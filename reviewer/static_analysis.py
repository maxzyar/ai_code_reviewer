### File: reviewer/static_analysis.py

import subprocess
import tempfile


def run_static_analysis(filename, code):
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        result = subprocess.run(["flake8", tmp.name], capture_output=True, text=True)
    return result.stdout