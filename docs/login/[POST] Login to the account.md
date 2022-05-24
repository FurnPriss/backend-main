# [POST] Login an account

Login an account to get more access to the API.

- **🌏 URL**: `/login/`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
  - username: `plain-strings`, `required`, `min=6 chars`
  - password: `plain-strings`, `required`, `min=8 chars`

- **✉ Data Example**
  > type the data example in json or xml format
  ```json
  {
    "username": "iloveauth",
    "password": "abcd1234"
  }
  ```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If a validation error occurred.*
  - **🔢 Code**: `400 BAD REQUEST`
  - **✉ Content Example**:
    ```json
    {
      "error": true,
      "message": "The username or password you typed is invalid.",
      "data": {
        "username": "validation error message or an array to list the error occurred"
      }
    }
    ```

### ✅ Success Response(s)
- **❓ Condition**: *There is no validation error.*
  - **🔢 Code**: `201 CREATED`
  - **✉ Content Example**:
    ```json
    {
      "error": false,
      "message": "You've logged in successfully.",
      "data": {
        "accessToken": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d",
        "refreshToken":
        "cnd8suc9du8sfuiersfviuy987wp0okmkigt09sj"
      }
    }
    ```
