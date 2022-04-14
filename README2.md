# Phone a Friend

## API endpoints
### Base URL: **https://phone-a-friend.herokuapp.com**
*All requests, except registration and log in, require authentication.*

---
## Log in

**URL**: `api/auth/token/login`

**method**: `POST`

**JSON**
```
{
	"username": "admin",
	"password": "admin"
}
```
**JSON Response**

200 OK
```
{
	"auth_token": "528c06f5d3a9ec28cedf7a57abcd565223ea55cc"
}
```