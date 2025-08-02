import asyncio
import logging

import aio_pika
import psycopg2
import uvicorn
from fastapi import FastAPI
from golden.microservice_schemas import PaymentsModel

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
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect_robust(
        config.rabbitmq_url, loop=loop
    )

    channel: aio_pika.abc.AbstractChannel = await connection.channel()

    data = PaymentsModel(
        user='user',
        amount='299'
    )

    await channel.default_exchange.publish(
        aio_pika.Message(
            body=data.model_dump_json().encode()
        ),
        routing_key=config.payments_queue_name
    )

    await connection.close()

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
    return d




def main() -> None:
    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
