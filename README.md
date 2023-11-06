# Sampo Price Estimation Service

This is a work in progress price estimation service for the [Sampo app](https://github.com/ohjelmistoprojekti-sampo/sampo).

## Prerequisites

- Python and `pip` are required.

## Installation

1. Clone the repository.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required Python packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Start the service:

	```
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
	```

5. Make a get request using a web browser or a tool like `curl`.

```
http://localhost:8000/estimate-price?item_description=yourItemDescription&condition=3
```