import sys

database_signatures = {
    # SQLite
    b'\x53\x51\x4C\x69\x74\x65\x20\x66\x6F\x72\x6D\x61\x74\x20\x33': 'SQLite (sqlite)',
    # Microsoft Access
    b'\xFD\xFF\xFF\xFF\x00\x00\x00\x00': 'Microsoft Access (mdb)',
    b'\x00\x01\x00\x00\x53\x74\x61\x6E\x64\x61\x72\x64\x20\x4A\x65\x74\x20\x44\x42': 'Microsoft Access (accdb)',
    # MySQL
    b'\xFE\x62\x69\x6E': 'MySQL (myd)',
    b'\xFE\x6E\x61\x6D\x65': 'MySQL (myi)',
    # PostgreSQL
    b'\x50\x47\x00\x00': 'PostgreSQL (pgdata)',
    # MongoDB
    b'\x16\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x01': 'MongoDB (bson)',
    # Oracle
    b'\x00\x00\x01\x00': 'Oracle (dbf)',
    # Microsoft SQL Server
    b'\x01\x0F\x00\x00': 'Microsoft SQL Server (mdf)',
    b'\x00\x01\x00\x00\x04\x00\x00\x00': 'Microsoft SQL Server (ldf)',
    # MySQL - InnoDB
    b'\x49\x53\x4F\x4D': 'MySQL InnoDB (ibdata1)',
    b'\x49\x53\x4F\x4D\x4C': 'MySQL InnoDB (ib_logfile0)',
    b'\x49\x53\x4F\x4D\x4D': 'MySQL InnoDB (ib_logfile1)',
    # PostgreSQL (with file header)
    b'\x80\x01\x00\x00\x00\x00\x00\x00': 'PostgreSQL (pgdata - with file header)',
    # MariaDB (Aria)
    b'\x43\x4B\x52\x4E\x04\x00\x00\x00\xA6\x00\x00\x00\x00\x00': 'MariaDB Aria (aria)',
    # Firebird
    b'\x30\x82\x01\x00': 'Firebird (fdb)',
    # SQLite WAL (Write-Ahead Logging)
    b'\x57\x41\x4C\x2D': 'SQLite WAL (wal)',
    # SQLite SHM (Shared Memory)
    b'\x53\x48\x4D\x01': 'SQLite SHM (shm)',
    # SQLite rollback journal
    b'\x2F\x72\x6A\x6F\x75\x72\x6E\x61\x6C': 'SQLite Rollback Journal (journal)',
    # SQLite rollback journal (in-memory)
    b'\x2F\x74\x6D\x70\x2F\x73\x71\x6C\x69\x74\x65\x2F\x31\x31\x36\x37': 'SQLite In-Memory Rollback Journal (journal)',
    # IBM DB2
    b'\x42\x5A': 'IBM DB2 (db2)',
    # Sybase
    b'\x04\x01\x00\x00': 'Sybase (db - Old)',
    b'\x04\x01\x00\x00\x01\x00\x00\x00': 'Sybase (db - New)',
    # dBASE
    b'\x03\x00\x00\x00': 'dBASE (dbf)',
    # FoxPro
    b'\xF5\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00': 'FoxPro (dbf)',
    # Paradox
    b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': 'Paradox (db - Old)',
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': 'Paradox (db - New)',
    # Lotus Notes NSF
    b'\x1A\x52\x4D\x49\x00\x00\x00\x00': 'Lotus Notes NSF (nsf)',
    # HSQLDB
    b'\x48\x53\x51\x4C\x44\x42': 'HSQLDB (hsql)',
    # SQLite - Write-Ahead Logging (WAL) format 2
    b'\x57\x41\x4C\x46\x02': 'SQLite WAL (wal - format 2)',
    # SQLite - Write-Ahead Logging (WAL) format 3
    b'\x57\x41\x4C\x46\x03': 'SQLite WAL (wal - format 3)',
    # SQLite - Write-Ahead Logging (WAL) format 4
    b'\x57\x41\x4C\x46\x04': 'SQLite WAL (wal - format 4)',
    # SQLite - Write-Ahead Logging (WAL) format 5
    b'\x57\x41\x4C\x46\x05': 'SQLite WAL (wal - format 5)',
    # SQLite - Write-Ahead Logging (WAL) format 6
    b'\x57\x41\x4C\x46\x06': 'SQLite WAL (wal - format 6)',
}
    
def detect_database_type(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(16)
        for signature, database_type in database_signatures.items():
            if header.startswith(signature):
                return database_type
        return "Unknown"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        database_type = detect_database_type(sys.argv[1])
        print(f"The database type is: {database_type}")
    else:
        print("Invalid parameter!!! You need call: python database_type_detect.py your_database_file")
