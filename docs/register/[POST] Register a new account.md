# Register a New Account

A brief explanation of the API feature or endpoint.

- **🌏 URL**: `/register`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
	> These variables should be passed as `plain string`
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
			"status": 400,
			"message": "There is an error related to the form. Please check carefully.",
		}
		```
- **❓ Condition**: *If the email has been used.*
	- **🔢 Code**: `500 NOT FOUND`
	- **✉ Content Example**:
		```json
		{
			"status": 500,
			"message": "Email has been used"
		}
		```

### ✅ Success Response(s)
- **❓ Condition**: *If there is no validation error and the username is available.*
	- **🔢 Code**: `201 CREATED`
	- **✉ Content Example**:
		```json
		{
			"status": 201,
			"message": "You've created a new account.",
		}
		```
