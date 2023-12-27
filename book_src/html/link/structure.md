# Структура директорий

При создании больших сайтов полезной является такая организация, когда страницы каждого раздела сайта помещаются в собственную папку. Папки сайтов также иногда называют директориями.

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:10px;width:50%;" markdown>
## СТРУКТУРА

Схема справа демонстрирует структуру директорий вымышленного сайта развлечений ExampleArts.

Верхняя папка называется **корневым** каталогом. (В этом примере корневой каталог носит имя *examplearts*.)

В корневом каталоге хранятся все файлы и папки сайта.

Для упрощения организации хранения файлов каждый раздел сайта имеет свою собственную папку.
</div>
<div style="flex:1;margin-right:10px;width:50%;" markdown>
## ОТНОШЕНИЯ

Отношения между папками и файлами сайта очень напоминает генеалогическое древо человека.

На схеме снизу указаны некоторые отношения.

Так, папка *examplearts* является родительской для папок *movies*, *music* и *theater*.

В то же время папки *movies*, *music* и *theater* являются дочерними по отношению к папке *examplearts*.
</div>
<div style="flex:1;margin-right:10px;width:50%;" markdown>
## ГЛАВНЫЕ СТРАНИЦЫ

Главная страница сайта, написанная на языке HTML (и главные страницы всех разделов сайта), имеет имя файла *index. html*.

Как правило, веб-серверы настроены таким образом, чтобы возвращать посетителю страницу с именем *index. html*, если иное не указано во введенном адресе.

Поэтому, если вы введете адрес *examplearts.com* , то получите страницу *examplearts.com/index. html*; аналогично страница *examplearts.com/music/index*. html будет возвращена при вводе адреса *examplearts.com/music*.
</div></div>

<img src="/html-css-manual/assets/images/structureex.png" style="left:50%">

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Корневой каталог содержит:

* файл с именем *index.html*, являющийся главной страницей всего сайта

* отдельные папки для разделов сайта, посвященных фильмам, музыке, и театру
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Каждая подпапка содержит:

* файл с именем *index.html*, являющийся главной страницей для данного раздела сайта

* страницу с обзорами, сохраненную с именем *reviews.html*

* страницу с перечнем названий *listings.html* (кроме раздела, посвященного DVD-дискам)
</div>
<div style="flex:1;;width:50%;" markdown>
Раздел, посвященный фильмам, содержит:

* папку *cinema*

* папку *dvd*
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/other'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/mail'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
