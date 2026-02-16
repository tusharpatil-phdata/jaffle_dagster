from dagster import asset, job, Definitions

@asset
def hello_asset():
    return "Hello from Dagster"

@job
def hello_job():
    hello_asset()

defs = Definitions(
    assets=[hello_asset],
    jobs=[hello_job],
)
