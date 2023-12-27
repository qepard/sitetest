# Добавление изображений

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## &lt;img&gt;

Для добавления изображения на страницу воспользуйтесь элементом `<img>`. Он является пустым (то есть без закрывающего тега).

Для него должны быть указаны следующие два атрибута.

## `src`
Данный атрибут сообщает браузеру расположение нужного изображения. Как правило, его значением будет относительный URL- адрес, указывающий на изображение, хранящееся в директориях вашего собственного сайта.

(В данном примере все изображения расположены в подпапке images. Об относительных URL-адресах речь шла в предыдущей главе.)

## `alt`

Данный атрибут предоставляет текстовое описание изображения, выводимое на экран в случае, если нет возможности показать само изображение.

</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<img src="images/quokka.jpg" 
alt="Семейка квокки" 
title="Квокка или короткохвостый кенгуру - единственный представитель рода Setonix семейства кенгуровых. 
Квокка внешне напоминает кенгуру, но имеет короткий, даже относительно размеров тела, хвост."/>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/imgex.jpg"></figure>

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Текст, указываемый в значении атрибута `alt`, часто называют **замещающим текстом**.

Он должен представлять собой точное описание изображения, чтобы оно могло быть распознано программным обеспечением экранного доступа (используемым людьми с нарушением зрения) и поисковыми системами.
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Если вы используете изображение лишь как декорацию для улучшения оформления сайта (и оно не несет никакой смысловой нагрузки, как, например, графический разделитель — горизонтальная линия), используйте атрибут `alt` с пустым значением (между кавычек не должно быть никакого текста).
</div></div></div></div>

## `title`

С элементом `<img>` вы также можете использовать атрибут `title` для сообщения дополнительной информации об изображении.

Большинство браузеров отобразят содержимое этого атрибута в качестве всплывающей подсказки при наведении указателя мыши на изображение.
<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/widthheight'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
