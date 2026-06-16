def test_login():
    assert login("admin", "12345") == True
    assert login("user", "wrong") == False
    print("All tests passed!")
