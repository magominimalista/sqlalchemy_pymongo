from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import text

# Correct connection string for an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')

# Define metadata object
metadata_obj = MetaData()

# Define user table
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

# Define user_prefs table
user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

# Print info for user_prefs table
print("\nInfo da tabela user_prefs")
print(user_prefs.primary_key)

# Print all tables in metadata
print(metadata_obj.tables)

# Print sorted tables
for table in metadata_obj.sorted_tables:
    print(table)

# Create all tables in metadata_obj
metadata_obj.create_all(engine)

# Define a new metadata object for financial_info table
metadata_db_obj = MetaData()

# Define financial_info table
financial_info = Table(
    'financial_info',
    metadata_db_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False),
)

# Print info for financial_info table
print("\nInfo da tabela financial_info")
print(financial_info.primary_key)

# Insert sample data into the user table
with engine.connect() as conn:
    conn.execute(user.insert(), [
        {'name': 'John Doe', 'email_address': 'john@example.com', 'nickname': 'johnny'},
        {'name': 'Jane Smith', 'email_address': 'jane@example.com', 'nickname': 'janey'}
    ])

    # Execute a SQL query
    sql = text('SELECT * FROM user')
    result = conn.execute(sql)

    # Print query results
    print("\nResults from the 'user' table:")
    for row in result:
        print(row)
