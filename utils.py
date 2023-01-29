import json

# загрузка постов
def get_posts_all():
    with open("data/posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)  
        return posts  

# загрузка комментариев
def get_comments_all():
    with open("data/comments.json", "r", encoding="utf-8") as file:
        comment = json.load(file)  
        return comment  

# поиск постов по имени пользователя
def get_posts_by_user(user_name):
    try:
        post = []
        all_post = get_posts_all()
        for i in all_post:
            if user_name == i["poster_name"]:
                post.append(i)
        return post
    except ValueError:
        return []

# поиск постов по индексу поста
def get_comments_by_post_id(post_id):
    try:
        comment = []
        all_comment = get_comments_all()
        for i in all_comment:
            if post_id == i['post_id']:
                comment.append(i)
        return comment
    except ValueError:
        return []

# поиск постов по слову в посте
def search_for_posts(query):
    try:
        contents = []
        all_posts = get_posts_all()
        for i in all_posts:
            if query in i["content"]:
                contents.append(i)
        return contents
    except ValueError:
        return []

# поиск постов по индексу пользователя
def get_post_by_pk(pk):
    try:
        one_post = get_posts_all()
        for i in one_post:
            if pk == i["pk"]:
                return i
    except ValueError:
        return []
