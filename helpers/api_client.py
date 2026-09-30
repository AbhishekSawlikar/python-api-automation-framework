import json
import requests
import allure


class APIClient:
    def __init__(self, base_url: str, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.timeout = timeout
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _log_and_attach(self, method: str, url: str, response: requests.Response, payload=None):
        req_details = f"METHOD: {method}\nURL: {url}\nHEADERS:\n{json.dumps(dict(self.session.headers), indent=2)}"
        if payload:
            req_details += f"\nPAYLOAD:\n{json.dumps(payload, indent=2)}"
        allure.attach(req_details, name="API Request", attachment_type=allure.attachment_type.TEXT)

        res_details = f"STATUS: {response.status_code}\nBODY:\n{response.text}"
        allure.attach(res_details, name="API Response", attachment_type=allure.attachment_type.JSON)

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        payload = kwargs.get("json") or kwargs.get("data")

        response = self.session.request(method, url, **kwargs)
        self._log_and_attach(method, url, response, payload)
        return response

    def get(self, endpoint: str, params=None, **kwargs):
        return self.request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json=None, **kwargs):
        return self.request("POST", endpoint, json=json, **kwargs)

    def put(self, endpoint: str, json=None, **kwargs):
        return self.request("PUT", endpoint, json=json, **kwargs)

    def patch(self, endpoint: str, json=None, **kwargs):
        return self.request("PATCH", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)