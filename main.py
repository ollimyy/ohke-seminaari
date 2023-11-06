from fastapi import FastAPI, Query
from src.price_estimator import estimate_price_from_condition

app = FastAPI()

@app.get("/estimate-price")
async def estimate_price(
    item_description: str = Query(..., description="Description of the item"),
    condition: int = Query(..., description="Condition of the item (1-5)", ge=1, le=5)
):

    item_description = item_description
    condition = condition

    price_estimate = estimate_price_from_condition(condition)

    return price_estimate