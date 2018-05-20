"""Weather app."""
import requests
import bs4
import collections


WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    """Put everything in motion."""
    print_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


def print_header():
    """Print the header."""
    print('-------------------------------------------')
    print('              WEATHER APP')
    print('-------------------------------------------')
    print()


def get_html_from_web(zipcode):
    """Get the html from the requested url."""
    url = 'https://www.wunderground.com/weather/us/or/portland/{}'.format(
        zipcode)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    """Parse the received html."""
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(
        class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(
        class_='wu-unit-temperature').find(class_='wu-label').get_text()
    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_and_state_from_location(loc: str):
    """Do something to the state and location."""
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    """Clean the text."""
    if not text:
        return text
    text = text.strip()
    return text


if __name__ == __name__:
    main()