from prefect import flow

@flow
def my_flow():
    print("HI")

my_flow()
