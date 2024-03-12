# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, TextAreaField
from wtforms import validators

class JSONForm(FlaskForm):
    bot_type = SelectField('Тип бота', choices=[('chat_gpt', 'ChatGPT'), ('yandex_gpt', 'YandexGPT')], validators=[validators.DataRequired()])
    
    role_or_task = SelectField('Изучаемый язык', 
                            choices=[('Представь что ты преподаватель английского языка, а я твой ученик', 'English'), 
                                    ('Представь что ты преподаватель немецкого языка, а я твой ученик', 'German')], 
                            validators=[validators.DataRequired()]) 
    
    lesson_type = SelectField('Тип уроки', choices=[('Диалог на определённую тему','Диалог на определённую тему'), 
                                                    ('Проверка слов на определённую тему', 'Проверка слов на определённую тему')], 
                                        validators=[validators.DataRequired()])
    
    topic_of_dialogue = TextAreaField('Тема урока')
    text_for_questions = TextAreaField('Текст для ответов на вопросы')
    save_lesson_to_file = BooleanField('Сохранять урок в файл', default=True)

