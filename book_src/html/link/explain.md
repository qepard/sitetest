# Ссылки

Ссылки создаются с помощью элемента `<a>`. 

Пользователи могут щелкнуть по любому слову текста, помещенного между открывающим `<а>` и закрывающим `</a>` тегами элемента. 

Используя атрибут `href`, вы можете указать, на какую страницу будет перенаправлен пользователь при щелчке мышью по данной ссылке.

``` html title="Ссылка"
<a href="https://www.imdb.com">IMDB</a>
```

<div style="display:flex;float:center;" markdown>
<div style="flex:1;margin-right:10px;" markdown>
* <span style="color:#2EAD6E">Зеленым</span> цветом указан адрес страницы на которую переведет вас данная ссылка.
</div>
<div style="flex:1;" markdown>
* `IMDB` — текст, по которому пользователь щелкает мышью
</div></div>

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/linkex.png"></figure>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:10px;" markdown>
Текст, помещенный между открывающим `<а>` и закрывающим `</a>` тегами, называется «текстом ссылки».

По мере возможности он должен пояснять посетителям, куда они будут переведены в результате щелчка мышью (а не просто гласить «щелкните здесь»). 

На рисунке выше вы можете видеть ссылку на сайт «IMDB».
</div>
<div style="flex:1;margin-right:10px;" markdown>
Многие люди переходят между страницами, находя ссылки в тексте.

Ясный и доходчивый текст способен помочь посетителям вашего сайта отыскать именно то, что нужно им.

Это оставит у них больше приятных впечатлений о вашем сайте, что, в свою очередь, поощрит их посещать его чаще.

(Кроме того, это поможет людям, использующим программы экранного доступа.)
</div>
<div style="flex:1;" markdown>
Чтобы создать хороший текст ссылки, подумайте над тем, какие запросы станут использовать люди при поиске страницы с информацией, на которую вы ссылаетесь.

Например, вместо текста наподобие «места, где можно переночевать», напишите что-то более конкретное, например «гостиницы Москвы».
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/other'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
