# pip пакеты проекта
- Flask
- Flask-WTF

# Добавление поля на страницу 
1. В forms.py импортируем тип нужного поля и в класс JSONForm добавляем его (атрибуты которые можно передавать я спрашивал у ChatGPT, первый атрибут - всегда лейбл)
2. В routes.py в функции my_form у словаря data добавляем новое поле
3. В шаблоне index.html добавляем код в нужное место 
```
<div class="form__input-container">
    <label class="form__label" for="{{ form.bot_type.id }}">Тип бота</label>
    {{ form.bot_type(class="form__input_select") }}
</div>
```
***Вместо bot_type название новго поля а вместо _select у класса добавляем тип нового поля (_select, _checkbox, _textarea)***
