# Register a New Account

A brief explanation of the API feature or endpoint.

- **🌏 URL**: `/register/`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
	> These variables should be `plain strings`.
	- name: `required`
	- username: `required`, `min=6`
	- email: `required`
	- password: `required`, `min=8`

- **✉ Data Example**
	```json
	{
		"name": "Ryuzaki Ramadansyah",
		"username": "ryuzakir",
		"email": "ryuzaki.ramadansyah@example.com",
		"password": "abcd1234"
	}
	```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If there is an invalid field that doesn't meet the data constraint (Validation Error).*
	- **🔢 Code**: `400 BAD REQUEST`
	- **✉ Content Example**:
		```json
		{
			"error": true,
			"message": "There are one or more error field(s). Please check it carefully.",
			"data": {
				"confirmPassword": "validation error message or an array to list the error occurred"
			}
		}
		```
- **❓ Condition**: *If the `email` is already used or the `username` is not available.*
	- **🔢 Code**: `409 CONFLICT`
	- **✉ Content Example**:
      - **❓ Condition**: *If the `email` is already used*
		```json
		{
			"error": true,
			"message": "The email has been used. Please try another one or login instead."
		}
		```
      - **❓ Condition**: *If the `username` is not available.*
		```json
		{
			"error": true,
			"message": "The username is not available. Please try another one or login instead."
		}
		```

### ✅ Success Response(s)
- **❓ Condition**: *If there is no validation error and the email is available.*
	- **🔢 Code**: `201 CREATED`
	- **✉ Content Example**:
		```json
		{
			"status": 201,
			"message": "You've created a new account.",
		}
		```
