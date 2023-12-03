# Sampo Price Estimation Service

This is a price estimation service for the [Sampo app](https://github.com/ohjelmistoprojekti-sampo/sampo). The service fetches the relevant data by item description from a MongoDB database and gives a price estimation according to the item's condition that is described with values 1-5.

## Built with

* Python
  * scikit-learn
  * pandas
  * numpy
  * matplotlib
* [FastAPI](https://fastapi.tiangolo.com/)
* MongoDB
* Docker


## Prerequisites

- Python and `pip` are required.
- For the database functionality a MongoDB database with item listing data is needed. [Sampo scraper service](https://github.com/ohjelmistoprojekti-sampo/Scrape/) can be used to gather data.

## Installation

1. Clone the repository.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required Python packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Configure MongoDB in a .env file. Alternatively you can use the sample data
generator to generate data in price estimator.

5. Start the service:

	```
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
	```

## Usage

### REST service

Make a get request using a web browser or a tool like `curl`.

   ```
   http://localhost:8000/estimate-price?item_description=yourItemDescription&condition=3
   ```

### Estimation plotting
   
Alternatively plot_estimation.py can be used from the commandline:

```
python3 app/plot_estimation.py yourItemDescription 3
```

The graph is saved as a file in the `/app` directory.


