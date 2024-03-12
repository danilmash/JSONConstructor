# -*- coding: utf-8 -*-
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
            'role_or_task': request.form.get('role_or_task'),
            'lesson_type': request.form.get('lesson_type'),
            'topic_of_dialogue': request.form.get('topic_of_dialogue'),
            'text_for_questions': request.form.get('text_for_questions'),
            'save_lesson_to_file': request.form.get('save_lesson_to_file'),
        }

        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as temp_file:
            json.dump(data, temp_file, ensure_ascii=False)
            temp_file_path = temp_file.name

        if request.form.get('filename'):
            return send_file(temp_file_path, as_attachment=True, download_name='%s.json' % (request.form.get('filename')))
        else:
            return send_file(temp_file_path, as_attachment=True, download_name='form-data.json')



    return render_template('index.html', form=form)