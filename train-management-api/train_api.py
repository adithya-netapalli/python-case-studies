from fastapi import FastAPI
app = FastAPI()

trains = [
    (12760, "Charminar Express", "Hyderabad", "Chennai", 650),
    (12723, "Telangana Express", "Hyderabad", "New Delhi", 1200),
    (17015, "Visakha Express", "Secunderabad", "Bhubaneswar", 850),
    (12701, "Hussain Sagar Express", "Mumbai", "Hyderabad", 700)
]

@app.get("/trains")
def get_all_trains():
    return trains
  
@app.get("/trains/{train_number}")
def search_train(train_number: int):

    for train in trains:
        if train[0] == train_number:
            return train

    return "Train not found"


@app.get("/trains/destination/{destination}")
def get_trains_by_destination(destination: str):

    result = []

    for train in trains:
        if train[3] == destination:
            result.append(train)

    return result


@app.get("/trains/cheapest")
def get_cheapest_train():

    cheapest = trains[0]

    for train in trains:
        if train[4] < cheapest[4]:
            cheapest = train

    return cheapest


@app.get("/trains/fare/{max_fare}")
def get_trains_by_fare(max_fare: int):
    result = []
    for train in trains:
        if train[4] <= max_fare:
            result.append(train)
    return result

@app.post("/trains")
def add_train( 
    train_number: int,
    train_name: str,
    source: str,
    destination: str,
    fare: int
):

    train = (train_number, train_name, source, destination, fare)
    trains.append(train)
    return "Train added successfully"
