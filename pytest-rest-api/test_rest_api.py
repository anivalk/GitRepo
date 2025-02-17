import pytest
from make_requests import make_request

def test_search_asteroids_with_sucess():
    # Arrange:
    base_url = "https://api.nasa.gov/neo/rest/v1/feed/"
    #Act:
    response = make_request(base_url)
    #Assertion:
    assert response.status_code == 404  # Validation of status code  
    data = response.json() 
    # Assertion of body response content:  
    assert len(data) > 0  
    #assert data["element_count"] > 0



   


    

   

 

   

    

