# Поле ввода поискового запроса

В языке **HTML5** существует специальный тип элементов формы, предоставляющий возможность создать поле ввода поискового запроса.

<div style="display:flex;margin-top:20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" class="annotate" markdown>
## `type="search"`
Для создания поля поискового запроса на языке **HTML5** присвойте атрибуту type элемента `<input>` значение `search`.

Старые версии браyзеров отобразят этот элемент формы как простое поле ввода текста.

В новых версиях браузеров реализованы дополнительные возможности для работы с такими полями.

Например, *Safari* для компьютеров *Мас* выводит дополнительный значок с крестиком, позволяющий очистить поле от введенной информации.

Кроме того, в этом браузере поля ввода поискового запроса автоматически отображаются с закругленными углами.

## `placeholder` 
Слюбым полем ввода вы можете использовать атрибут `placeholder`(1), значением которого является текст, отображаемый в поле до того, как пользователь введет свой запрос.

Старые версии браузеров игнорируют этот атрибут.
</div>

1.  Placeholder(*англ.*) — заполнитель.

<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.example.org/search.php">
    <p>Поиск:</p>
    <input type="search" name="poisk" />
    <input type="submit" value="Искать" />
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formsearch.png"></figure>
<div style="margin-top:40px;" markdown>
``` html title="Код"
<form action="https://www.example.org/search.php">
    <p>Поиск:</p>
    <input type="search" name="poisk" 
    placeholder="Купить компьютер"/>
    <input type="submit" value="Искать" />
</form>
```
</div>
<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formsearch2.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/urlmail'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/example'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
