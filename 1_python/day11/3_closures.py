def create_rate_limiter(max_calls):
    counter = 0

    def check_limit():
        nonlocal counter
        if counter >= max_calls:
            raise Exception("Number of tries exceeded limit, try again after some time")
        counter += 1

    return check_limit




if __name__ == "__main__":
    api_limiter = create_rate_limiter(3)

    api_limiter()  # Allowed
    api_limiter()  # Allowed
    api_limiter()  # Allowed
    api_limiter()  # Raises exception
