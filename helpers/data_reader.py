from helpers.data_reader import DataReader

# Load JSON template
static_users = DataReader.read_json("static_payloads.json")
default_payload = static_users["default_user"]

# Load CSV records for pytest.mark.parametrize
csv_rows = DataReader.read_csv("users_test_data.csv")

# Load Excel scenarios
excel_rows = DataReader.read_excel("test_data.xlsx", sheet_name="Sheet1")