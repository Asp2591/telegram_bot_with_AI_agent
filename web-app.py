import os
from flask import Flask, render_template, request
from pathlib import Path
from phi.agent import Agent
from phi.model.google import Gemini

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# AI Agent setup
image_text_agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=False,
    structured_outputs=True,
    parse_response=True,
)

# Store last uploaded image
last_uploaded_image = None

@app.route("/", methods=["GET", "POST"])
def home():
    global last_uploaded_image
    analysis_result = None
    user_question = None

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename:
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(file_path)
                last_uploaded_image = file.filename  # Store last uploaded image

        elif "question" in request.form and last_uploaded_image:
            user_question = request.form["question"]
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], last_uploaded_image)
            try:
                response = image_text_agent.run(
                    f"You are given an image. Answer this question based on the image: {user_question}",
                    images=[image_path]
                ).content
                analysis_result = response
            except Exception as e:
                analysis_result = f"Error analyzing image: {str(e)}"

    return render_template("index.html", image=last_uploaded_image, analysis=analysis_result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
