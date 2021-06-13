from flask import Flask
app = Flask(__name__)


@app.route('/')
def demo():
    return 'This is a sample application for ct devops project updated!\n'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


