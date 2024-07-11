---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# API

- [API](#api)
  - [Useful Links](#useful-links)
  - [Status Codes](#status-codes)
  - [Naming Conventions](#naming-conventions)
    - [1. Use RESTful Resource Naming](#1-use-restful-resource-naming)
    - [2. Keep URLs Simple](#2-keep-urls-simple)
    - [3. Use HTTP Methods Consistently](#3-use-http-methods-consistently)
    - [4. Use Lowercase Letters](#4-use-lowercase-letters)
    - [5. Avoid Using Query Parameters for CRUD](#5-avoid-using-query-parameters-for-crud)
    - [6. Use Hyphens (-) Instead of Underscores (\_)](#6-use-hyphens---instead-of-underscores-_)
    - [7. Be Clear with Endpoint Functionality](#7-be-clear-with-endpoint-functionality)
    - [8. Version Your API](#8-version-your-api)
    - [9. Use Conventional Status Codes](#9-use-conventional-status-codes)
    - [10. Keep Consistent Naming](#10-keep-consistent-naming)

## Useful Links

- [Restful API](https://restfulapi.net/)
- [Postman](https://www.postman.com/)
- [DesignAPIs](http://designapis.com/)
- [Design APIs Github](https://github.com/designapis)
- [Open APIs Org](https://www.openapis.org/)
- [Swagger IO](https://swagger.io/tools/open-source/)

## Status Codes

| Status Code | Reason Phrase         | Description                                                 |
|-------------|-----------------------|-------------------------------------------------------------|
| 200         | OK                    | The request was successfully received, understood, and accepted.|
| 201         | Created               | The request was successful and a resource was created.      |
| 204         | No Content            | The request was successful, but there's no representation to return (i.e. the response is empty).|
| 400         | Bad Request           | The request could not be understood or was missing required parameters.|
| 401         | Unauthorized          | Authentication failed or user does not have permissions for the desired action.|
| 403         | Forbidden             | Authentication succeeded, but the authenticated user does not have access to the requested resource.|
| 404         | Not Found             | The requested resource could not be found.                  |
| 405         | Method Not Allowed    | The method specified in the request is not allowed for the resource identified by the request URI.|
| 409         | Conflict              | The request could not be completed due to a conflict with the current state of the target resource.|
| 500         | Internal Server Error | An error occurred on the server.                            |
| 503         | Service Unavailable   | The service is unavailable, often due to maintenance.       |

## Naming Conventions

### 1. Use RESTful Resource Naming

- **Collections**: Use plural nouns (e.g., `/users`, `/orders`).
- **Individual Resources**: Reference individual resources by ID (e.g., `/users/{id}`, `/orders/{orderId}`).

### 2. Keep URLs Simple

- Avoid deep nesting, e.g., use `/users/{id}/orders` instead of `/users/{id}/purchases/orders/{orderId}`.

### 3. Use HTTP Methods Consistently

- `GET`: Retrieve a resource.
- `POST`: Create a new resource.
- `PUT` or `PATCH`: Update an existing resource.
- `DELETE`: Remove a resource.

### 4. Use Lowercase Letters

- URLs are case-sensitive (except the domain). Using lowercase ensures consistency.
  - Good: `/users/{id}`
  - Avoid: `/Users/{ID}`

### 5. Avoid Using Query Parameters for CRUD

- Use query parameters for filtering, sorting, and pagination, not for CRUD operations.
  - Good: `/users?role=admin`
  - Avoid: `/getUser?userId=123`

### 6. Use Hyphens (-) Instead of Underscores (_)

- Hyphens are more commonly used in URLs and are typically more readable.
  - Good: `/order-items`
  - Avoid: `/order_items`

### 7. Be Clear with Endpoint Functionality

- If an endpoint triggers an action, the action should be clear.
  - Good: `/users/{id}/activate` or `/orders/{id}/cancel`

### 8. Version Your API

- Always version your API from the start (e.g., `/v1/users`). This ensures backward compatibility when changes are made.

### 9. Use Conventional Status Codes

- Ensure you return the correct HTTP status codes to indicate the result of an API call (e.g., `200 OK`, `404 Not Found`).

### 10. Keep Consistent Naming

- Use consistent naming for parameters, e.g., always use `id` rather than mixing `id`, `ID`, `itemId`.
