# This class is used in the python_requests_module give the user an appropriate response to their
# request, using the status code that will be returned.

class RequestResponse:
    def __init__(self, response):
        self.response = response

    def check_response_code(self):
        if self.response.status_code is 200:
            return "Successfully got a response from " + str(self.response.url) + "\n"
        elif self.response.status_code is 204:
            return "There was no content found at " + str(self.response.url) + "\n"
        elif self.response.status_code is 301:
            return "This URL has moved permanently " + str(self.response.url) + "\n"
        elif self.response.status_code is 400:
            return "Unrecognised request, perhaps there is a spelling mistake or error. in " + \
                   str(self.response.url) + "\n"
        elif self.response.status_code is 401:
            return "Unauthorized Access, incorrect credentials " + str(self.response.url) + "\n"
        elif self.response.status_code is 403:
            return "Forbidden access to resources available at " + str(self.response.url) + "\n"
        elif self.response.status_code is 404:
            return "No Page has been found, perhaps this resource has changed, double check." + \
                   str(self.response.url) + "\n"
        elif self.response.status_code is 500:
            return "Internal Server error has occured whilst connecting to " + str(self.response.url) + "\n"

