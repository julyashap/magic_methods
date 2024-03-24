from book_writer import BookWriter

bw = BookWriter('Pushkin')
with bw as writer:
    writer.add_page('Я вас любил')
    writer.add_page('Любовь еще быть может')
    writer.add_page('В моей душе угасла не совсем')

print('Книга завершена')
