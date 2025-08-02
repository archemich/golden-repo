import logging

import psycopg2
import uvicorn
from fastapi import FastAPI

from .configuration import Configuration

config = Configuration()

app = FastAPI()
conn = psycopg2.connect(config.db_url)
logger = logging.getLogger(__name__)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/pay")
async def pay() -> dict[str, str]:
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                'INSERT INTO payments (amount) VALUES (%(int)s);',
                {'int': 299}
            )
    return {"message": "success"}


@app.get("/payments")
async def get_payments() -> dict:
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                'SELECT id, amount, created_at FROM payments;'
            )
            res = cur.fetchall()

    d =  {'data': res, 'columns': ['id', 'pay_amount', 'date']}
    print(d)
    return d


def main() -> None:
    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
