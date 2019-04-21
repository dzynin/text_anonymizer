from flask import Flask, request, render_template
import text_anonymizer

app = Flask(__name__)

@app.route('/')
def my_form():
    print('rendering template ...')
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    anonymized_text = text_anonymizer.anonymize_placeholder(text)
    return render_template('form.html',
                           original_text = text,
                           anonymized_text = anonymized_text)


if __name__ == '__main__':
    app.run()