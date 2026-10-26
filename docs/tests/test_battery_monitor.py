# BATTEYE Test Cases

| Test ID | Test Condition | Input | Expected Result |
|---|---|---|---|
| TC01 | Normal battery | 12.6V, 4A, 30°C | Normal status |
| TC02 | Low voltage | 11.2V, 5A, 30°C | Low-voltage alert |
| TC03 | High temperature | 12.4V, 5A, 48°C | High-temperature alert |
| TC04 | High current | 12.2V, 12A, 32°C | High-current alert |
| TC05 | Multiple abnormal values | 11.1V, 12A, 48°C | Multiple alerts |
| TC06 | Normal recovery | 12.5V, 4A, 30°C | Normal status |
| TC07 | Invalid voltage | Negative/non-numeric value | Validation error |
| TC08 | Missing sensor data | Missing temperature | Data-validation error |

## Example Pytest Test

```python
def test_low_voltage():
    voltage = 11.2

    assert voltage < 11.5


def test_high_temperature():
    temperature = 48

    assert temperature > 45


def test_high_current():
    current = 12

    assert current > 10
```

Run the tests with:

```bash
pytest
```
