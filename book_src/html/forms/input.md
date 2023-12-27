# Ввод текста

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<input>`
Элемент `<input>` используется для создания компонентов формы нескольких типов. Значение атрибута `type` указывает этот тип.

## `type="text"`
Когда атрибуту `type` присваивается значение `text`, это значит, что будет создано однострочное поле ввода текста.

## `name`
При введении пользователем данных в веб-форму сервер должен знать, какие сведения относятся к какому элементу формы (например, при обработке формы авторизации на сайте сервер должен знать, что было введено в качестве имени пользователя, а что - в качестве пароля).

Поэтому для каждого элемента формы следует указывать атрибут `name`.

Значение этого атрибута служит для идентификации элемента формы и отправляется на сервер вместе с введенными данными.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/login.php">
    <p>Имя пользователя:
        <input type="text" name="username" 
        size="15" maxlength="30" />
    </p>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/sitetest/assets/images/forminputex.png"></figure>

## `maxlength`
Вы можете использовать атрибут `maxlength` для ограничения количества символов, которое посетителю разрешается ввести в данное поле.

Например при запросе года вы можете ограничить количество символов, установив значение атрибута `maxlength` равным 4.

## `size`

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
При создании новых форм не следует указывать атрибут `size`.

Он использовался ранее для установки ширины поля ввода текста (в качестве единицы измерения выступало количество видимых символов).
</div>
<div style="flex:1;width:50%;" markdown>
Так, например, значение 3 создавало поле ввода текста, ширина которого была достаточной для отображения трех введенных символов (хотя пользователи при желании могли ввести и большее количество).
</div></div>
Для управления шириной элементов новых форм рекомендуется использовать средства каскадных таблиц стилей (**CSS**).

Я упомянул атрибут `size` только потому, что вы можете встретиться с ним при просмотре исходного кода старых сайтов.
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/forms/struct'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/forms/pass'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
