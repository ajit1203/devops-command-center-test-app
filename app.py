def add(a, b):
    return a + b


def health():
    return {"status": "ok", "service": "devops-command-center-test-app"}


if __name__ == "__main__":
    print(health())
