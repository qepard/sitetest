# Пример

Это пример демонстрирует создание формы для сбора мнений посетителей сайта и оформления подписки на новостную рассылку.

В элементе `<form>` используется атрибут action, указывающий адрес веб-страницы, на которую отправляются введенные данные.

Все элементы формы находятся между тегами `<form>` и `</form>`.

В форме используется несколько видов элементов, созданых для сбора различных данных.

`<fieldset>` используется для группировки связанных по смыслу элементов формы.

`<label>` указывает назначение каждого из элементов.

``` html title="Код"
<html>
    <head>
        <title>Формы</title>
    </head>
    <body>
        <form action=" http://www.example.com/review.php " method="get">
            <fieldset>
                <legend>Данные пользователя:</legend>
                <label>Имя:
                    <input type="text" name="name" size="30" maxlength="100">
                </label>
                <br />
                <label>Email:
                    <input type="email" name="email" size="30" maxlength="100">
                </label>
                <br />
            </fieldset>
            <br />
            <fieldset>
                <legend>Ваше мнение:</legend>
                <p>
                    <label for="hear-about">
                        Как вы узнали о нас?
                    </label>
                    <select name="referrer" id="hear-about">
                        <option value="google">Google</option>
                        <option value="friend">От друзей</option>
                        <option value="advert">Реклама</option>
                        <option value="other">Другоe</option>
                    </select>
                </p>
                <p>Посетите ли вы наш сайт снова?
                    <br />
                    <label>
                        <input type="radio" name="rating" value="yes" />
                        Да
                    </label>
                    <label>
                        <input type="radio" name="rating" value="no" />
                        Нет
                    </label>
                    <label>
                        <input type="radio" name="rating" value="maybe" />
                            Возможно
                    </label>
                </p>
                <p>
                    <label for="comments">Комментарий:</label>
                    <br />
                    <textarea rows="4" cols="40" id="comments"></textarea>
                </p>
                <label>
                    <input type="checkbox" mame="subscribe" checked="checked" />
                        Я хочу получать рассылку с новостями сайта
                </label>
                <br />
                <input type="submit" value="Submit review"/>
            </fieldset>
        </form>
    </body>
</html>
```

<center>[Результат](/html-css-manual/assets/files/FORMEX.html){ .md-button }

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/search'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/extra'"><span style="margin: 0 10px;">Следующая глава</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
