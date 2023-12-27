import os

directory = r'C:\Users\qep\source\repos\GitHub\sitetest\book_src'  # Указанный вами путь к директории

search_string = "html-css-manual"
replacement_string = "sitetest"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):  # Можно указать расширения файлов, в которых нужно делать замену
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            if search_string in file_content:
                file_content = file_content.replace(search_string, replacement_string)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(file_content)

print("Замены выполнены успешно.")
