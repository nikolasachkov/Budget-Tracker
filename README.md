# Budget Tracker API

The Budget Tracker API provides a simple and intuitive way to manage personal finances through a RESTful interface. Built with Flask, this API supports a range of operations essential for personal budgeting.

## Features

- **Transaction Management**: Add, update, and delete financial transactions.
- **Budget Overview**: Retrieve a list of transactions and view your spending habits over time.
- **Insights**: Gain insights into your financial activities with monthly summaries.
- **Swagger Documentation**: Interactive API documentation with Swagger UI for easy testing and exploration of endpoints.

## Usage

Interact with the API endpoints to perform CRUD operations on your transactions. The endpoints include functionality such as:

- `POST /transactions`: Create a new financial transaction.
- `GET /transactions`: Retrieve all transactions.
- `PUT /transactions/{id}`: Update a transaction by its ID.
- `DELETE /transactions/{id}`: Remove a transaction from your records.

For detailed API usage, visit the Swagger UI at `http://localhost:5000/swagger` after launching the application.

## Testing

Ensure the integrity of your transactions and budget calculations with the included test suite, which can be executed to validate the various API endpoints and business logic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
