from app import add, health


def test_add():
    assert add(2, 3) == 5


def test_health():
    result = health()
    assert result["status"] == "ok"
    assert result["service"] == "devops-command-center-test-app"
