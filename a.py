# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = "theme=auto; over18=1; _ym_uid=1635847009406407938; _ym_d=1635847009; locale=zh; _ym_isad=2; _jdb_session=d7ZdU%2FavfWLVXK9awNa7EMjxfLBzfMVzNGvc%2Ben0coKs5HLkhTx0ccudYHC64tahW80QoNySgBDBAloluO8j2nx7QVAOfdwTMPcXy%2FLiTVnzR4ZnoRUue3KAhy0d%2BfU7BnucgbQBsL4dWT3sXC%2Fo9pPNIB6JTq7J0zzHwyVQXrD82fT%2FWbh4fDkigs8h9BqX3MVG7p%2BWLu%2F%2BlEhAY1JVVilMXT7ojntHQNfJliLVuGp%2FaIrB32%2Bq0PmLfCLyICuo3qzUPWtOntj6FKUCWxkjNH1J0Ogf3NoESNWZgQJ1Afd8NweAWQQb84LZqbwS3XrG7VvRgOY1EFsIrkphS%2Ba4ij18ozHKriengUU0I2gNVZfQYeNBZuzTQ%2FqLxwYLt924FMA%3D--Z2aIizgjyA1RvpLH--%2BdCJUjvThBIUKi3WlBz52Q%3D%3D"
    trans = transCookie(cookie)
    print (trans.stringToDict())