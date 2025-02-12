from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

# API endpoint to process the emotion detection
@app.route('/emotionDetector')
def sent_detector():
    # Get the text input from the form or JS
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass text and store response
    response = emotion_detector(text_to_analyze)

    # Formatting the response
    formatted_emotions = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']}, and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

    # Check if the dominant emotion is None (invalid text input or API error)
    if response['dominant_emotion'] is None:
        # If dominant_emotion is None, return an error message in the same format
        formatted_emotions = "Invalid text! Please try again."

    # Return the formatted string
    return formatted_emotions, 200

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4012)
