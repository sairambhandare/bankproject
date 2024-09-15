# Bank Branch API (Django REST Framework)

This project is a RESTful API service built using Django and Django REST Framework for retrieving bank and branch information. It allows users to fetch a list of banks and details of a specific branch based on the branch's IFSC code.

## Features

- REST API endpoints to retrieve bank list and branch details.
- Simple and clear architecture using Django REST Framework.
- Test cases for API functionality.
- Instructions for running the project locally.
- Ready to be deployed on platforms like Heroku.

## Endpoints

- **GET /banks/** - Returns the list of all banks.
- **GET /branch/{ifsc}/** - Returns the branch details for a specific IFSC code.

---

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sairambhandare/bankproject.git
cd bankproject
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```
The API will now be available at `http://127.0.0.1:8000/`.


## API Endpoints

### 1. List of Banks

**Endpoint**: `/banks/`

**Method**: `GET`

**Description**: Retrieves a list of all banks available in the system.

**Request**: No parameters required.

**Response**:
- **Status Code**: `200 OK`
- **Response Body**:
  ```json
  [
      {
        "id": 1,
        "name": "STATE BANK OF INDIA"
      },
      {
        "id": 2,
        "name": "PUNJAB NATIONAL BANK"
      },
      {
        "id": 3,
        "name": "CANARA BANK"
      }
  ]
  ```

### 2. Branch Details by IFSC

**Endpoint**: `/branch/<ifsc>/`

**Method**: `GET`

**Description**: Retrieves the details of a specific branch using its IFSC code.

**Request**: 
- URL Parameter:
    - `ifsc`: The unique IFSC code of the branch.
- Sample Request:
    - URL: `/branch/BOFA0001234/`

**Response**:
- **Status Code**: `200 OK`
- **Response Body**:
  ```json
  {
    "ifsc": "ZSBL0000311",
    "bank": {
        "id": 101,
        "name": "ZILA SAHAKRI BANK LIMITED GHAZIABAD"
    },
    "branch": "VIJAYNAGAR",
    "address": "B 1,SEC 12 PRATAP VIHAR VIJAYNAGAR",
    "city": "GHAZIABAD",
    "district": "GHAZIABAD",
    "state": "UTTAR PRADESH"
  }
  ```
