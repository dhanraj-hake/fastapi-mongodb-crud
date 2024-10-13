
# FastAPI MongoDB Application

This is a FastAPI application that uses MongoDB as its database. The app provides APIs for managing Items and User Clock-In Records.

## How to Run the Project

1. Clone the Repository:
```
git clone https://github.com/dhanraj-hake/fastapi-mongodb-crud.git
```

```
cd fastapi-mongodb-crud
```

2. Create `.env` File:
In the root of the project directory, create a `.env` file. Add your MongoDB connection URI (replace with your actual MongoDB URI):
```
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/retryWrites=true&w=majority&appName=Cluster0
```

3. Install Dependencies:
```
pip install -r requirements.txt
```

4. Run the FastAPI Development Server:
```
fastapi dev
```


- The app will be running at http://127.0.0.1:8000.
- Open your browser and go to http://127.0.0.1:8000/docs to access the FastAPI Swagger UI for API testing.



## Available Endpoints

### Items API:
- **POST /items**: Create a new item.
- **GET /items/{id}**: Retrieve an item by ID.
- **GET /items/filter**: Filter items by:
  - Email (exact match).
  - Expiry Date (items expiring after the provided date).
  - Insert Date (items inserted after the provided date).
  - Quantity (items with quantity greater than or equal to the provided number).
- **GET /items/aggregate**: Aggregate data to return the count of items for each email (grouped by email).
- **PUT /items/{id}**: Update an item’s details by ID (excluding the Insert Date).
- **DELETE /items/{id}**: Delete an item based on its ID.


### User Clock-In Records API:
- **POST /clock-in**: Create a new clock-in entry.
- **GET /clock-in/{id}**: Retrieve a clock-in record by ID.
- **GET /clock-in/filter**: Filter clock-in records by:
  - Email (exact match).
  - Location (exact match).
  - Insert DateTime (clock-ins after the provided date).
- **PUT /clock-in/{id}**: Update a clock-in record by ID (excluding Insert DateTime).
- **DELETE /clock-in/{id}**: Delete a clock-in record based on its ID.
