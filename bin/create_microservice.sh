$name = $1

mkdir ./services/$name
mkdir ./services/$name/db
mkdir ./services/$name/models
mkdir ./services/$name/schemas
touch ./services/$name/app.py
touch ./services/$name/__init__.py
cp requirements.txt ./services/$name/requirements.txt