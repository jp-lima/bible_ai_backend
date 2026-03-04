from typing import NotRequired
from repositories.wallet_repo import *
from datetime import datetime
from zoneinfo import ZoneInfo
import uuid

def service_create_new_wallet(user_id):

    new_id = uuid.uuid4()
    now = datetime.now(ZoneInfo("America/Sao_Paulo"))

    create_new_wallet(str(new_id), user_id,  20,now, "", now, now  ) 

    return












