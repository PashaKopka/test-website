# test-website

This is website with users and post. You can register user and do some posts. This app using python, Django, Django REST
Framework.

### REST API requests:

GET `posts_list_api`: request to get information about existing posts (readonly)

GET `post_detail_api/<int:id>`: request to get detail information about some post (readonly)

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

GET `user_detail_api/<int:id>`: request to get information about one users
(readonly)

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

POST `api/token`: request to get access and refresh JWT token. Example:

```json
{
  "username": "Name of your user",
  "password": "password123"
}
```