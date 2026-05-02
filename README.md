# SCHelper API Documentation

## Overview

SCHelper API — это backend-сервис для работы с API EXBO (Stalcraft), предоставляющий доступ к данным пользователя, персонажей и игровой статистике.

API использует OAuth2 авторизацию через EXBO и session-based аутентификацию.

Базовый URL: `/api/v1/`

---

## Terminology

**User** — игровой аккаунт EXBO (создаётся через OAuth).

**Character** — персонаж пользователя в конкретном регионе (eu, ru, sea, nea). У одного пользователя может быть несколько персонажей.

---

## Authentication Flow

1. Выполнить запрос: GET `/api/v1/auth/exbo/`

2. Пользователь будет перенаправлен на страницу авторизации EXBO.

3. После успешной авторизации EXBO выполнит redirect на: `/api/v1/auth/exbo/callback/?code=...`

4. В результате:
- создаётся пользователь в базе
- access_token сохраняется в session
- user_id сохраняется в session

5. После этого становятся доступны защищённые endpoints.

Авторизация основана на session (cookie). Если session отсутствует — происходит redirect на `/auth/exbo/`.

---
### Authorization Details
- Используется session-based аутентификация
- Данные session:
    - user_id
    - access_token
- При отсутствии session происходит redirect на /auth/exbo/

--- 
## Endpoints

### 1. EXBO Authorization

#### GET /api/v1/auth/exbo/

Перенаправляет пользователя на OAuth авторизацию EXBO.

**Response:**
- HTTP 302 Redirect

---

#### GET /api/v1/auth/exbo/callback/

Обрабатывает callback от EXBO и создаёт пользователя.

**Query params:**
- `code` — OAuth code

**Success (201):**
```json
{
  "user_id": "string",
  "access_token": "string",
  "refresh_token": "string",
  "token_expires_in": 123456
}
```

**Error (400):**
```json
{
  "error": "Invalid OAuth state"
}
```
---

#### GET `/api/v1/auth/refresh_token/`

Обновляет access_token через refresh_token.
Требует активную session.

Success (200):
```json
{
  "response": "token was successfully updated"
}
```
Redirect:
- если пользователь не авторизован → redirect на `/auth/exbo/`

---

### 2. Characters
#### GET `/api/v1/characters/`

Возвращает список персонажей пользователя.

Поиск происходит по регионам (ru, eu, sea, nea). Возвращается первый найденный результат.

**Success (200):**
```json
[
  {
    "information": {
      "id": "uuid",
      "name": "string",
      "creationTime": "datetime"
    }
  }
]
```

**Error:**
```json
["error_title", status_code]
```
или
```json
{
  "error": "user not found"
}
```

---
### 3. Profile
#### GET `/api/v1/profile/`
Возвращает профиль персонажа.

Логика:

- если найден 1 персонаж → возвращается объект
- если несколько → возвращается список объектов
- поиск идёт по всем регионам

**Success (200):**

Один персонаж:
```json
{
  "username": "string",
  "uuid": "uuid",
  "status": "string",
  "alliance": "string",
  "lastLogin": "datetime",
  "displayedAchievements": [],
  "stats": [...]
}
```
несколько персонажей:
```json
[
  { ... },
  { ... }
]
```

**error:**
```json
{
  "error": "character not found"
}
```

---
### 4.Emission
#### GET `/api/v1/emission/`

Возвращает информацию о выбросе (emission) для региона.

**Success (200):**
```json
{
  ...
}
```
Возвращается первый найденный ответ по регионам.

---
### 5. Friends List
#### GET `/api/v1/friends_list/`
Возвращает список друзей для всех персонажей пользователя.

**Success (200):**
```json
[
  {
    ...
  },
  {
    ...
  }
]
```
Каждый элемент списка — ответ API для одного региона/персонажа.
