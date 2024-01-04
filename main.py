import time
import uuid
from jwcrypto import jwk, jwt

device_id = str(uuid.uuid4())
key = jwk.JWK.generate(kty="EC", crv="P-256")
token = jwt.JWT(header={
    "typ": "dpop+jwt",
    "alg": "ES256",
    "jwk": key.export(private_key=False, as_dict=True)},
    claims={
        "iat": int(time.time()),
        "jti": str(uuid.uuid4()),
        # Please change htu by yourself
        "htu": "https://api.mercari.jp/v2/entities:search",
        # Please change htm by yourself
        "htm": "POST",
        "uuid": device_id})
token.make_signed_token(key)
jwt_token = token.serialize()
print(jwt_token)
