sudo python3 -m pip install virtualenv
echo "Creating virtual environment..."
environment= venv
virtualenv -p python3 venv
echo "Activating virtual environment..."
. venv/bin/activate
echo "$environment Virual environment activated..."