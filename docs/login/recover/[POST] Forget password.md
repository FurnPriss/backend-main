# Forget Password

An endpoint to recover user account by entering the username or email of the user.

- **🌏 URL**: `/api/reset-psw/`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
  - email: `required`
    > - this variable should be a `plain text`.
    > - the api can define which email by checking the input as a valid email address and email has available on our database. Do this with form validation.


- **✉ Data Example**
  ```json
  {
    "email": "ryuzakir@gmail.com",
    "password": "djangorest",
    "confirm_password": "djangorest"
  }
  ```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If the filed password and confirm password not same or (Validation Error).*
  - **🔢 Code**: `400 BAD REQUEST`
  - **✉ Content Example**:
    ```json
    {
      "message": "Password must be same with confirm field" or "Please complete field on form",
    }
    ```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If the email isn't available on our database*
  - **🔢 Code**: `404 NOT FOUND`
  - **✉ Content Example**:
    ```json
    {
      "message": "Email isn't available on our database",
    }
    ```

### ❌ Error Response(s)
- **❓ Condition**: *error from django*
  - **🔢 Code**: `404 NOT FOUND`
  - **✉ Content Example**:
    ```json
    {
      "detail": "Email isn't available on our database",
    }
    ```

### ✅ Success Response(s)
- **❓ Condition**: *If there is no validation error.*
	- **🔢 Code**: `200 OK`
	- **✉ Content Example**:
		```json
		{
			"message": "We sent email to you. Please check your inbox",
		}
		```
