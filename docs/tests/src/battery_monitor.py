def test_low_voltage():
    voltage = 11.2

    assert voltage < 11.5


def test_high_temperature():
    temperature = 48

    assert temperature > 45


def test_high_current():
    current = 12

    assert current > 10
