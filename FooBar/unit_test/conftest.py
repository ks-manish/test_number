import pytest
from selenium import webdriver


@pytest.fixture(params=["Chrome"], scope="session")
def driver_get(request):
    web_drivers = {"Chrome": webdriver.Chrome()}
    web_driver = web_drivers[request.param]
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
    yield
    web_driver.close()
