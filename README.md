# URL Shortener

A production-inspired URL Shortener built with FastAPI, PostgreSQL, Redis, and Docker.

## Features

- Short URL generation using Base62 encoding
- PostgreSQL for persistent URL storage
- Redis caching for fast redirects
- Redis-based rate limiting
- URL expiration support
- Cache TTL synchronized with URL expiration
- Graceful fallback to PostgreSQL when Redis is unavailable
- HTTP 307 redirects
- Load testing with Locust

## Tools

- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Locust
- Docker

## Architecture

```text
                    Client
                      |
                      v
                 FastAPI API
                 /         \
                /           \
          /shorten          /{short_code}
              |                   |
              v                   v
         Rate Limiter          Redis
              |              (Cache Hit)
              v                   |
         PostgreSQL               |
              |                   |
              +-------> Redis <--+
                         |
                         v
                    307 Redirect
