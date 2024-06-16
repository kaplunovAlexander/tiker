from flask import Flask, request, send_file
from generate import generate_video

app = Flask(__name__)

@app.route('/generate')
def generate():
    text = request.args.get('text', '')

    if not text:
        return "Text parameter is required", 400

    output_path = "output.mp4"
    try:
        generate_video(text)
    except Exception as e:
        return str(e), 500

    try:
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run()