# Флажки

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `type="checkbox"`
С помощью флажков посетители сайта могут выбирать из нескольких вариантов ответа, а также отменять выбор.

## `checked`
Атрибут `checked` указывает, что данный флажок должен быть установлен по умолчанию при загрузке страницы.

Атрибут принимает единственное значение `checked`.

При использовании флажков, использование `checked` не обязательно.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/profile.php">
    <p>Пожалуйста, выберите любимые жанры музыки: 
    <br />
        <input type="checkbox" name="genre" 
        value="rock" checked="checked" />Рок
        <input type="checkbox" name="genre" 
        value="pop" checked="checked" />Поп
        <input type="checkbox" name="genre" 
        value="techno" />Электроника
    </p>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formflags.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/switch'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/list'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
