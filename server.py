from flask import Flask

app = Flask(__name__)

@app.route('sendPattern', methods=['POST'])
def sendPattern():
    pass

if __name__ == '__main__':
    app.run()
