# Fit-App API
Backend API for Fit-App SPA

## Version: 1.0

### Security
**Bearer Auth**  

|apiKey|*API Key*|
|---|---|
|In|header|
|Name|Authorization|
|Description|Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token|

### /progress/

#### GET
##### Summary:

Get a list of every user's progress

##### Description:

Requires read:progress permission

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [ [all_progress_model](#all_progress_model) ] |

### /progress/test/{user_id}

#### GET
##### Summary:

TEST Endpoint

##### Description:

Generate  artificial user's progress and return all progress

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [ [progress_list_model](#progress_list_model) ] |

### /progress/{user_id}

#### GET
##### Summary:

Get a list of user's progress

##### Description:

Only authenticated user can access their own resource

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [ [progress_list_model](#progress_list_model) ] |

#### POST
##### Summary:

Post a progress

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |
| payload | body |  | Yes | [progress_model](#progress_model) |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 | Success | [progress_model](#progress_model) |

#### PATCH
##### Summary:

Patch a progress

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |
| payload | body |  | Yes | [progress_model](#progress_model) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Modify progress successful |

### /users/

#### GET
##### Summary:

Get a list of all users

##### Description:

This endpoint requires read:user permission

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [ [user_list_model](#user_list_model) ] |

#### POST
##### Summary:

Create a new user

##### Description:

Only authenticating user can post
User ID is defined by the verified subject in the access token

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| payload | body |  | Yes | [user_model](#user_model) |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 | Success | [user_model](#user_model) |

### /users/{user_id}

#### GET
##### Summary:

Obtain user information

##### Description:

Only authenticated user can access their own resource

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |
| X-Fields | header | An optional fields mask | No | string (mask) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [user_model](#user_model) |

#### DELETE
##### Summary:

Delete existing user

##### Description:

Require delete:user permission
This will also delete associated progress for this user

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | User deleted successfully |

#### PATCH
##### Summary:

Update user

##### Description:

Authenticated user can only access their own resource

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | string |
| payload | body |  | Yes | [user_patch_model](#user_patch_model) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | User modified successfully |

### Models


#### user_model

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | string | IdP provided user-id | No |
| target_weight | number | User target weight | No |
| height | number | height in cm | No |
| city | string | City | No |
| state | string | State or Country (Non-US) | No |

#### user_list_model

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| users | [ [user_model](#user_model) ] |  | No |
| count | integer | Total number of users | No |

#### user_patch_model

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| target_weight | number | User target weight in kg | No |
| height | number | height in cm | No |
| city | string | City | No |
| state | string | State or Country (Non-US) | No |

#### all_progress_model

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| progresses | [ [progress_model](#progress_model) ] |  | No |
| count | integer | Progress counts | No |

#### progress_model

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| user_id | string | IdP provided user-id | No |
| track_date | date | Date of tracking | Yes |
| weight | number | Current weight | Yes |
| mood | string | Mood value. Can be one of the following (neutral, bad, good) | Yes |
| diet | string | Diet value. Can be one of the following (neutral, bad, good) | Yes |

#### progress_list_model

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| user_id | string | IdP provided user-id | No |
| progresses | [ [progress_model](#progress_model) ] |  | No |
| count | integer | Progress counts | No |