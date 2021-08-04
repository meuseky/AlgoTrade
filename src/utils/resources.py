from pathlib import Path


def get_resources_path():
    module_path = Path(__file__).parent
    relative_path = '../../resources'
    resource_path = (module_path / relative_path).resolve()
    return resource_path


resources_path = get_resources_path()


def get_historical_data_path(instrument_type, ticker_symbol):
    relative_path = "historical_data/{}/{}".format(instrument_type, ticker_symbol)
    historical_data_path = (resources_path / relative_path).resolve()
    historical_data_path.mkdir(parents=True, exist_ok=True)
    return historical_data_path


def get_historical_data_filename(instrument_type, ticker_symbol):
    historical_data_path = get_historical_data_path(instrument_type, ticker_symbol)
    filename = "historical_data.csv"
    historical_data_filename = (historical_data_path / filename).resolve()
    return str(historical_data_filename)
