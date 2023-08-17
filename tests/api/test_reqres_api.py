from api_requests.api_requests import ReqresInApi
from api_validations.api_validations import Validations
import logging
import pytest

logger = logging.getLogger("api")


class TestSuitPositive:
    def test_get_list_users(self):
        response = ReqresInApi.get_list_users()
        request_method = response.request.method
        assert request_method == 'GET'
        assert Validations.valid_status_code(response, 200), "Status code not as expected."
        assert Validations.response_time(response, 600), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {600} ms."
        logger.info("Successful GET request(list_users)")

    parameters = [(2), (3)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_get_single_user(self, user_id):
        response = ReqresInApi.get_single_user(user_id)
        request_method = response.request.method
        assert request_method == 'GET'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.response_time(response, 600), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {600} ms."
        logger.info("Successful GET request(single_user)")

    parameters = [("Matthew", "programmer"), ("Steve", "designer"), ("Josh", "QA engineer")]

    @pytest.mark.parametrize("name,job", parameters)
    def test_create_new_user(self, name, job):
        response = ReqresInApi.create_new_user(name, job)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 201), \
            f"Error: status code is not correct. Expected: 201, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["name", "job", "id", "createdAt"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Successful POST request(create_new_user)")

    parameters = [("Steven", "developer", 2), ("Robert", "game designer", 3),
                  ("Mike", "Project Manager", 5)]

    @pytest.mark.parametrize("name,job,user_id", parameters)
    def test_update_user(self, name, job, user_id):
        response = ReqresInApi.update_user(name, job, user_id)
        request_method = response.request.method
        assert request_method == 'PUT'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["name", "job", "updatedAt"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Successful PUT request(update_user)")

    parameters = [(2), (3)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_delete_user(self, user_id):
        response = ReqresInApi.delete_user(user_id)
        request_method = response.request.method
        assert request_method == 'DELETE'
        assert Validations.valid_status_code(response, 204), \
            f"Error: status code is not correct. Expected: 204, Actual: {response.status_code}"
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Successful DELETE request")

    parameters = [("janet.weaver@reqres.in", "ReqRes"), ("emma.wong@reqres.in", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_user(self, username, password):
        response = ReqresInApi.register(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["id", "token"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 1000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {1000} ms."
        logger.info("Successful POST request(registration_user)")

    parameters = [("janet.weaver@reqres.in", "ReqRes"), ("emma.wong@reqres.in", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_login_user(self, username, password):
        response = ReqresInApi.login(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["token"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 1000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {1000} ms."
        logger.info("Successful POST request(login_user)")

    parameters = [(2), (3)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_get_user_avatar(self, user_id):
        response = ReqresInApi.get_single_user(user_id)
        request_method = response.request.method
        assert request_method == 'GET'
        assert response.json()['data']['avatar'] == f'https://reqres.in/img/faces/{user_id}-image.jpg', \
            'Avatar is not ok'

    def test_list_resource(self):
        response = ReqresInApi.get_list_resource()
        request_method = response.request.method
        assert request_method == 'GET'
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['page'] == 1
        assert response_body["per_page"] == 6
        assert response_body["total"] == 12

    parameters = [(2, "fuchsia rose"), (4, "aqua sky"), (5, "tigerlily")]

    @pytest.mark.parametrize("resource_id,name", parameters)
    def test_get_single_resource(self, resource_id, name):
        response = ReqresInApi.get_resource(resource_id)
        request_method = response.request.method
        assert request_method == 'GET'
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['data']['name'] == name


class TestSuitNegative:
    parameters = [(25), (35)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_get_invalid_single_user(self, user_id):
        response = ReqresInApi.get_single_user(user_id)
        request_method = response.request.method
        assert request_method == 'GET'
        assert Validations.valid_status_code(response, 404), \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Single user not found. Empty response.")

    parameters = [("", "ReqRes"), ("", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_without_email(self, username, password):
        response = ReqresInApi.register(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing email or username"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing email or username")

    parameters = [("janet.weaver@reqres.in", ""), ("emma.wong@reqres.in", "")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_without_password(self, username, password):
        response = ReqresInApi.register(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing password"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing password")

    parameters = [("", "ReqRes"), ("", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_login_without_email(self, username, password):
        response = ReqresInApi.login(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing email or username"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing email or username")

    parameters = [("janet.weaver@reqres.in", ""), ("emma.wong@reqres.in", "")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_login_without_password(self, username, password):
        response = ReqresInApi.login(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing password"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing password")

    parameters = [("123.weaver@reqres.in", "ReqRes"), ("emma150.wong@reqres.in", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_login_with_wrong_email(self, username, password):
        response = ReqresInApi.login(username, password)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Incorrect login or password")

# import requests
# import logging
# from utils.json_utils import change_json_values, write_response_to_file
# import json
# import jsonpath as jsonpath
# import pytest
#
# URL = "https://reqres.in/api/users"
# FILE_PATH = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/"
# logger = logging.getLogger("api")
#
#
# class Test_Reqres_API:
#     parameters = [("Test_User1", "programmer"), ("Test_User5", "designer"), ("Another_User", "HR")]
#
#     @pytest.mark.parametrize("name,job", parameters)
#     def test_create_user_post(self, name, job):
#         json_rq_path = f"{FILE_PATH}post/rq.json"
#         json_rs_path = f"{FILE_PATH}post/rs.json"
#         change_json_values(json_rq_path, name, job)
#         file = open(json_rq_path, 'r')
#         request_json = json.loads(file.read())
#         response_json = requests.post(URL, request_json)
#         assert response_json.status_code == 201, "Status code not 201"
#         res_json = json.loads(response_json.text)
#         write_response_to_file(json_rs_path, res_json)
#         file.close()
#         get_task_data = response_json.json()
#         assert get_task_data["name"] == name, "Values name are not equals"
#         assert get_task_data["job"] == job, "Values job are not equals"
#
#     parameters = [("Test_User1 Updated", "developer", 2), ("Test_User5 Updated", "game designer", 3),
#                   ("Another_User Updated", "HR manager", 4)]
#
#     @pytest.mark.parametrize("name,job,user_id", parameters)
#     def test_update_user_put(self, name, job, user_id):
#         url = f"{URL}/{user_id}"
#         json_rq_path = f"{FILE_PATH}put/rq.json"
#         json_rs_path = f"{FILE_PATH}put/rs.json"
#         change_json_values(json_rq_path, name, job)
#         file = open(json_rq_path, 'r')
#         request_json = json.loads(file.read())
#         response_json = requests.put(url, request_json)
#         assert response_json.status_code == 200, "Status code not 200"
#         res_json = json.loads(response_json.text)
#         write_response_to_file(json_rs_path, res_json)
#         file.close()
#         get_task_data = response_json.json()
#         assert get_task_data["name"] == name, "Values name are not equals"
#         assert get_task_data["job"] == job, "Values job are not equals"
#
#     parameters = [("total", 1, 12), ("total_pages", 2, 2)]
#
#     @pytest.mark.parametrize("param,page_number,expected_value", parameters)
#     def test_get_user(self, param, page_number, expected_value):
#         url = f"{URL}?page={page_number}"
#         json_rs_path = f"{FILE_PATH}get/rs.json"
#         response = requests.get(url)
#         assert response.status_code == 200, "Status code not 200"
#         response_json = json.loads(response.text)
#         write_response_to_file(json_rs_path, response_json)
#         pages = jsonpath.jsonpath(response_json, param)
#         assert pages[0] == expected_value, "Values are not equals"
#
#     parameters = [(2), (3)]
#
#     @pytest.mark.parametrize("user_id", parameters)
#     def test_delete_user(self, user_id):
#         url = f"{URL}/{user_id}"
#         response = requests.delete(url)
#         assert response.status_code == 204, "Status code not 204"
