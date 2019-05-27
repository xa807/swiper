# coding:utf-8

import sqlite3
import requests

config = {
    'host': 'es',
    'index': 'food_index',
    'doc_type': 'food',
    'db_name': '../swiper.db'
}


def init():
    try:
        # 创建es-index
        index_url = f'http://{config["host"]}:9200/{config["index"]}'
        resp = requests.put(index_url,
                            json={
                                "settings": {
                                    "number_of_shards": 5,
                                    "number_of_replicas": 1
                                }
                            })

        conn = sqlite3.connect(config['db_name'])
        c = conn.cursor()
        c.execute('SELECT id,name,author,image,steps,steps_time,practice,taste FROM t_food')
        for row_data in c.fetchall():
            id, name, author, image, steps, steps_time, practice, taste = row_data

            doc_url = index_url + f'/{config["doc_type"]}/{id}'
            resp = requests.post(doc_url,
                                 json={
                                     'name': name,
                                     'author': author,
                                     'image': image,
                                     'steps': steps,
                                     'steps_time': steps_time,
                                     'practice': practice,
                                     'taste': taste
                                 })

            if resp.json()['created']:
                print(f'add {id} Doc ok')

    except Exception as e:
        print(e)


def search_doc(s):
    try:
        url = f'http://{config["host"]}:9200/{config["index"]}/_search?q={s}'
        resp = requests.get(url)
        data = resp.json()
        result = []
        for hits in data['hits']['hits']:
            food_data = hits['_source']
            food_data['id'] = hits['_id']
            result.append(food_data)

        return result
    except Exception as e:
        return []


if __name__ == '__main__':
    init()