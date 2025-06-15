import base64
import json

def decode_jwt_payload(token):
    try:
        # Pega a parte do payload (segunda parte do token)
        payload_part = token.split('.')[1]

        # Corrige o padding do Base64
        padding = '=' * (-len(payload_part) % 4)
        payload_part += padding

        # Faz o decode Base64
        decoded_bytes = base64.urlsafe_b64decode(payload_part)
        decoded_str = decoded_bytes.decode('utf-8')

        # Converte JSON para dicionário Python
        payload = json.loads(decoded_str)
        return payload

    except Exception as e:
        print(f"Erro ao decodificar JWT: {e}")
        return None