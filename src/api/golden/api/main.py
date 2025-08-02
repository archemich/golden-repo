import numpy as np
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/pay")
async def pay() -> dict[str, str]:
    return {"message": "Hello pay"}


@app.get("/payments")
async def get_payments() -> dict[str, list[int | float | str]]:
    d =  {'data': np.random.rand(50, 2).tolist(), 'columns': ['pay_amount', 'date']}
    return d


def main() -> None:
    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
