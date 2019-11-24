from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

if __name__ == '__main__':
    app.run()

# conda info --envs (check available virtual environments)
# conda activate flaskenv
# conda deactivate flaskenv
## closing the server
# sudo lsof -i:5000
# kill XXXX
## Ref: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
