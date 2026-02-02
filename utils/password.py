from enum import verify
import bcrypt

def create_hash(plain_password:str):
    salt = bcrypt.gensalt()  # gera um salt seguro automaticamente
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")  # salva como string no banco

def verify_hash(plain_password,hashed_password):
      return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


if __name__ == "__main__":
    t = verify_hash("sdksd", "$2b$12$HJYK7YkGSNSA2EGOQSqg1.SgVcP.t.CZZxb2wbCF/GqnVBEub9Vom")


    print(t)
