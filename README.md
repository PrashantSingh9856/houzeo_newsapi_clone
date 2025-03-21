# Alembic Configuration and Migrations

This guide will help you configure Alembic, make migrations, and apply them to your database.

## Prerequisites

- Python installed
- SQLAlchemy installed
- Alembic installed

## Installation

Install Alembic using pip:

```bash
pip install alembic
```

## Configuration

1. **Initialize Alembic**: Run the following command to initialize Alembic in your project directory:

    ```bash
    alembic init alembic
    ```

    This will create an `alembic` directory with the necessary configuration files.

2. **Edit `alembic.ini`**: Update the `sqlalchemy.url` in the `alembic.ini` file to point to your database:

    ```ini
    sqlalchemy.url = postgresql://user:password@localhost/dbname
    ```

3. **Edit `env.py`**: Modify the `env.py` file to include your SQLAlchemy models. Import your models and set the `target_metadata`:

    ```python
    from myapp.models import Base
    target_metadata = Base.metadata
    ```

## Making Migrations

1. **Create a Migration Script**: Use the following command to generate a new migration script:

    ```bash
    alembic revision --autogenerate -m "description of changes"
    ```

    This will create a new migration script in the `alembic/versions` directory.

2. **Review the Migration Script**: Check the generated script and make any necessary adjustments.

## Applying Migrations

1. **Upgrade the Database**: Apply the migrations to your database using the following command:

    ```bash
    alembic upgrade head
    ```

    This will apply all pending migrations.

## Additional Commands

- **Downgrade the Database**: To revert the last migration, use:

    ```bash
    alembic downgrade -1
    ```

- **Check Current Revision**: To see the current revision of the database, use:

    ```bash
    alembic current
    ```

## Conclusion

You have now configured Alembic, created migrations, and applied them to your database. For more information, refer to the [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/).
