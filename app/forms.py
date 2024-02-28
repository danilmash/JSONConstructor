from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, TextAreaField
from wtforms import validators

class JSONForm(FlaskForm):
    bot_type = SelectField('Тип бота', choices=[('chat_gpt', 'ChatGPT'), ('yandex_gpt', 'YandexGPT')], validators=[validators.DataRequired()])
    language = SelectField('Изучаемый язык', choices=[('eng', 'English'), ('ge', 'German')], validators=[validators.DataRequired()])
    lesson_type = SelectField('Тип уроки', choices=[('topic_speak','Разговор на выбранную тему'), ('words_check', 'Проверка слов на выбранную тему')], validators=[validators.DataRequired()])
    topic = TextAreaField('Тема урока')
    text = TextAreaField('Текст для ответов на вопросы')
    save_to_file = BooleanField('Сохранять урок в файл', default=True)

