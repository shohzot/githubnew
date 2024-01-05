import json


class CacheStorage:
    def __init__(self,):
        self.__cache = {}

    async def get_storage(self):
        return self.__cache

    async def get_user(self, chat_id: int):
        return self.__cache[chat_id]

    async def add(self, chat_id: int, forms: list, likes: list, mutual: list) -> str:
        template = {
            "forms": forms,
            "likes": likes,
            "mutual": mutual,
        }
        self.__cache[chat_id] = template
        return json.dumps({chat_id: template})

    async def delete_user(self, chat_id) -> None:
        self.__cache.pop(key=chat_id)

    async def delete_position(self, chat_id, dictionary="forms") -> None:
        try:
            del self.__cache[chat_id][dictionary][0]
        except Exception as ex:
            print(ex)


