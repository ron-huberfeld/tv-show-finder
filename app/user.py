from hashlib import md5


class User(object):
    def avatar(self, size, data):
        digest = md5(data.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
