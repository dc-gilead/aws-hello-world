from test.unit.webapp import client

def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "Brian Carpio" in html
    assert "Is DevOps" in html
    assert landing.status_code == 200
