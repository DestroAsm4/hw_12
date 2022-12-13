import json
from json import JSONDecodeError


def load_posts_json():
    '''
    :return: возвращает json файл
    '''
    with open('posts.json', 'r', encoding='utf8') as jfile:
        try:
            result = json.load(jfile)
            return result
        except JSONDecodeError:
            # Будет выполнено, если файл найден, но не превращается из JSON
            print("Файл не удается преобразовать")


def tegs(text):
    '''
    :param text: получает текст поста
    :return: возвращает список слов-тегов
    '''
    text_split = text.split()
    tegs = list(filter(lambda item: item[0] == '#', text_split))
    result = list(map(lambda item: item[1:len(item)], tegs))
    return result


def write_index_tegs(index, tegs=None):
    '''
    :param index: индекс тегов
    :param tegs: список слов-тегов
    :return: записывает данные в файл index_tegs
    '''
    if tegs:
        list_tegs = ', '.join(tegs)
    else:
        list_tegs = None
    with open('index_tegs.txt', 'a', encoding='utf8') as afile:
        afile.write(str(index) + ':' + str(list_tegs) + '\n')


def write_all_tegs():
    '''
    :return: пишет индекс - теги, по всем данным в файле post.json
    '''
    posts = load_posts_json()
    for index, post in enumerate(posts):
        list_tegs = tegs(post['content'])
        write_index_tegs(index, list_tegs)


def read_tegs():
    '''
    :return: возвращает индекс - теги в списке словарей
    '''
    result = []
    with open('index_tegs.txt', 'r', encoding='utf8') as rfile:
        for line in rfile:
            split_line = line.split(':')
            if split_line[1].strip() == 'None':
                result.append({int(split_line[0]): None})
            else:
                list_tegs = split_line[1].strip().split(', ')
                result.append({int(split_line[0]): list_tegs})
        return result


def desaired_content(key):
    '''
    :param key: слово по которому идет поиск тегов
    :return: возвращет индексы, если искомый тег соответствует списку тегов
    '''
    result = []
    list_tegs = read_tegs()
    for item in list_tegs:
        item_values = list(item.values())[0]
        if item_values and key in item_values:
            result.append(list(item.keys())[0])
    return result


def desired_posts(list_index):
    '''
    :param list_index: получает список индексов из функции desaired_content
    :return: возвращает список постов
    '''
    posts = load_posts_json()
    result = []
    for index in list_index:
        result.append(posts[index])
    return result


def add_post(link_pic, text):
    '''
    :param link_pic: ссылка на картинку
    :param text: текст поста
    :return: пишет в файл json новый пост
    '''
    posts = load_posts_json()
    new_post = {'pic': link_pic, 'content': text}
    posts.append(new_post)
    with open('posts.json', 'w', encoding='utf-8') as jfile:
        json.dump(posts, jfile, ensure_ascii=False, indent=2)


def add_tegs(text):
    '''
    :param text: получает текст поста
    :return: используя фнкции создает новыйы список тегов в файле index-tegs
    '''
    new_index = len(read_tegs())
    list_tegs = tegs(text)
    write_index_tegs(new_index, list_tegs)


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def is_filename_allowed(filename):
    '''
    :param filename: получает имя файла
    :return: проверяет его на соответствие списку расширений
    '''
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False
