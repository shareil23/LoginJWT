# Mercari Code Test

Mercari Auth Exercise Code.

## Stack
|||
|----|-------|
|Language|Python|
|Framework|Flask|
|Database|Postgres|
|Cache|Redis|
|Container|Docker|
|Port Services Running|`8000`|
|Port Database Running|`7000`|


## Current Directory Structure
```bash
├── README.md
├── app.py
├── Documents
├── docker-compose.yml
├── manage.py
├── migration.sh
├── requirements.txt
└── src
    ├── Config
    ├── Controller
    ├── Models
    ├── Schema
    ├── Static
    ├── Templates
    ├── Test
    ├── InBound
    ├── OutBound
    ├── __init__.py

```

# How To Run The Services

```bash
docker-compose up
```

# How To Destroy The Services

```bash
docker-compose down --rmi local -v
```

# How To Run The Unitest

```bash
TBD
```

# Tech DEBT
- Add unit test
- Fix some error handling issue
- Fix the structure to repository model so no need to duplicate I/O type calling, and sepearate between business and tech logic
- Move from SQL to NoSQL to improve the performance
- Handling GRPC for every services that need check the authorization
- Separate env file for Dev, Staging, and Production
- Handling importing file using full path to avoid error
- Add caching mechanism for checking the token duration
