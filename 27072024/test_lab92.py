import allure
import pytest
import requests


@allure.title("Create Booking CRUD")
@allure.description("TC01 - Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    URL=base_url+base_path
    headers={"Content-Type" : "application/json"}
    payload={

            "firstname": "Somraj",
            "lastname": "Navale",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    response=requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code==200
    responseData=response.json()

    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] >0
    assert type(responseData["bookingid"]) == int
    firstname=responseData["booking"]["firstname"]
    assert firstname=="Somraj"