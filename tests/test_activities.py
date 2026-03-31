def test_get_activities_returns_seeded_activity_data(client, activities_state):
    # Arrange
    expected_activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity_name in payload
    assert payload[expected_activity_name]["description"] == activities_state[expected_activity_name]["description"]
    assert payload[expected_activity_name]["schedule"] == activities_state[expected_activity_name]["schedule"]
    assert payload[expected_activity_name]["max_participants"] == activities_state[expected_activity_name]["max_participants"]
    assert payload[expected_activity_name]["participants"] == activities_state[expected_activity_name]["participants"]