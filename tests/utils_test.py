import pytest
from utils import *

def test_get_posts_all():
    test = get_posts_all()
    assert type(test) == list, "Ошибка, тип не list"
    assert type(test[0]) == dict, "Ошибка, тип не dict"

def test_get_comments_all():
    test = get_comments_all()
    assert type(test) == list, "Ошибка, тип не list"
    assert type(test[0]) == dict, "Ошибка, тип не dict"

def test_get_posts_by_user():
    user_name = 'leo'
    test = get_posts_by_user(user_name)
    assert type(test) == list, "Ошибка, тип не list"
    assert type(test[0]) == dict, "Ошибка, тип не dict"

def test_get_comments_by_post_id():
    post_id = 1
    test = get_comments_by_post_id(post_id)
    assert type(test) == list, "Ошибка, тип не list"
    assert type(test[0]) == dict, "Ошибка, тип не dict"

def test_search_for_posts():
    query = 'Утром'
    test = search_for_posts(query)
    assert type(test) == list, "Ошибка, тип не list"
    assert type(test[0]) == dict, "Ошибка, тип не dict"

def get_post_by_pk():
    pk = 1
    test = get_post_by_pk(pk)
    assert type(test) == list, "Ошибка, тип не list"
    assert type(test[0]) == dict, "Ошибка, тип не dict"
