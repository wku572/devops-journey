from unittest.mock import MagicMock

import pytest
import requests

import fetch_github


def make_response(json_data=None, error=None):
    response = MagicMock()
    response.json.return_value = json_data
    if error:
        response.raise_for_status.side_effect = error
    return response


def test_fetch_profile_returns_json(monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    fake = make_response({"login": "octocat", "public_repos": 8})
    monkeypatch.setattr(fetch_github.requests, "get", lambda *a, **k: fake)

    data = fetch_github.fetch_profile("octocat")

    assert data["login"] == "octocat"
    assert data["public_repos"] == 8


def test_fetch_profile_raises_on_http_error(monkeypatch):
    error = requests.exceptions.HTTPError("404 Not Found")
    fake = make_response(error=error)
    monkeypatch.setattr(fetch_github.requests, "get", lambda *a, **k: fake)

    with pytest.raises(requests.exceptions.HTTPError):
        fetch_github.fetch_profile("no-such-user")


def test_fetch_profile_sends_token(monkeypatch):
    captured = {}

    def fake_get(url, headers=None, timeout=None):
        captured["url"] = url
        captured["headers"] = headers
        return make_response({"login": "octocat"})

    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    monkeypatch.setattr(fetch_github.requests, "get", fake_get)

    fetch_github.fetch_profile("octocat")

    assert captured["url"].endswith("/users/octocat")
    assert captured["headers"]["Authorization"] == "Bearer test-token"


def test_main_exits_1_on_http_error(monkeypatch, capsys):
    def boom(username):
        raise requests.exceptions.HTTPError("404")

    monkeypatch.setattr(fetch_github, "fetch_profile", boom)
    monkeypatch.setattr("sys.argv", ["fetch_github.py", "someone"])

    with pytest.raises(SystemExit) as exc:
        fetch_github.main()

    assert exc.value.code == 1
    assert "HTTP error" in capsys.readouterr().out
