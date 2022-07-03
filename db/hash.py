from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes='bcrypt')


class Hash:

    @staticmethod
    def bcrypt(password: str):
        """
        bcrypt library is highly used to hash passwords and store them
        in the database
        :param password:
        :return:
        """
        return pwd_ctx.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password: str):
        """
        This is a normal way to verify the plain text and its hashing
        using bcrypt
        :param hashed_password:
        :param plain_password:
        :return:
        """
        return pwd_ctx.verify(plain_password, hashed_password)
