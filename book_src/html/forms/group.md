# Группировка элементов формы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<fieldset>`
Элементы формы, связанные по смыслу, можно сгруппировать между тегами `<fieldset>` и `</fieldset>`.

Это бывает особенно полезно при создании длинных форм.

Большинство браузеров отобразят `<fieldset>` в виде рамки вокруг группы элементов формы.

Внешний вид рамки может быть изменен с помощью каскадных таблиц стилей (**CSS**).
## `<legend>`
Элемент `<legend>`, содержащий надпись для обозначения группы элементов формы, как правило, помещают сразу после открывающего тега элемента `<fieldset>`.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<fieldset>
    <legend>Контактная информация</legend>
    <label>Email:<br />
        <input type="text" name="email" />
    </label>
    <br />
    <label>Телефон: <br />
        <input type="text" name="phone" />
    </label>
    <br />
    <label>Факс:<br />
        <input type="text" name="fax" />
    </label>
</fieldset>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formgroup.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/tags'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/date'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
