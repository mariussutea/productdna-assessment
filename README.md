## Installation

1. Install **uv**

`wget -qO- https://astral.sh/uv/install.sh | sh`

For systems other than Linux/MacOS, check install instructions [here](https://docs.astral.sh/uv/getting-started/installation/)

2. Install the required dependencies

`uv install`

3. Change to the `src` directory

`cd src`

4. Run the Django migrations

`uv run python manage.py migrate`

5. Create a django superuser for testing (input a username and a password when prompted)

`uv run python manage.py createsuperuser`

5. Run the server

`uv run python manage.py runserver`
