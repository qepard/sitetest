# Загрузка файлов на сервер

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<input>`
Если вы хотите позволить посетителям размещать файлы на вашем сайте, например изображения, видеоролики, MPЗ-записи или документы в формате PDF, вам понадобится специальное поле для загрузки файлов.

</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/zagruzka.php" method="post">
    <p>Выгрузите свою песню в формате MP3:</p>
        <input type="file" name="pesnya" />
        <br />
        <input type="submit" value="Загрузить" />
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formupload.png"></figure></div></div>
<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `type="file"`
Данное значение атрибута `type` создает поле, по внешнему виду напоминающее поле ввода текста, после которого помещается кнопка Обзор (Browse).
</div>
<div style="flex:1;margin-top:80px;width:50%;" markdown>
Когда посетитель щелкает по ней мышью, браузер открывает диалоговое окно, позволяющее выбрать нужный файл на компьютере.
</div></div>

При создании формы, позволяющей загружать файлы на сервер, всегда указывайте метод `post` (значение атрибута method элемента `<form>`).

Передача файлов на сервер невозможна при использовании метода `get`.

Внешний вид диалогового окна, выводимого при щелчке мышью по кнопке Обзор (Browse) и позволяющего посетителю выбрать нужный файл для загрузки, определяется установленной на компьютере посетителя операционной системой.

Вы не можете изменить интерфейс этого диалогового окна.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/list'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/confirm'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
