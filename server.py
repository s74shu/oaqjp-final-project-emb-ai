from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

def emotion_dom(result):
    res = 0
    emo = ''

    for k, v in result.items():
        if v > res:
            emo = k
            res = v

    return emo

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emo = emotion_dom(response)

    return f"For the given statement, the system response is {response}. The dominant emotion is {emo}."  


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

