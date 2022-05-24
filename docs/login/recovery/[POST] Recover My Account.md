# [POST] 1 - Recover My Account

An endpoint to recover user account by entering the username or email of the user account.

- **🌏 URL**: `/login/recovery/`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
  - usernameOrEmail: `required`, `min=6`
    > - this variable should be a `plain text`.
    > - the api can define which email by checking the input as a valid email address and email has available on our database. Do this with form validation.


- **✉ Data Example**
  - **❓ Condition**: *If the user enter the username.*
    ```json
    {
      "usernameOrEmail": "ryuzakir"
    }
    ```
  - **❓ Condition**: *If the user enter the email.*
    ```json
    {
      "usernameOrEmail": "ryuzakir@example.com"
    }
    ```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If the field doesn't meet the data constraints (`Validation Error`).*
  - **🔢 Code**: `400 BAD REQUEST`
  - **✉ Content Example**:
    ```json
    {
      "error": true,
      "message": "validation error message or an array to list the error occurred.",
    }
    ```
- **❓ Condition**: *If the email or username isn't available in our database.*
  - **🔢 Code**: `404 NOT FOUND`
  - **✉ Content Example**:
    ```json
    {
      "error": true,
      "message": "Our system can't find {{usernameOrEmail}}. Please try again or you can register a new account with that.",
    }
    ```

### ✅ Success Response(s)
- **❓ Condition**: *If there is `no validation error` and the `email-or-username` exist.*
	- **🔢 Code**: `200 OK`
	- **✉ Content Example**:
		```json
		{
			"error": false,
			"message": "We've sent an email that contains an OTP to you. Please check your email inbox.",
		}
		```
  - **⚠️ Note(s)**
    - The backend also sends an email to the user's email address. The email contains a single-use token. The password recovery action will use this token to let a user change their new password.

## ⚠️ Note(s)

### Email Template for the Forgot Password Process
- **📋 Data Constraint**
  - `name`: the name of the user.
  - `token`: the token that'll be used for resetting the password.
- **✉ Email Template**:
  ```markdown
  Hi [name],

  There was a request to change your password!

  If you did not make this request then please ignore this email.

  Otherwise, please copy this single-use token to the form in the application to continue make your new password: [token]
  ```

### After Sending the Email
The front end should use this endpoint to proceed with the new password creation.
- **⏭️ The next endpoint** : 
  [[POST] Create a New Password](../../accounts/[PUT]%20Reset%20Password.md)
