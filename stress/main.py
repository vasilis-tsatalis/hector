import typer
import urllib3
from concurrent.futures import ThreadPoolExecutor
import certifi
import datetime
import time
import logging

app = typer.Typer()

today = str(datetime.date.today())

http = urllib3.PoolManager(
    cert_reqs="CERT_NONE",
    ca_certs=certifi.where()
)

https = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

logging.basicConfig(
    filename=f'stress/logs/{today}_handler.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    )

@app.command("sequential")
def cli_one_to_one_requests(
    url: str, 
    runner: int = 1, 
    verify: bool = False,
    timeout: float = 0.0
    ):

    for i in range(runner):
        start_req = str(datetime.datetime.now())
        if verify == True:
            resp = https.request("GET", url)
        else:
            resp = http.request("GET", url)
        end_req = str(datetime.datetime.now())
        message = {
            "type": "sequential",
            "status": resp.status,
            "headers": resp.headers,
            "timestamp_start": start_req,
            "timestamp_end": end_req
        }
        logging.info(message)
        time.sleep(timeout)


# Function to fetch the URL
def fetch_url(url):
    try:
        start_req = str(datetime.datetime.now())

        resp = https.request("GET", url)

        end_req = str(datetime.datetime.now())

        message = {
            "type": "parallel",
            "status": resp.status,
            #"headers": resp.headers,
            "timestamp_start": start_req,
            "timestamp_end": end_req
        }
        return message
    except Exception as e:
        return None, str(e)


@app.command("parallel")
def cli_many_requests(
    url: str, 
    runner: int = 1, 
    booms: int = 1,
    verify: bool = False,
    timeout: float = 0.0
    ):

    for i in range(runner):

        start_req_pack = str(datetime.datetime.now())

        # Use ThreadPoolExecutor for parallel requests
        with ThreadPoolExecutor(max_workers=8) as executor:  # Adjust max_workers as needed
            # Submit the same URL multiple times
            results = list(executor.map(fetch_url, [url] * booms))

        end_req_pack = str(datetime.datetime.now())

        message = {
            "Runner Number": i,
            "Results": results,
            "timestamp_start": start_req_pack,
            "timestamp_end": end_req_pack
        }
        logging.info(message)

        time.sleep(timeout)


if __name__ == "__main__":
    app()