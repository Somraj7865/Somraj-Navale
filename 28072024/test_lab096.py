# PUT
# URL
# Path - Bookinf ID
# Token - Auth
# Payload

import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests


def test_put_request_postive1(create_token,create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking)
    PUT_URL = base_url+base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Rohini",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Rohini"

def test_put_request_postive2(create_token,create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking)
    PUT_URL = base_url+base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }


    json_payload = {
        "firstname": "Ria",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Ria"

#
# def test_delete():
#     URL = "https://restful-booker.herokuapp.com/booking/"
#     booking_id = create_booking()
#     DELETE_URL = URL + str(booking_id)
#     cookie_value = "token=" + create_token()
#     headers = {
#         "Content-Type": "application/json",
#         "Cookie": cookie_value
#     }
#     print(headers)
#
#     response = requests.delete(url=DELETE_URL, headers=headers)