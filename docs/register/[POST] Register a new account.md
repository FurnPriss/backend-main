# Register a New Account

A brief explanation of the API feature or endpoint.

- **🌏 URL**: `/api/register/`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
	> These variables should be passed as `plain string`
	- username: `required`, `min=6`
	- email: `required`
	- password: `required`, `min=8`

- **✉ Data Example**
	```json
	{
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
			"username": [
        		"This field may not be blank."
    		],
		}
		```
- **❓ Condition**: *If email didn't match with regex*
	- **🔢 Code**: `400 BAD REQUEST`
	- **✉ Content Example**:
		```json
		{
			"message": "Email must have a pattern '.com'.",
		}
		```
- **❓ Condition**: *If the email has been used.*
	- **🔢 Code**: `400 BAD REQUEST`
	- **✉ Content Example**:
		```json
		{
			"email": [
				"user model with this email already exists."
			]
		}
		```

### ✅ Success Response(s)
- **❓ Condition**: *If there is no validation error and the email is available.*
	- **🔢 Code**: `201 CREATED`
	- **✉ Content Example**:
		```json
		{
			"message": "You've created a new account.",
		}
		```
