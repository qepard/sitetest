# Источники и определения

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;" markdown>
## &lt;cite&gt;

Элемент `<cite>` может быть использован при оформлении ссылки на какой-то первоисточник, например на книгу, кинофильм или исследовательскую работу, для обозначения упоминаемого источника. 

В спецификации **HTML5** не рекомендуется использовать элемент `<cite>` с именами персоналий, однако это вполне допускается в **HTML4**, потому, скорей всего, большинство веб- дизайнеров так и продолжат использовать данный элемент в этих целях. 

Браузеры отображают содержимое элемента `<cite>` шрифтом с курсивным начертанием.

</div>
<div style="flex: 1;" markdown>
``` html title="Код"
<p>
По всему миру было продано 
более десяти миллионов копий книги 
<cite>Краткая история времени</cite> 
Стивена Хокинга.
</p>
```
<figure><figcaption>Результат</figcaption><img src="/sitetest/assets/images/citeex.png"></figure></div></div>
<hr>
<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;" markdown>
## &lt;dfn&gt;

Объяснение нового термина (научного концепта или профессионального жарго- низма) в тексте называется «определением».

Элемент `<dfn>` используется для обозначения определения какого-либо нового термина.

Некоторые браузеры отображают содержимое элемента `<dfn>` шрифтом с курсивным начертанием.

</div>
<div style="flex: 1;" markdown>
``` html title="Код"
<p><dfn>Черная дыра</dfn> - это
область в пространстве-времени,
гравитационное притяжение которой настолько велико, 
что покинуть её не могут даже объекты,
движущиеся со скоростью света 
(в том числе и кванты самого света).
</p>
```
<figure><figcaption>Результат</figcaption><img src="/sitetest/assets/images/dfnex.png"></figure></div></div>


<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/abbr'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/insdel'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>

