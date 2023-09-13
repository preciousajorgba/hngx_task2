import requests

# Define the base URL of your FastAPI API
base_url = "https://hngx-task2-qh6l.onrender.com"

# Helper function to print response or errors
def print_response(response):
    if response.status_code == 200:
        print("Response:")
        print(response.json())
    else:
        print("Error. Status code:", response.status_code)
        print("Response content:", response.text)

# Create a new user
def create_user():
    url = f"{base_url}/api/"
    data = {
        "name": "odin"
    }
    response = requests.post(url, json=data)
    print("Create User:")
    print_response(response)

# Read all users
def read_all_users():
    url = f"{base_url}/api/"
    response = requests.get(url)
    print("Read All Users:")
    print_response(response)

# Read a single user by ID
def read_user(user_id):
    url = f"{base_url}/api/{user_id}/"
    response = requests.get(url)
    print(f"Read User ID {user_id}:")
    print_response(response)

# Update a user by ID
def update_user(user_id):
    url = f"{base_url}/api/{user_id}/"
    data = {
        "name": "Updated Name"
    }
    response = requests.put(url, json=data)
    print(f"Update User ID {user_id}:")
    print_response(response)

# Delete a user by ID
def delete_user(user_id):
    url = f"{base_url}/api/{user_id}/"
    response = requests.delete(url)
    print(f"Delete User ID {user_id}:")
    print_response(response)

if __name__ == "__main__":
    # Example usage:
    create_user()
    read_all_users()
    read_user(1)  # Replace with an existing user's ID
    update_user(1)  # Replace with an existing user's ID
    delete_user(1)  # Replace with an existing user's ID
