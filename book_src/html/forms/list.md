# Раскрывающийся список

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<select>`
Раскрывающийся список появляется при щелчке мышью по элементу формы и позволяет посетителю сайта выбрать один вариант.

Для создания раскрывающегося списка используется элемент `<select>`.

Он может содержать два и более элементов `<option>`.

## `name`
Атрибут `name` определяет имя элемента формы, отправляемое на сервер вместе со значением, выбранным посетителем.

</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.example.com/profile.php">
    <p>
    На каком устройстве вы слушаете музыку чаще всего?
    </р>
    <select name="devices">
        <option value="phone">Телефон</option>
        <option value="radio">Радио</option>
        <option value="computer">Компьютер</option>
    </select>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formlist.png"></figure></div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `<option>`
Элемент `<option>` используется для указания вариантов ответа, которые может выбрать посетитель сайта.

Текст, помещенный между тегами `<option>` и `</option>`, будет выведен на экран как пункт раскрывающегося списка.
</div>
<div style="flex:1;width:50%;" markdown>
## `value`
Атрибут `value` используется в элементе `<option>` для установки значения, отправляемого на сервер вместе с именем выбранного элемента.
</div></div>
<hr>

# Список множественного выбора

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `size`
Добавив в элемент `<select>` атрибут `size`, вы превратите раскрывающийся список в поле, отображающее сразу несколько вариантов выбора.

Значением этого атрибута должно быть количество пунктов списка, отображаемых за раз.

В примере одновременно видны три из четырех вариантов ответа.

К сожалению, не все браузеры правильно отображают списки с атрибутом `size`, потому работоспособность сайта нужно тщательно проверять (особенно это касается браузеров *Firefox* и *Safari* на компьютерах с операционной системой *OS X*).
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/profile.php">
    <p> Играете ли вы на одном из инструментов, 
    перечисленных ниже? 
    (Вы можете выбрать сразу несколько вариантов ответа, 
    нажав и удерживая клавишу 
    <b>Ctrl</b>(Windows) или <b>Cmd</b>(OS X)).</p>
    <select name="instruments" size="3" multiple="multiple">
        <option value="giutar" 
        selected="selected">Гитара</option>
        <option value="drum">Барабаны</option>
        <option value="keyboards" 
        selected="selected">Клавишные</option>
        <option value="bass">Бас-гитара</option>
    </select>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formlist2.png"></figure></div></div>

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `multiple` 
Добавив атрибут `multiple` со значением `multiple`, вы позволите посетителям вашего сайта выбирать сразу несколько вариантов ответа (не забудьте написать предупреждение об этой возможности).
</div>
<div style="flex:1;margin-top:80px;width:60%;" markdown>
Также полезно будет упомянуть о том, что пользователи компьютеров под управлением операционной системы Windows могут выбрать несколько пунктов списка, нажав и удерживая клавишу *Ctrl*, а пользователи компьютеров *Мас* - с помощью клавиши *Cmd*.
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/flags'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/upload'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
