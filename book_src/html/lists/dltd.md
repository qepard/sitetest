# Списки определений

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## &lt;dl&gt;

Список определений создается с помощью элемента `<dl>` и, как правило, содержит набор понятий и их определений.

Внутри элемента `<dl>` вы зачастую сможете увидеть пары элементов `<dt>` и `<dd>`.

## &lt;dt&gt;

Используется для обозначения понятия (термина).

## &lt;dd&gt;

Используется для определения понятия.

Иногда вы можете столкнуться со списками, в которых два понятия имеют одно определение или где для одного понятия приводится несколько определений.

</div>
<div style="flex: 1;width:50%;" markdown>
``` html title="Код"
<dl>
    <dt>Сашими</dt>
    <dd>Сырая рыба, нарезанная тонкими кусочками; 
    подается с такими приправами, как нашинкованная японская редька (дайкон), 
    корень имбиря, васаби или соевый соус</dd>
    <dt>Весы</dt>
    <dd>Прибор, используемый для определения точного веса ингредиентов.</dd>
    <dd>Зодиакальный знак, 
    распространяющийся на календаре с 23 сентября по 22 октября, 
    единственный в зодиаке неодушевленный символ.</dd>
    <dt>Hoy-xay</dt>
    <dt>Ноухay</dt>
    <dd>Мастерство, умение, практическая сметка, высококвалифицированная работа; 
    компетенция и опыт, приобретаемые длительной практикой. </dd>
</dl>
```
<figure><figcaption>Результат</figcaption><img src="/sitetest/assets/images/dltdex.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/lists/liolul'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/lists/liaddition'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
