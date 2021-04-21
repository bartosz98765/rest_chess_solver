def test_moves_invalid_figure(client):
    # invalid figure
    response = client.get("/api/v1/invalid_figure/a1")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Figure does not exist."


def test_validation_invalid_figure(client):
    # invalid figure
    response = client.get("/api/v1/invalid_figure/a1/a2")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Figure does not exist."


def test_moves_king(client):
    # correct query
    response = client.get("/api/v1/king/a1")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": ["A2", "B1", "B2"],
        "currentField": "A1",
        "error": None,
        "figure": "king",
    }
    # invalid field
    response = client.get("/api/v1/king/invalid_field")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."


def test_validation_king(client):
    # correct KING move
    assert client.get("/api/v1/king/a1/a2").status_code == 200
    # invalid field
    response = client.get("/api/v1/king/a1/invalid_field")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."
    # incorrect KING move
    response = client.get("/api/v1/king/a1/a3")
    assert response.status_code == 200
    assert response.get_json()["error"] == "Current move is not permitted"


def test_moves_queen(client):
    # correct query
    response = client.get("/api/v1/queen/a1")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": [
            "A2",
            "A3",
            "A4",
            "A5",
            "A6",
            "A7",
            "A8",
            "B1",
            "B2",
            "C1",
            "C3",
            "D1",
            "D4",
            "E1",
            "E5",
            "F1",
            "F6",
            "G1",
            "G7",
            "H1",
            "H8",
        ],
        "currentField": "A1",
        "error": None,
        "figure": "queen",
    }
    # invalid field
    response = client.get("/api/v1/queen/h9")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."


def test_validation_queen(client):
    # correct move
    response = client.get("/api/v1/queen/d1/d2")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "D1",
        "destField": "D2",
        "error": None,
        "figure": "queen",
        "move": "valid",
    }
    # invalid field
    response = client.get("/api/v1/queen/A11/b8")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."
    # incorrect move
    response = client.get("/api/v1/queen/a1/b3")
    assert response.status_code == 200
    assert response.get_json()["error"] == "Current move is not permitted"


def test_moves_rook(client):
    # correct query
    response = client.get("/api/v1/rook/h8")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": [
            "A8",
            "B8",
            "C8",
            "D8",
            "E8",
            "F8",
            "G8",
            "H1",
            "H2",
            "H3",
            "H4",
            "H5",
            "H6",
            "H7",
        ],
        "currentField": "H8",
        "error": None,
        "figure": "rook",
    }
    # invalid field
    response = client.get("/api/v1/rook/a9")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."


def test_validation_rook(client):
    # correct move
    response = client.get("/api/v1/rook/a1/a8")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "A1",
        "destField": "A8",
        "error": None,
        "figure": "rook",
        "move": "valid",
    }
    # invalid field
    response = client.get("/api/v1/rook/b3/r8")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."
    # incorrect move
    response = client.get("/api/v1/rook/h8/a1")
    assert response.status_code == 200
    assert response.get_json()["error"] == "Current move is not permitted"


def test_moves_bishop(client):
    # correct query
    response = client.get("/api/v1/bishop/h1")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": ["A8", "B7", "C6", "D5", "E4", "F3", "G2"],
        "currentField": "H1",
        "error": None,
        "figure": "bishop",
    }
    # invalid field
    response = client.get("/api/v1/bishop/a0")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."


def test_validation_bishop(client):
    # correct move
    response = client.get("/api/v1/bishop/h1/a8")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "H1",
        "destField": "A8",
        "error": None,
        "figure": "bishop",
        "move": "valid",
    }
    # invalid field
    response = client.get("/api/v1/bishop/h9/h8")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."
    # incorrect move
    response = client.get("/api/v1/bishop/h8/h7")
    assert response.status_code == 200
    assert response.get_json()["error"] == "Current move is not permitted"


def test_moves_knight(client):
    # correct query
    response = client.get("/api/v1/knight/a8")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": ["B6", "C7"],
        "currentField": "A8",
        "error": None,
        "figure": "knight",
    }
    # invalid field
    response = client.get("/api/v1/knight/a15")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."


def test_validation_knight(client):
    # correct move
    response = client.get("/api/v1/knight/h1/f2")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "H1",
        "destField": "F2",
        "error": None,
        "figure": "knight",
        "move": "valid",
    }
    # invalid field
    response = client.get("/api/v1/knight/a3/8h")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."
    # incorrect move
    response = client.get("/api/v1/knight/h8/h7")
    assert response.status_code == 200
    assert response.get_json()["error"] == "Current move is not permitted"


def test_moves_pawn(client):
    # correct query for WHITE pawn
    # FIRST MOVE (START_MOVE_OFFSET)
    response = client.get("/api/v1/pawn/a2")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": ["A3", "A4"],
        "currentField": "A2",
        "error": None,
        "figure": "pawn",
    }
    # NEXT MOVE (MOVE_OFFSET)
    response = client.get("/api/v1/pawn/b3")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": ["B4"],
        "currentField": "B3",
        "error": None,
        "figure": "pawn",
    }
    # WHITE PAWN CAN'T STAND IN THE FIELD ON THE FIRST ROW - return empty list
    response = client.get("/api/v1/pawn/c1")
    assert response.status_code == 200
    assert response.get_json() == {
        "availableMoves": [],
        "currentField": "C1",
        "error": None,
        "figure": "pawn",
    }

    # invalid field (uppercase: e.g. A5)
    response = client.get("/api/v1/pawn/A5")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."


def test_validation_pawn(client):
    # correct query for WHITE pawn
    # FIRST MOVE (START_MOVE_OFFSET)
    response = client.get("/api/v1/pawn/d2/d4")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "D2",
        "destField": "D4",
        "error": None,
        "figure": "pawn",
        "move": "valid",
    }
    # NEXT MOVE (MOVE_OFFSET)
    response = client.get("/api/v1/pawn/d3/d4")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "D3",
        "destField": "D4",
        "error": None,
        "figure": "pawn",
        "move": "valid",
    }
    # WHITE PAWN CAN'T STAND IN THE FIELD ON THE FIRST ROW
    response = client.get("/api/v1/pawn/d1/d2")
    assert response.status_code == 200
    assert response.get_json() == {
        "currentField": "D1",
        "destField": "D2",
        "error": "Current move is not permitted",
        "figure": "pawn",
        "move": "invalid",
    }
    # invalid field
    response = client.get("/api/v1/pawn/3a/h1")
    assert response.status_code == 409
    assert response.get_json()["error"] == "Field does not exist."
    # incorrect move
    response = client.get("/api/v1/pawn/e6/h6")
    assert response.status_code == 200
    assert response.get_json()["error"] == "Current move is not permitted"
