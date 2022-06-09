# [POST] Reset Password

The token received in the user's email will be used in this endpoint. They'll input the token and the new password into their account.

- **🌏 URL**: `/api/reset-psw/confirm`
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
  - **❓ Condition**: *If the user enter code verification*
    ```json
    {
      "code": "DSJNc"
    }
    ```

## 📥 Response(s)

### ❌ Error Response(s)
- **🔢 Code**: `400 BAD REQUEST`
- **✉ Content Example**:
  - **❓ Condition**: *If code didn't match from db*
    ```json
    {
      "message": "Code is incorrect",
    }
    ```

### ❌ Error Response(s)
- **🔢 Code**: `404 BAD REQUEST`
- **✉ Content Example**:
  - **❓ Condition**: *error from django*
    ```json
    {
      "detail": "not found",
    }
    ```
  

### ✅ Success Response(s)
- **❓ Condition**: *code is match.*
	- **🔢 Code**: `201 CREATED`
	- **✉ Content Example**:
		```json
		{
			"code": "bsoi2",
		}
		```