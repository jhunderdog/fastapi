from datetime import datetime, timedelta
import time
import random
import bcrypt
from jose import jwt
class UserService:
    encoding: str = "UTF=8"
    secret_key : str = "92240a4702adc109eebc4b0db083a0e41a14c132d813bbbfce01765de1fa1b72"
    jwt_algorithm : str = "HS256"
    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding),
            salt=bcrypt.gensalt()
        )
        return hashed_password.decode(self.encoding)

    def verify_password(
            self, plain_password: str, hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            plain_password.encode(self.encoding),
            hashed_password.encode(self.encoding)
        )

    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
            "sub": username, #unique id
            "exp": datetime.now() + timedelta(days=1),
        },
            self.secret_key,
            algorithm=self.jwt_algorithm,
        )

    def decode_jwt(self, access_token : str):
        payload : dict = jwt.decode(
            access_token, self.secret_key, algorithms=[self.jwt_algorithm]
        )
        # expire
        return payload["sub"] #username

    @staticmethod
    def create_otp() -> int:
        return random.randint(1000, 9999)

    @staticmethod
    def send_email_to_user(email: str) -> None:
        time.sleep(10)
        print(f"Sending email to {email}!")