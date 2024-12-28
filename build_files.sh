pip install -r requirements.txt
# python3.13 manage.py collectstatic

#!/bin/bash
# echo "Collecting static files"
# python3 manage.py collectstatic --noinput
# echo "Build complete"

#!/bin/bash
echo "Collecting static files"
python3 manage.py collectstatic --noinput
echo "Build complete"
