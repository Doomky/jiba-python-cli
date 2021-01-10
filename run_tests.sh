#!/bin/bash

python -m venv .venv

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  .venv\\Scripts\\activate.bat
else
  source .venv/bin/activate
fi

python -m pip install -r requirements.txt
pytest ./tests/

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  .venv\\Scripts\\deactivate.bat
else
  deactivate
fi
