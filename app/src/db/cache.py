import abc


class AbstractCache:
    @abc.abstractmethod
    def get_cache(self, id_: str):
        """Получить кэш из хранилища"""
        pass

    @abc.abstractmethod
    def put_data_to_cache(self, id_: str, user_agent: str, data: str):
        """Записать в кэш данные"""
        pass

    def delete_cache(self, id_: str):
        """Удалить кеш из хранилища"""
