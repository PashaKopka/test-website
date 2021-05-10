# test-website

This is website with users and post. You can register user and do some posts. This app using python, Django, Django REST
Framework.

### REST API requests:

GET `posts_list_api`: request to get information about existing posts (readonly)

Result json:
```json
[
	{
    "id": "id-s of posts",
    "name": "Here will be names of articles",
    "article": "Here will be texts of articles",
    "image": "/url/to/image/of/this/article.png",
    "url": "url-of-this-article"
	},
```

GET `post_detail_api/<int:id>`: request to get detail information about some post (readonly)

Result json:
```json
[
	{
    "id": "id of post",
    "name": "Here will be name of article",
    "article": "Here will be text of article",
    "image": "/url/to/image/of/this/article.png",
    "url": "url-of-this-article"
	},
```

POST `new_post_api`: request to create some new post (must be JWT token). Example:

```json
{
  "name": "Name of your article",
  "article": "Body of your article",
  "image": "Path to file"
}
```

POST `toggle_like`: request to toggle like on post (must be JWT token). Example:

```json
{
  "post_id": "13"
}
```

GET `users_list_api`: request to get information about all users (readonly)

Result json:
```json
[
  {
    "id": "id of users",
    "username": "names of users",
    "last_login": "date:and:time:of:last:login",
    "email": "user.email@test.com"
  },
]
```

GET `user_detail_api/<int:id>`: request to get information about one users
(readonly)

Result json:

```json
{
  "id": "id of this user",
  "last_login": "date:and:time:of:last:login",
  "username": "name of user",
  "email": "user.email@test.com",
  "date_joined": "date:and:time:of:registration",
  "last_request": "date:and:time:of:last:request",
  "posts": ["Here will be info about posts of this user"],
  "liked_posts": ["Here will be info about liked posts of this user"]
}
```

POST `api/sign_up/`: request to register new user. Example:

```json
{
  "username": "Name of your user",
  "password": "password123",
  "email": "your.email@example.com"
}
```

GET `api/analitics`: request to get like analitics (readonly). Example:

```
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15
```

Result json:

```json
[
  {
    "id": "id of like",
    "post": {
	    "id": "id of post",
	    "name": "Here will be name of article",
	    "article": "Here will be text of article",
	    "image": "/url/to/image/of/this/article.png",
    },
    "user": {
		  "id": "id of this user",
		  "last_login": "date:and:time:of:last:login",
		  "username": "name of user",
		  "email": "user.email@test.com",
		  "date_joined": "date:and:time:of:registration",
		  "last_request": "date:and:time:of:last:request",
		  "posts": ["Here will be info about posts of this user"],
		  "liked_posts": ["Here will be info about liked posts of this user"]
    },
    "date": "2021-05-07"
  },
]
```

GET `api/analitics/format`: request to get like analitics (readonly). Example:

```
/api/analitics/format/?date_from=2019-02-02&date_to=2022-02-15
```

Result json:
```json
[
  {
    "date": "just date",
    "count": "here will be count of likes in this day"
  }
]
```

POST `api/token`: request to get access and refresh JWT token. Example:

```json
{
  "username": "Name of your user",
  "password": "password123"
}
```