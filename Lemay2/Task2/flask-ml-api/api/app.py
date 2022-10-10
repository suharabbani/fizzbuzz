from flask import Flask, jsonify, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import json

app = Flask(__name__)  # define app using Flask

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)

@app.route("/classification", methods=['GET'])
def classification():
    args = request.args   
    sample = args.get("text", type=str)
    print(sample)
    #sample = json.loads(request.data)["text"]
    return jsonify(str(pipe(sample)))

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'It works! '})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
