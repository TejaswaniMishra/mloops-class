# import TestClient so we can send simulated HTTP request directly to the FastAPI app
from fastapi.testclient import TestClient
# import the application object from main.py
from main import app 

# create a rerusable TestClient instance for all test functions 
client = TestClient(app)

def test_health_check():
    # verify that the app is running and /health endpoint is working correctly
    # send a GET request to the /health endpoint
    response = client.get("/health")
    # assert that the response status code is 200 (successful status code )
    assert response.status_code == 200
    # assert that the response JSON matches the expected output
    assert response.json() == {"status": "healthy "} 

def test_valid_iris_prediction():
    # verify that the /predict endpoint returns the correct prediction for valid input data
    # send a POST request to the /predict endpoint with valid input data
    payload={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    # assert that the response status code is 200 (successful status code )
    assert response.status_code == 200 
    result = response.json() # convert the json response to a Python dictionary

    # assert that the response JSON contains the expected keys and values
    assert "prediction" in result
    assert "class_name" in result

    # the predicted cllass for the given input data should be one of the three iris classes
    assert result["class_name"] in ["setosa", "versicolor", "virginica"]    

    assert result["prediction"] in [0, 1, 2]  # the predicted class index should be 0, 1, or 2

def test_invalid_iris_input():
    # verify that the /predict endpoint returns an error for invalid input data
    # send a POST request to the /predict endpoint with invalid input data (negative values)
    payload={
        "sepal_length": -5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    # assert that the response status code is 422 (Unprocessable Entity) for validation errors
    assert response.status_code == 422