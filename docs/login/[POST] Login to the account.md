# [POST] Login an account

Login an account to get more access to the API.

- **🌏 URL**: `/login`
- ~~**📋 URL Parameters**: -~~
- **🛤️ Method**: `POST`
- **🔐 Auth required**: `NO`
- ~~**🚫 Permissions required**: -~~

## 📤 Request(s)

- **📋 Data Constraint**
  - email: `plain-strings`, `required`
  - password: `plain-strings`, `required`, `min=8 chars`

- **✉ Data Example**
  > type the data example in json or xml format
  ```json
  {
    "email": "akhfzz23@gmail.com",
    "password": "kertosari"
  }
  ```

## 📥 Response(s)

### ❌ Error Response(s)
- **❓ Condition**: *If email not found*
  - **🔢 Code**: `400 BAD REQUEST`
  - **✉ Content Example**:
    ```json
    {
      "detail": "No active account found with the given credentials"
    }
    ```

### ✅ Success Response(s)
- **❓ Condition**: *There is no validation error.*
  - **🔢 Code**: `201 CREATED`
  - **✉ Content Example**:
    ```json
    {
      "error": false,
      "message": "The tokens has been generated successfully.",
      "data": {
          "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0NzU1OTQzLCJpYXQiOjE2NTQ3NTU2NDMsImp0aSI6ImQwNzcxNTY3NzkxNTQwMzQ4ZDlmMTI5NTQ0NmRmMzBkIiwidXNlcl9pZCI6MX0.hNaMN2TzKdT5ARW6g_BgfbZLFe4DRb8BTxuhL8pFjCo",
          "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDg0MjA0MywiaWF0IjoxNjU0NzU1NjQzLCJqdGkiOiI2NTc2ZTAzMzJkZjI0MDFkYWZmNDA1NzMxNGIxNzBmZSIsInVzZXJfaWQiOjF9.I1IkHx6dRHe-kycxJzx0ENkWUJU-QA7cmfg_JhJ36-4"
      }
    }
    ```
