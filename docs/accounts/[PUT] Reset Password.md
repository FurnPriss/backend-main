# [POST] Reset Password

The token received in the user's email will be used in this endpoint. They'll input the token and the new password into their account.

- **🌏 URL**: `/login/accounts/`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `PUT`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
  > these variable should be a `plain text`.
  - token: `required`
    > - the single-use token received from the user's email.
  - newPassword: `required`, `min=8`, `newPassword!=oldPassword`
    > - the new password should be different from the old password.
  - confirmPassword: `required`, `min=8`, `confirmPassword==newPassword`
    > - the confirmPassword should have the same value with the newPassword.


- **✉ Data Example**
  - **❓ Condition**: *If the user enter the username.*
    ```json
    {
      "token": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d",
      "newPassword": "djangorest",
      "confirmPassword": "djangorest"
    }
    ```
  - **❓ Condition**: *If the user enter the email.*
    ```json
    {
      "token": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d",
      "newPassword": "djangorest",
      "confirmPassword": "djangorest"
    }
    ```

## 📥 Response(s)

### ❌ Error Response(s)
- **🔢 Code**: `400 BAD REQUEST`
- **✉ Content Example**:
  - **❓ Condition**: *If the password and confirm password not same.*
    ```json
    {
      "error": true,
      "message": "Passwords did not match.",
    }
    ```
  - **❓ Condition**: *If a validation error occurred.*
    ```json
    {
      "error": true,
      "message": "There are one or more error field(s). Please check it carefully.",
      "data": {
        "confirmPassword": "validation error message or an array to list the error occurred"
      }
    }
    ```
  

### ✅ Success Response(s)
- **❓ Condition**: *If there is no validation error.*
	- **🔢 Code**: `204 NO CONTENT`
	- **✉ Content Example**:
		```json
		{
			"error": false,
			"message": "The password is updated successfully.",
		}
		```
