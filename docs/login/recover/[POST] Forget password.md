# Forget Password

An endpoint to recover user account by entering the username or email of the user.

- **🌏 URL**: `/login/recover`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
  - username-or-email: `required`, `min=6`
    > - this variable should be a `plain text`.
    > - the api can define which email or username by checking the input as a valid email address. Do this with form validation.


- **✉ Data Example**
  ```json
  {
    "username-or-email": "ryuzakir",
  }
  ```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If the filed doesn't meet the data constraints (Validation Error).*
  - **🔢 Code**: `400 BAD REQUEST`
  - **✉ Content Example**:
    ```json
    {
      "error": true,
      "message": "validation error message or an array to list the error occurred.",
    }
    ```

### ✅ Success Response(s)
- **❓ Condition**: *If there is no validation error.*
	- **🔢 Code**: `200 OK`
	- **✉ Content Example**:
		```json
		{
			"error": false,
			"message": "We will send you an email that contains an OTP if there is any account related.",
		}
		```
