import hashlib


def gen_secret(passwd):
    if isinstance(passwd, str):
        sha512 = hashlib.sha512()
        sha512.update(passwd.encode("utf-8"))
        return sha512.hexdigest()
    raise Exception("密码不是字符类型，请检验后重试！")