"""
This module sets up the database connection using SQLAlchemy for a Flask application.
It checks if the target database exists and creates it using the `schema.sql` file if necessary.

Functions:
    check_database_exists(target_db: str, admin_engine) -> bool
        Checks if the target database exists using the admin connection.

    create_database(target_db: str, admin_engine) -> bool
        Creates the target database.

    run_schema(target_db_url: str, schema_file: str) -> bool
        Executes the SQL statements in the schema file to set up the database schema.

    init_db(app: Flask) -> None
        Configures the database connection and initializes the SQLAlchemy app.
        If the database does not exist, it creates the database first.
"""

from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, ProgrammingError
import os
import logging

# Initialize SQLAlchemy
db = SQLAlchemy()

# Path to the SQL schema file
SCHEMA_FILE = "schema.sql"

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG for detailed logs
logger = logging.getLogger(__name__)


def get_admin_engine(database_url: str):
    """
    Creates an SQLAlchemy engine connected to the server's default database for administrative tasks.
    Adjust the default database as per your DBMS (e.g., 'postgres' for PostgreSQL).

    Args:
        database_url (str): The original database URL.

    Returns:
        Engine: An SQLAlchemy engine connected to the admin/default database.
    """
    from urllib.parse import urlparse, urlunparse

    url_parts = urlparse(database_url)

    if url_parts.scheme.startswith('postgresql'):
        admin_db = 'postgres'
    elif url_parts.scheme.startswith('mysql'):
        admin_db = 'mysql'
    elif url_parts.scheme.startswith('sqlite'):
        # SQLite doesn't require a separate admin connection
        return None
    else:
        raise ValueError(f"Unsupported database type: {url_parts.scheme}")

    # Replace the database name with the admin/default database
    admin_url = urlunparse(
        (
            url_parts.scheme,
            url_parts.netloc,
            admin_db,
            url_parts.params,
            url_parts.query,
            url_parts.fragment,
        )
    )
    logger.debug("Admin URL: %s", admin_url)
    return create_engine(admin_url)


def check_database_exists(target_db: str, admin_engine) -> bool:
    """
    Checks if the target database exists using the admin connection.

    Args:
        target_db (str): The name of the target database.
        admin_engine (Engine): The SQLAlchemy engine connected to the admin database.

    Returns:
        bool: True if the target database exists, False otherwise.
    """
    if admin_engine is None:
        # For SQLite, existence is determined by the presence of the file
        exists = os.path.exists(target_db)
        logger.info("SQLite database exists: %s", exists)
        return exists

    try:
        with admin_engine.connect() as connection:
            if admin_engine.url.drivername.startswith('postgresql'):
                result = connection.execute(
                    text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
                    {"dbname": target_db}
                )
                exists = result.scalar() is not None
            elif admin_engine.url.drivername.startswith('mysql'):
                result = connection.execute(
                    text("SHOW DATABASES LIKE :dbname"),
                    {"dbname": target_db}
                )
                exists = result.scalar() is not None
            else:
                logger.error("Unsupported DBMS for existence check.")
                exists = False
        logger.info("Database '%s' exists: %s", target_db, exists)
        return exists
    except OperationalError as e:
        logger.error(
            "OperationalError while checking database existence: %s", e)
        return False
    except ProgrammingError as e:
        logger.error(
            "ProgrammingError while checking database existence: %s", e)
        return False
    except Exception as e:
        logger.error(
            "Unexpected error while checking database existence: %s", e)
        return False


def create_database(target_db: str, admin_engine) -> bool:
    """
    Creates the target database using the admin connection.

    Args:
        target_db (str): The name of the target database.
        admin_engine (Engine): The SQLAlchemy engine connected to the admin database.

    Returns:
        bool: True if the database was created successfully, False otherwise.
    """
    if admin_engine is None:
        # For SQLite, the database is created when connecting
        logger.info(
            "Creating SQLite database by connecting to '%s'.", target_db)
        try:
            open(target_db, 'a').close()
            logger.info(
                "SQLite database '%s' created successfully.", target_db)
            return True
        except Exception as e:
            logger.error(
                "Error creating SQLite database '%s': %s", target_db, e)
            return False

    try:
        with admin_engine.connect() as connection:
            # Set isolation level to AUTOCOMMIT for CREATE DATABASE
            connection = connection.execution_options(
                isolation_level="AUTOCOMMIT")
            logger.debug("Set connection to AUTOCOMMIT for database creation.")

            if admin_engine.url.drivername.startswith('postgresql'):
                # Use SQLAlchemy's text construct with proper quoting to prevent SQL injection
                connection.execute(text(f'CREATE DATABASE "{target_db}"'))
            elif admin_engine.url.drivername.startswith('mysql'):
                connection.execute(text(f"CREATE DATABASE `{target_db}`"))
            else:
                logger.error("Unsupported DBMS for database creation.")
                return False
        logger.info("Database '%s' created successfully.", target_db)
        return True
    except ProgrammingError as e:
        logger.error("ProgrammingError while creating database: %s", e)
    except OperationalError as e:
        logger.error("OperationalError while creating database: %s", e)
    except Exception as e:
        logger.error("Unexpected error while creating database: %s", e)
    return False


def run_schema(target_db_url: str, schema_file: str) -> bool:
    """
    Executes the SQL statements in the schema file to set up the database schema.

    Args:
        target_db_url (str): The database URL for the target database.
        schema_file (str): The path to the SQL schema file.

    Returns:
        bool: True if the schema was applied successfully, False otherwise.
    """
    if not os.path.exists(schema_file):
        logger.error("Schema file '%s' does not exist.", schema_file)
        return False

    try:
        with open(schema_file, 'r', encoding='utf-8') as file:
            schema_sql = file.read()
            logger.debug("Read schema.sql content successfully.")

        engine = create_engine(target_db_url)

        # Set isolation level to AUTOCOMMIT to handle commands that can't run inside transactions
        with engine.connect() as connection:
            connection = connection.execution_options(
                isolation_level="AUTOCOMMIT")
            logger.debug("Set connection to AUTOCOMMIT for schema execution.")

            # Split the SQL script into individual statements
            statements = [stmt.strip()
                          for stmt in schema_sql.strip().split(';') if stmt.strip()]
            logger.info(
                "Executing %d SQL statements from schema.sql.", len(statements))

            for idx, statement in enumerate(statements, start=1):
                try:
                    logger.debug("Executing statement %d: %s", idx,
                                 statement[:100] + '...' if len(statement) > 100 else statement)
                    connection.execute(text(statement))
                    logger.debug("Statement %d executed successfully.", idx)
                except Exception as stmt_e:
                    logger.error(
                        "Error executing statement %d: %s", idx, stmt_e)
                    return False

        logger.info(
            "Database schema applied successfully from '%s'.", schema_file)
        return True
    except Exception as e:
        logger.error("Error applying database schema: %s", e)
        return False


def init_db(app):
    """
    Configures the database connection and initializes the SQLAlchemy app.
    If the database does not exist, it creates the database first.

    Args:
        app (Flask): The Flask application instance.
    """
    database_url = getenv("DATABASE_URL")
    if not database_url:
        logger.error("DATABASE_URL environment variable is not set.")
        raise ValueError("DATABASE_URL environment variable is not set.")

    from urllib.parse import urlparse

    url_parts = urlparse(database_url)
    if url_parts.scheme.startswith('sqlite'):
        target_db = url_parts.path  # For SQLite, the path is the database file
    else:
        # Remove leading '/' for DB name
        target_db = url_parts.path.lstrip('/')

    admin_engine = get_admin_engine(database_url)

    if not check_database_exists(target_db, admin_engine):
        logger.info("Database '%s' does not exist. Creating it.", target_db)
        created = create_database(target_db, admin_engine)
        if not created:
            logger.error(
                "Failed to create the database '%s'. Aborting initialization.", target_db)
            raise RuntimeError(f"Failed to create the database '{target_db}'.")

        logger.info("Running schema script to set up the database.")
        schema_applied = run_schema(database_url, SCHEMA_FILE)
        if not schema_applied:
            logger.error(
                "Failed to apply the schema to the database '%s'.", target_db)
            raise RuntimeError(
                f"Failed to apply the schema to the database '{target_db}'.")
    else:
        logger.info(
            "Database '%s' already exists. Skipping creation.", target_db)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    try:
        db.init_app(app)
        logger.info("SQLAlchemy has been initialized with the app.")
    except Exception as e:
        logger.error("Error initializing SQLAlchemy with the app: %s", e)
        raise
