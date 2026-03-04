## I. Overview

This system (https://datarisk8.com/) provides multi-platform account risk detection capabilities, supporting platforms such as **Facebook**, **Instagram**, **WhatsApp**, and **Reddit**, each with different detection types. All requests are submitted uniformly through the detection interface, and the corresponding logic is executed based on the "Platform + Check Type".
Remember Buy card-key for checking.
---

## II. General API Information

### 2.1 Request Method and Endpoint

- **Method**: `POST`
- **Path**: `/api/v1/detect`
- **Content-Type**: `application/json`

### 2.2 General Request Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| platform | string | Yes | Platform: `facebook` / `instagram` / `whatsapp` |
| check_type | string | Yes | Check type, see sections for each platform |
| phone_numbers | string[] | Yes | List to be checked (phone numbers [**Must include country code**]/emails/UIDs/CKs/accounts, etc., depending on the check type) |
| card_key | string | Yes | Card key for authentication and fee deduction |
| use_proxy | boolean | No | Whether to use a proxy, default `true` |
| generate_report | boolean | No | Whether to generate a report, default `false` |

### 2.3 General Response Structure

| Field | Type | Description |
|------|------|------|
| success | boolean | Whether the request was successful |
| message | string | Information message, e.g., "Detection completed" |
| data | array | List of detection results, each item see "Single Result" below |
| statistics | object | Statistical information |

**Single Result (data[i])**

| Field | Type | Description |
|------|------|------|
| phone | string | Original identifier submitted (phone number/email/UID/CK/username, etc.) |
| status | string | `success` / `failed` |
| is_new | boolean | Whether it's a new account (applicable for some check types) |
| is_blocked | int | 0 Not checked, 1 Risk/Restricted/Invalid, 2 Valid/Active (applicable for some types) |
| reg_date | string | Registration date (only for UID type checks) |
| error_msg | string | Error message in case of failure |
| details | object | Extended details, varies by check type |

**Statistics (statistics)**

| Field | Type | Description |
|------|------|------|
| total_phones | int | Total number of items |
| new_phones | int | Number of new accounts |
| old_phones | int | Number of old accounts |
| failed_phones | int | Number of failed checks |
| pending_phones | int | Number of pending checks |
| total_time | float | Total time taken (seconds) |
| success_rate | float | Success rate (%) |
| completion_time | string | Completion time |

---

## III. Facebook Platform

### 3.1 Risk Check (risk)

**Function**: Checks if a phone number/email is registered and if the account is restricted.

**Input Requirements**:

- One phone number or email per line.
- Batch check up to 100 accounts per request.
- Example: `8613800138000`, `xxx@gmail.com`

**API Example**

```json
POST /api/v1/detect
{
  "platform": "facebook",
  "check_type": "risk",
  "phone_numbers": ["8613800138000", "user@gmail.com"],
  "card_key": "your-card-key",
  "use_proxy": true,
  "generate_report": false
}
```

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "8613800138000",
      "is_new": false,
      "is_blocked": 2,
      "reg_date": "",
      "status": "success",
      "error_msg": "",
      "details": {}
    }
  ],
  "statistics": {
    "total_phones": 1,
    "new_phones": 0,
    "old_phones": 1,
    "failed_phones": 0,
    "pending_phones": 0,
    "total_time": 2.5,
    "success_rate": 100.0,
    "completion_time": "2026-02-27 12:00:00"
  }
}
```

---

### 3.2 UID Check (uid)

**Function**: Checks registration time and account status based on Facebook UID.

**Input Requirements**:

- One UID per line.
- Batch check up to 100 UIDs per request.
- Example: `61571169000001`

**API Example**

```json
POST /api/v1/detect
{
  "platform": "facebook",
  "check_type": "uid",
  "phone_numbers": ["61571169000001"],
  "card_key": "your-card-key"
}
```

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "61571169000001",
      "is_new": false,
      "is_blocked": 2,
      "reg_date": "2020-05-01",
      "status": "success",
      "error_msg": "",
      "details": {}
    }
  ],
  "statistics": {
    "total_phones": 1,
    "new_phones": 0,
    "old_phones": 1,
    "failed_phones": 0,
    "success_rate": 100.0
  }
}
```

---

### 3.3 CK Validity Check (ck)

**Function**: Checks if a Cookie (CK) is valid.

**Input Requirements**:

- One CK string per line.
- Batch check up to 100 items per request.
- Example: `c_user=61571169000001; xs=xxxxxxxxx`

**API Example**

```json
POST /api/v1/detect
{
  "platform": "facebook",
  "check_type": "ck",
  "phone_numbers": ["c_user=61571169000001; xs=xxxxxxxxx"],
  "card_key": "your-card-key"
}
```

**Response Description**: For this type, `is_blocked` indicates CK validity—`2` Valid, `1` Invalid; `is_new` and `reg_date` are not applicable for this type.

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "c_user=61571169000001; xs=xxxxxxxxx",
      "is_new": false,
      "is_blocked": 2,
      "reg_date": "",
      "status": "success",
      "error_msg": "",
      "details": {}
    }
  ],
  "statistics": { "total_phones": 1, "success_rate": 100.0 }
}
```

---

## IV. Instagram Platform

### 4.1 New/Old Account Check (isnew)

**Function**: Checks if an account is new or old.

**Input Requirements**:

- One phone number, email, or username per line.
- Batch check up to 100 accounts per request.

**API Example**

```json
POST /api/v1/detect
{
  "platform": "instagram",
  "check_type": "isnew",
  "phone_numbers": ["username_or_phone_1", "username_or_phone_2"],
  "card_key": "your-card-key"
}
```

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "username_or_phone_1",
      "is_new": true,
      "is_blocked": 0,
      "reg_date": "",
      "status": "success",
      "error_msg": "",
      "details": {}
    }
  ],
  "statistics": {
    "total_phones": 2,
    "new_phones": 1,
    "old_phones": 1,
    "failed_phones": 0,
    "success_rate": 100.0
  }
}
```

---

### 4.2 Risk Check (risk)

**Function**: Queries account information and checks risk status based on username.

**Input Requirements**:

- One username per line.
- Batch check up to 100 accounts per request.

**API Example**

```json
POST /api/v1/detect
{
  "platform": "instagram",
  "check_type": "risk",
  "phone_numbers": ["instagram_username_1"],
  "card_key": "your-card-key"
}
```

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "instagram_username_1",
      "is_new": false,
      "is_blocked": 2,
      "reg_date": "",
      "status": "success",
      "error_msg": "",
      "details": {}
    }
  ],
  "statistics": { "total_phones": 1, "success_rate": 100.0 }
}
```

---

### 4.3 Cookie Extraction (extract_cookies)

**Function**: Logs into accounts and extracts cookies.

**Input Requirements**:

- Format per line: `username;password;2fa_code(if any)` (Note: separator is a semicolon).
- Supports batch extraction, up to 30 accounts per request.

**API Example**

```json
POST /api/v1/detect
{
  "platform": "instagram",
  "check_type": "extract_cookies",
  "phone_numbers": ["username1;pwd1", "username2;pwd2;3279"],
  "card_key": "your-card-key"
}
```

**Response Description**: Upon success, the cookie or session information is typically found in `details`. Upon failure, `error_msg` provides the reason (e.g., incorrect username/password, security verification triggered, etc.).

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "username1",
      "is_new": true,
      "is_blocked": 0,
      "reg_date": "",
      "status": "success",
      "error_msg": "",
      "details": { "response": "session_string_or_cookie..." }
    }
  ],
  "statistics": { "total_phones": 1, "success_rate": 100.0 }
}
```

---

## V. WhatsApp Platform

### 5.1 New/Old Account Check (isnew)

**Function**: Checks if the account corresponding to a phone number is new or old.

**Input Requirements**:

- One phone number per line.
- Check up to 100 accounts per request.

**API Example**

```json
POST /api/v1/detect
{
  "platform": "whatsapp",
  "check_type": "isnew",
  "phone_numbers": ["8613800138000"],
  "card_key": "your-card-key"
}
```

**Response Example**

```json
{
  "success": true,
  "message": "Detection completed",
  "data": [
    {
      "phone": "8613800138000",
      "is_new": false,
      "is_blocked": 0,
      "reg_date": "",
      "status": "success",
      "error_msg": "",
      "details": {}
    }
  ],
  "statistics": {
    "total_phones": 1,
    "new_phones": 0,
    "old_phones": 1,
    "failed_phones": 0,
    "success_rate": 100.0
  }
}
```
---
## VI. Reddit Platform

### 6.1 Ban/Restriction Check (isblock)

---

## VII. Errors and Limitations

- **400**: Bad request (e.g., empty phone numbers list, unsupported platform/check type, invalid card key, or insufficient balance). The `detail` field in the response body will specify the reason.
- **401**: Card key not provided or invalid. The frontend should redirect to login.
- **500**: Internal server error. The `detail` field in the response body will contain a brief error message.
- The number of `phone_numbers` in a single request must not exceed the system configuration limit (e.g., 100), otherwise a 400 error is returned.
