from fastapi import FastAPI
import ntplib
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

app = FastAPI()


@app.get("/time")
def get_chile_time():
    client = ntplib.NTPClient()
    response = client.request("ntp.shoa.cl", version=3)
    # Hora en UTC con tz=UTC
    utc_time = datetime.fromtimestamp(response.tx_time, tz=timezone.utc)
    # Convertir a hora oficial de Chile
    chile_time = utc_time.astimezone(ZoneInfo("America/Santiago"))
    return {
        "hora_actual_chile": chile_time.strftime("%Y-%m-%d %H:%M:%S"),
    }
