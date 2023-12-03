import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class CreateCafeteriaRequest(BaseModel):
    id: Annotated[int, Field(alias="id", ge=1)]
    name: Annotated[str, Field(max_length=50, alias="name")]
    campus_id: Annotated[int, Field(alias="campusID", ge=1)]
    latitude: Annotated[float, Field(alias="latitude", ge=-90, le=90)]
    longitude: Annotated[float, Field(alias="longitude", ge=-180, le=180)]

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "학생식당",
                "campusID": 1,
                "latitude": 37.123456,
                "longitude": 127.123456,
            },
        }


class UpdateCafeteriaRequest(BaseModel):
    name: Annotated[str, Field(max_length=50, alias="name")]
    latitude: Annotated[float, Field(alias="latitude", ge=-90, le=90)]
    longitude: Annotated[float, Field(alias="longitude", ge=-180, le=180)]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "학생식당",
                "latitude": 37.123456,
                "longitude": 127.123456,
            },
        }


class CreateCafeteriaMenuRequest(BaseModel):
    date: Annotated[datetime.date, Field(alias="date")]
    time: Annotated[str, Field(alias="time")]
    menu: Annotated[str, Field(alias="menu", max_length=400)]
    price: Annotated[str, Field(alias="price", max_length=30)]

    class Config:
        json_schema_extra = {
            "example": {
                "date": "2021-07-31",
                "time": "조식",
                "menu": "토스트",
                "price": "3000원",
            },
        }


class UpdateCafeteriaMenuRequest(BaseModel):
    price: Annotated[str, Field(alias="price", max_length=30)]

    class Config:
        json_schema_extra = {
            "example": {
                "price": "3000원",
            },
        }


class CafeteriaListItemResponse(BaseModel):
    cafeteria_id: Annotated[int, Field(alias="id", ge=1)]
    cafeteria_name: Annotated[str, Field(max_length=50, alias="name")]


class CafeteriaListResponse(BaseModel):
    data: Annotated[list["CafeteriaListItemResponse"], Field(alias="data")]


class CafeteriaDetailResponse(BaseModel):
    cafeteria_id: Annotated[int, Field(alias="id", ge=1)]
    cafeteria_name: Annotated[str, Field(max_length=50, alias="name")]
    latitude: Annotated[float, Field(alias="latitude", ge=-90, le=90)]
    longitude: Annotated[float, Field(alias="longitude", ge=-180, le=180)]


class CafeteriaMenuResponse(BaseModel):
    date: Annotated[datetime.date, Field(alias="date")]
    time: Annotated[str, Field(alias="time")]
    menu: Annotated[str, Field(alias="menu", max_length=400)]
    price: Annotated[str, Field(alias="price", max_length=30)]


class CafeteriaMenuListResponse(BaseModel):
    data: Annotated[list["CafeteriaMenuResponse"], Field(alias="data")]
