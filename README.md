# Async Inventory DB Logic & Schema for FastAPI

## Task Overview
You are tasked with building the PostgreSQL database backend for an inventory management system. The API endpoints for adding new products and listing all products are fully implemented in FastAPI, but the underlying database integration is not. Your main responsibilities are to design an efficient PostgreSQL schema for products, add all required keys and constraints, and then implement the async database logic that enables product creation and fetching through the API.

## Guidance

- The API code is scaffolded in `app/main.py`—do not change the route logic.
- Database connection and session setup are in `app/database.py`.
- Define your DB models in `app/models.py` and your schema (DDL) in `schema.sql`.
- Use `run.sh` for full Dockerized project setup; connect via the provided `DATABASE_URL`.

## Objectives

- Design a normalized `products` table with fields for name, SKU, quantity, price, and timestamps.
- Add primary key constraints, appropriate data types, uniqueness, and indexes as needed for efficient lookups.
- Implement async SQLAlchemy DB models and core CRUD logic for adding and querying products.
- Ensure all DB interactions are asynchronous and do not block the FastAPI event loop.
- Validate all new products are inserted with unique SKUs and required fields only.

## How to Verify

- Use the `/products` POST endpoint to insert a new product; confirm it is persisted in the DB and visible from the `GET /products` endpoint.
- Attempt to add duplicate SKU and observe proper constraint/validation errors.
- Fetch product list and check that all fields (id, name, sku, quantity, price, timestamps) are returned and data matches the DB.
- Run `docker-compose logs` and check for error-free async DB operations during usage.
