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
    #name_types = [x.strip() for x in request.form['name_types'].upper().split(sep=',')]
    name_types = request.form.getlist('name_types_checkbox')
    fictional_checkbox = request.form.getlist('fictional_checkbox')
    fictional = "FICTIONAL" in fictional_checkbox
    anonymized_text = text_anonymizer.anonymize(text, name_types=name_types, fictional = fictional)
    return render_template('form.html',
                           original_text = text,
                           anonymized_text = anonymized_text)


if __name__ == '__main__':
    app.run()