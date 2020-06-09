from partsML import get_prediction
from flask import Flask, render_template, request, redirect



app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def fileUpload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        image_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=image_bytes)
    return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == '__main__':
    app.run()





