from flask import Flask, request, jsonify
import os
import Final_Black_Out    # You must create this function

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join("uploads", filename)

    # Save file to server
    file.save(file_path)

    # Run your OCR + Gemini + Redaction
    output = process_file(file_path)

    return jsonify({
        "status": "success",
        "message": "File processed successfully",
        "output_files": output
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
