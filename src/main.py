from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/estimate-price")
async def estimate_price(
    item_description: str = Query(..., description="Description of the item"),
    condition: int = Query(..., description="Condition of the item (1-5)", ge=1, le=5)
):

    item_description = item_description
    condition = condition

    # TODO:
    # 1. Get relevant dataset matching item_description from database
    # 2. Estimate price using the dataset and condition

    # to see if the parameters are working correctly
    print(f"Item description: {item_description}, Condition: {condition}")
    # placeholder value, replace with price estimation function
    return {"price": 42}
