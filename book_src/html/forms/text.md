# Текстовая область

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<textarea>`
Элемент `<textarea>` используется для создания многострочных областей ввода текста.

В отличие от других элементов формы, он не является пустым, а следовательно, для него должны следует указать открывающий и закрывающий теги.

Текст, помещенный между ними, будет выведен в поле при загрузке страницы.

Если посетитель не удалит этот текст, то он отправится на сервер вместе с введенными им данными. (На некоторых сайтах реализован сценарий на языке *JavaScript*, очищающий текстовую область при щелчке мышью по ней.)
</div>
<div style="flex:1;margin-right:20px;width:60%;" markdown>
``` html title="Код"
<form action="http://www.primer.ru/profile.php">
    <p>Что вы думаете об этом выступлении?</p>
    <textarea name="comments" cols="20" rows="4">
    Введите свой комментарий…</textarea>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formtextex.png"></figure>

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
При создании новой формы используйте правила **CSS** для установки ширины и высоты текстовой области.

Однако при просмотре исходного кода старых сайтов вы можете встретить атрибуты `cols` и `rows`.
</div>
<div style="flex:1;width:50%;" markdown>
Атрибут `cols` устанавливает ширину текстовой области (измеряется в количестве символов в одной строке).

Атрибут `rows` задает высоту поля в строках.

</div></div></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/pass'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/switch'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
