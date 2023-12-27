# Важная информация и логическое ударение

<div style="display:flex;" markdown>
<div style="flex:1;margin-top:-20px;" markdown>
## &lt;strong&gt;

Элемент `<strong>` используется для обозначения того, что текст, помещенный в него, имеет высокую степень важности. 

Например текст этого элемента может быть интонационно выделен при чтении программой экранного доступа. 

По умолчанию браузеры отображают содержимое элемента `<strong>` шрифтом с полужирным начертанием.

</div>
<div style="flex:1;margin-left:10px" markdown>

``` html title="Код"
<p><strong>Будьте осторожны: </strong>
В данной местности орудуют воры-карманники.
</p>
<p>Данная игрушка содержит
большое количество мелких деталей и 
<strong>
не предназначена для детей младше пяти лет.
</strong>
</p>
```
<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/sitetest/assets/images/strongex.png"></figure></div></div>
<hr>
<div style="display:flex;" markdown>
<div style="flex:1;" markdown>
## &lt;em&gt;

Элемент `<em>` используется для обозначения логического ударения, которое несколько изменяет значение всего предложения.

По умолчанию браузеры отображают содержимое элемента `<em>` шрифтом с курсивным начертанием.

</div>
<div style="flex:1;margin-left:10px;margin-top:10px;" markdown>

``` html title="Код"
<p>Я <em>думаю</em>, Анна была первой.</p>
<p>Я думаю, <em>Анна</em> была первой.</p>
<p>Я думаю, Анна была <em>первой</em>.</p>
```
<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/sitetest/assets/images/emex.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/supsub'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/bqq'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
