# Кнопки и скрытые элементы формы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" class="annotate" markdown>
## `<button>`
Элемент `<button>` был добавлен в язык **HTML**, чтобы позволить разработчикам сайтов получить более полный контроль над внешним видом кнопок, а также сделать возможным появление внутри кнопки других элементов.

Это значит, что теперь вы можете сочетать на кнопке текст и изображение, располагая их между открывающим `<button>` и закрывающим `</button>` тегами.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action=" http://www.example.com/add.php ">
    <button><img src="images/add.png" alt="добавить" 
    width="10" height="10" />Добавить</button>
    <input type="hidden" name="mark" 
    value="song lyrics" />
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formhidden.png"></figure></div></div>
<div class="annotate" markdown>
## `type="hidden"`
В этом примере мы также продемонстрируем вам элемент формы `hidden`(1).

Скрытые элементы не отображаются, хотя вы и можете увидеть их при просмотре исходного кода страницы.

Они позволяют веб-дизайнерам размещать в форме данные, невидимые посетителям.

Например разработчик может сохранить в скрытом поле информацию о том, с какой страницы посетитель отправил форму на сервер.
</div>

1.  `Hidden`(*англ.*) — скрытый.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/grafic'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/tags'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
