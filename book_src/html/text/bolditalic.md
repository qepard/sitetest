# Полужирное и курсивное начертание

## &lt;b&gt;

<div style="display: flex;" markdown>
<div style="flex: 1; width:50%;" markdown>
Чтобы выделить текст полужирным начертанием шрифта, нужно поместить его между тегами `<b>` и `</b>`. Элемент `<b>` также обозначает фрагмент текста (например, ключевые слова), внешний вид которого будет отличаться от основного текста абзаца. 

При этом использование данного элемента не добавляет дополнительных значений к тексту.
</div>
<div style="flex: 1;width:50%" markdown>
``` html title="Жирное начертание"
<p>Вот так можно вывести текст с 
<b>полужирным</b> начертанием шрифта.
</p>
<p>В аннотации основные характеристики
какого-либо продукта могут быть выделены
<b>полужирным</b> начертанием шрифта.
</p>
```

</div></div>
<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/sitetest/assets/images/boldtext.png"></figure>

## &lt;i&gt;

Чтобы отобразить текст с курсивным начертанием шрифта, его следует поместить между тегами `<i>` и `</i>`.

Элемент `<i>` определяет фрагмент текста, отличающийся от основного текста. 

Например:

* технические термины
* иностранные слова
* прочие виды включений в текст, которые принято выделять курсивом

``` html title="Курсивное начертание"
<p>Вот так можно отобразить текст <i>курсивом</i>.</p>
    <p>Это сорт картофеля <i>Solanum tuberosum</i>.</p>
<p>Капитан Кук приплыл в Австралию на корабле <i>Индевор</i>.</p>
```

<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/sitetest/assets/images/italictext.png"></figure>


<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/headers'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/supsub'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
