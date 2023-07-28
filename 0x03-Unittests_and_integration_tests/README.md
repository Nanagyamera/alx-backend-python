Unit Testing and Integration Testing

This repository contains the implementation of unit tests and integration tests for a Python application. The tests are organized into different test classes, and they cover various functions and methods of the application. The testing is carried out using the Python unittest library, parameterized for parameterized testing, and unittest.mock.patch for mocking external calls and methods.

Test Cases

TestAccessNestedMap

This test class covers the access_nested_map function from the utils module. The test cases verify that the function correctly accesses values from a nested dictionary based on the provided path.

test_access_nested_map: Tests the access_nested_map function for different inputs using parameterized and checks if it returns the expected results.
test_access_nested_map_exception: Tests that the access_nested_map function raises a KeyError when an invalid path is provided.

TestGetJson

This test class covers the get_json function from the utils module, which retrieves JSON data from a URL.

test_get_json: Tests the get_json function by mocking external HTTP calls using unittest.mock.patch. The test checks if the function returns the expected JSON payload for different URLs.

TestMemoize

This test class covers the memoize decorator from the utils module, which provides memoization functionality.

test_memoize: Tests the memoize decorator by mocking the underlying method using unittest.mock.patch. The test verifies that the decorated method is only called once, even when accessed multiple times.

TestGithubOrgClient

This test class covers the GithubOrgClient class, which interacts with the GitHub API to retrieve organization data.

test_org: Tests the org property of GithubOrgClient by mocking the get_json method. The test checks if the property returns the correct organization data for different organization names.

test_public_repos_url: Tests the _public_repos_url method of GithubOrgClient by mocking the org property. The test ensures that the method returns the expected repository URL.

test_public_repos: Tests the public_repos method of GithubOrgClient by mocking both the get_json and _public_repos_url methods. The test verifies that the method returns the correct list of public repositories.

test_has_license: Tests the has_license method of GithubOrgClient with different input scenarios to verify if it correctly checks for the presence of a specific license in a repository.

TestIntegrationGithubOrgClient

This test class covers the integration testing of the GithubOrgClient class. It uses fixtures to mock external API calls.

test_integration_public_repos: Integration tests for the public_repos method of GithubOrgClient. The test verifies that the method returns the expected repository data based on the provided fixtures.
