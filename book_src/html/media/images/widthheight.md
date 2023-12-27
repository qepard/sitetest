# Высота и ширина изображений

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Зачастую вы будете видеть элемент `<img>` с еще двумя атрибутами, определяющими его размер:

## `height`
Данный атрибут устанавливает высоту изображения в пикселах.

## `width`
Данный атрибут устанавливает ширину изображения в пикселах.

Как правило, время загрузки изображений значительно дольше, чем HTML-кода, составляющего всю остальную разметку страницы.

Поэтому рекомендуется указывать размеры изображений, чтобы браузер мог продолжить обработку текста сайта, не дожидаясь окончания их загрузки и оставив необходимое количество пустого места.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<img src="images/quokkajpg" 
alt="Семейка квокки" 
width="600" height="450" />
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/imgex.jpg"></figure></div></div>

Все чаще и чаще создатели сайтов устанавливают размеры изображений с помощью каскадных таблиц стилей (**CSS**), а не посредством языка **HTML**.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/add'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/placing'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
