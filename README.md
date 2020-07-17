# Flight Optimizer Server

## About the project

`Flight-Optimizer` is a service that searches for the cheapest flights based on price per kilometer criteria.

### Information about Django server-side

- Server side is deployed to **Heroku services**: https://flight-optimizer-server.herokuapp.com/

- **Github actions** were used as **CI / CD** for this project.  

- **All build and deployment statuses** of the server can be found [on project's Github Actions](https://github.com/erikduisheev/flight-optimizer-server/actions).

### Information about `flight-optimizer` python package

Python package that searches these specific flights (and also provides CLI for that):
- Is published on **PYPI**: https://pypi.org/project/flight-optimizer/

- The source code of CLI package can be found [here](https://github.com/erikduisheev/flight-optimizer).

- Build and publishment statuses of CLI package is [here](https://github.com/erikduisheev/flight-optimizer/actions).

### Information about client-side

Front-end is deployed to the **AWS Amplify** services: https://deployment.dkbw81rcej2op.amplifyapp.com/

The source code of front-end can be found [here](https://github.com/erikduisheev/flight-optimizer-frontend).

### Credits

`Flight-Optimizer` was developed by inspiration from [B12 Team](https://www.b12.io/about).


## Environment variables

| NAME                  | EXAMPLE              | DESCRIPTION                                        |
| --------------------- | ---------            | -------------------------------------------------- |
| SECRET_KEY            | secret               | A secret key for a particular Django installation. |
| DEBUG                 | true                 | Flag that turns on debug mode. `true` or `false`   |
| DJANGO_SETTINGS_MODULE| optimizer.settings   | Name of the settings module                        |
| ALLOWED_HOSTS         | *                    | List of allowed hosts, separated by white space " "      |
| DATABASE_URL          | postgres://user:password@localhost:5432/db_name           | Database connection URL                          |

## Installation guide

### Running with docker

Specify environment variables. Example is provided in the above section.

Build and run the docker container, using next command: 
```
docker-compose up --build
```

Server will be up and running on the port 5000

To get into the container, run:
```
docker exec -it db_name sh
```

### Setup your users

Create a superuser account:  
```
python manage.py createsuperuser
```

Create migrations:
 
```
python manage.py makemigrations
```

Apply migrations:
 
```
python manage.py migrate
```

## How to use

###There are two endpoints:

#### 1) `flights` endpoint:

```
GET /api/flights?from=paris&to=london&to=bishkek
```

Possible response:
```json
{
    "departure": {
        "city": "Paris",
        "airport": "Paris Orly"
    },
    "destinations": [
        {
            "city": "London",
            "airport": "Heathrow",
            "price": 175,
            "distance": "367",
            "price_per_km": "0.48",
            "is_reachable": true
        },
        {
            "city": "Bishkek",
            "is_reachable": false
        }
    ]
}
```

In the response there will be a list of destinations. If there is no flights to some destination, then `is_reachable` key will be false. Otherwise it will have additional fields such as `airport`, `price`, `distance` and `price_per_km`. 


#### 2) `locations` endpoint:

```
GET /api/locations?city=par
```
It returns all possible cities from user's input. This data is going to be used for suggesting to user some possible cities based on his/her input.

Possible response:
```json
{
    "city": "par",
    "possible_cities": [
        {
            "city": "Paris",
            "country": "France"
        },
        {
            "city": "Parikia",
            "country": "Greece"
        },
        {
            "city": "Saint Andrew Parish",
            "country": "Dominica"
        },
        {
            "city": "Paramaribo",
            "country": "Suriname"
        }
    ]
}
```  

If there is no such city, `possible cities` list will be empty. 