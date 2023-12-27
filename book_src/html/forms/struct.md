# Структура формы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<form>`
Все элементы формы помещаются в тег `<form>`.

Для него всегда должен быть указан атрибут `action`, кроме того, для этого элемента часто устанавливают атрибуты `method` и `id`.

## `action` 
Каждый элемент `<form>` требует указания атрибута `action`, значением которого является URL-адрес страницы-получателя введенных данных при отправке формы на сервер.

</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form 
    action="https://www.primer.ru/subscribe.php" 
    method="get">
    <p>Здесь будут отображены элементы формы.</p>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formex.png"></figure>

## `id`
Мы обсудим атрибут `id` в главе 8.

Сейчас лишь скажем, что его значение используется для различения формы и других элементов разметки страницы (зачастую этот атрибут используется сценариями, например, для проверки заполнения всех обязательных полей формы).
</div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `method`
Формы можно отправить одним из двух методов: `get` или `post`.

При использовании метода `get` введенные данные будут добавлены в конец URL-адреса, указанного в атрибуте `action`.
</div>
<div style="flex:1;width:50%;" markdown>
<div style="display:flex;margin-top:80px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
При использовании метода `post` данные отправляются на сервер с помощью так называемых **HTML**-заголовков.
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Если атрибут `method` не указан, то форма будет отправлена на сервер с помощью метода `get`.
</div></div></div></div>
<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Метод `get` идеален:

* для коротких форм (таких как поля для ввода поискового запроса)
* при простом получении данных с веб-сервера (без отправки сведений, добавляемых в базу данных).
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Хорошей практикой будет использование метода `post` в случае, если ваша форма:

* позволяет пользователям загружать файлы на сайт
* очень длинная
* содержит конфиденциальные данные (например пароли)
* добавляет сведения в базу данных или удаляет их оттуда.
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/why'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/input'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
