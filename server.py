from flask import jsonify, Flask, request
from Lantern_Controller import Lantern_Manager

app = Flask(__name__)
lantern_manager = Lantern_Manager()

@app.route('/changeLanternPattern', methods=['POST'])
def change__lantern():
    lantern_id = request.args.get("id")
    pattern = request.args.get("pattern")
    hex_color = request.args.get("hexColor")
    frequency = request.args.get("frequency")
    lantern_manager.handle_current_process(lantern_id, pattern, hex_color, frequency)
    return jsonify(status=200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)