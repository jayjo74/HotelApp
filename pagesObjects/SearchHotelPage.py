from selenium.webdriver.common.by import By

class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver

     # Locator
    location = (By.NAME, "location") #select
    hotels = (By.NAME, "hotels") #select
    roomType = (By.NAME, "room_type") #select
    numRoom = (By.NAME, "room_nos")
    checkInDate = (By.NAME, "datepick_in")
    checkOutDate = (By.NAME, "datepick_out")
    adultPerRoom = (By.NAME, "adult_room")
    childPerRoom = (By.NAME, "child_room")
    search = (By.NAME, "Submit")
    reset = (By.NAME, "Reset")

    #Actions
    def getLocation(self):
        return self.find_element(*SearchHotelPage.location)

    def getHotels(self):
        return self.find_element(*SearchHotelPage.hotels)

