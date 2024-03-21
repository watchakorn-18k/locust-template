from locust import HttpUser, task, between

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA5MzI2ODEsImlhdCI6MTcxMDkxMTA4MSwibmJmIjoxNzEwOTExMDgxLCJ1aWQiOiIwNzRmNjIyNS02MDg2LTVkYjctYTQyNS02MmU3M2I2N2I2YjYiLCJ1c2VyX2lkIjoiTVpqQ3JLSTNrSk9EYTIzMFlvUWp5ZGZoc3RHMyJ9.TICJZmCQjak4pnXFsAZT3QcnlxSVz47dBFRRK1L-pB0"


data_payload = [
    {"method": "get", "endpoint": "/generate_invite_coupon"},
    {
        "method": "post",
        "endpoint": "/generate_pin_coupon",
        "payload": {
            "prefix": "Compare",
            "pin_count": 20,
            "uses": 10,
            "point_coupon": 100,
            "timestamp": "2030-06-16",
            "jwt_pass": "",
        },
    },
    {
        "method": "post",
        "endpoint": "/check_coupon",
        "payload": {"coupon_name": "TESTECHO4Y5V37RU"},
    },
    {
        "method": "post",
        "endpoint": "/check_invite_coupon",
        "payload": {"invite_code": "RMCF20BC23BA5RJMTSQE"},
    },
]


class LoadTesting(HttpUser):
    wait_time = between(0.5, 1.5)

    def on_start(self):
        self.client.headers = {"Authorization": f"Bearer {token}"}

    @task
    def test(self):
        for i in data_payload:
            self.client.request_name = i["endpoint"]
            if i["method"] == "get":
                self.client.get(i["endpoint"])
            else:
                self.client.post(i["endpoint"], json=i["payload"])

    # @task
    # def generate_pin_coupon(self):
    #     self.client.post(
    #         "/generate_pin_coupon",
    #         json={
    #             "prefix": "Compare",
    #             "pin_count": 20,
    #             "uses": 10,
    #             "point_coupon": 100,
    #             "timestamp": "2030-06-16",
    #             "jwt_pass": "",
    #         },
    #     )

    # @task
    # def check_coupon(self):
    #     # print(dir(self.client))
    #     self.client.request_name = "test"
    #     self.client.post(
    #         "/check_coupon",
    #         json={"coupon_name": "TESTECHO4Y5V37RU"},
    #     )
    #     time.sleep(500)

    # @task
    # def check_invite_coupon(self):
    #     self.client.post(
    #         "/check_invite_coupon",
    #         json={"invite_code": "RMCF20BC23BA5RJMTSQE"},
    #     )
