from flask import render_template, request, jsonify, send_file
from app import app
from app.forms import JSONForm
import json
import tempfile
import os

@app.route('/', methods=['GET', 'POST'])
def my_form():
    form = JSONForm()
    if request.method == 'POST':
        data = {
            'bot_type': request.form.get('bot_type'),
            'language': request.form.get('language'),
            'lesson_type': request.form.get('lesson_type'),
            'topic': request.form.get('topic'),
            'text': request.form.get('text'),
            'save_to_file': request.form.get('save_to_file'),
        }

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            json.dump(data, temp_file)
            temp_file_path = temp_file.name

        return send_file(temp_file_path, as_attachment=True, download_name='form_data.json')

        os.remove(temp_file_path)


    return render_template('index.html', form=form)