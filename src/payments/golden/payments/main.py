import asyncio
import aio_pika
import aio_pika.abc

import psycopg2

from golden.microservice_schemas import PaymentsModel
from .configuration import Configuration


#
# @app.get("/pay")
# async def pay() -> dict[str, str]:
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(
#                 'INSERT INTO payments (amount) VALUES (%(int)s);',
#                 {'int': 299}
#             )
#     return {"message": "success"}
#


async def _main(loop):
    config = Configuration()
    conn = psycopg2.connect(config.db_url)

    connection = await aio_pika.connect_robust(
        config.rabbitmq_url, loop=loop
    )
    async with connection:
        # Create a channel
        channel = await connection.channel()
        queue = await channel.declare_queue(
            config.payments_queue_name,  # Replace with your queue name
            durable=True,           # If the queue is durable
            auto_delete=False       # If the queue should auto-delete
        )
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    data = PaymentsModel.model_validate_json(message.body.decode())
                    with conn:
                        with conn.cursor() as cur:
                            cur.execute(
                                'INSERT INTO payments (amount) VALUES (%(int)s);',
                                {'int': data.amount}                                    )
def main() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_main(loop))
    loop.close()

if __name__ == '__main__':
    main()
