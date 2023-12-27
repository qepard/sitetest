# Ввод даты

## `<input>`
Во многие формы требуется вводить такую информацию, как даты, адреса электронной почты или URL.

Обычно это реализуется с помощью полей ввода текста.

В языке **HTML5** появились новые элементы формы, позволяющие стандартизировать ввод данных определенного типа.

Более старые версии браузеров, не поддерживающие **HTML5**, будут визуализировать такие элементы формы просто как однострочные поля ввода текста.

<div style="display:flex;margin-top:20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `type="date"`
Для запроса ввода даты вы можете использовать элемент `<input>` со значением `date` атрибута `type`.

Таким образом, в браузерах, поддерживающих элементы формы спецификации **HTML5**, будет выведено поле для ввода даты.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/bookings/" 
method="post">
    <label for="depart">Дата вылета</label>
    <input type="date" name="depart"/>
    <input type="submit" value="Отправить">
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formdate.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/group'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/validation'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
