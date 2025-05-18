from mcp.server.fastmcp import FastMCP
import requests

# auto o cong 8000.
mcp = FastMCP(
    name="mcp-server",
)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Cộng hai số nguyên."""
    return a + b

@mcp.tool()
def get_current_temperature_by_city(city_name: str) -> float:
    """Lây nhiệt độ hiện tại của một thành phố từ OpenWeatherMap API."""
    api_key = "c836d09a9cda465c28b6d80817f3e4f0"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]
    else:
        raise ValueError(f"Error fetching temperature for {city_name}: {response.status_code}")
    
# Resource : Cung cấp tài nguyên nào đó
# Prompt: Querry lên để lấy 1 prompt cho 1 tình huống nào đó

@mcp.resource("resource://ma_so_thue")
def get_ma_so_thue() -> str:
    """Lấy mã số thuế của công ty"""
    return "1800278630"

@mcp.resource("resource://say_hi/{name}")
def say_hi(name: str) -> str:
    """Nói xin chào với tên được cung cấp"""
    return "Hello {}".format(name)

@mcp.prompt()
def review_sentence(sentence: str) -> str:
    return "Review this sentence, remove any personal information: \n\n{}".format(sentence)

if __name__ == "__main__":
    # Initialize and run the server
    # print("Listening...")
    # mcp.run(transport='stdio')
    mcp.run(transport='sse')
