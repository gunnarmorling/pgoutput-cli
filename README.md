# pgoutput-cli

A command-line client for consuming [logical replication](https://www.postgresql.org/docs/current/protocol-logical-replication.html) events from Postgres, using the pgoutput logical decoding plug-in.
As pgoutput emits a binary [event format](https://www.postgresql.org/docs/current/protocol-logicalrep-message-formats.html), messages are not really readable using [pg_recvlogical](https://www.postgresql.org/docs/current/app-pgrecvlogical.html) or `pg_logical_slot_get_changes()`,
as would be the case with text-based decoding plug-ins like wal2json or test_decoding.

All the heavy-lifting is done by [pypgoutput](https://github.com/dgea005/pypgoutput) by Daniel Geals.
As this project isn't maintained any longer,
it has [been forked](https://github.com/gunnarmorling/pypgoutput) to ensure compatibility with current Python and dependency versions.

`pgoutput-cli` wraps this in a ready-to use Python application and a container image.

## Prerequisites

This project depends on [Psycopg](https://www.psycopg.org/), a PostgreSQL adapter for the Python programming language.
See its [installation instructions](https://www.psycopg.org/docs/install.html#install-from-source) for building it from source. On macOS, I had to do the following things:

```bash
brew install libpq
brew install openssl

export LDFLAGS="-L/opt/homebrew/opt/openssl@3/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openssl@3/include"
export PATH="/opt/homebrew/opt/libpq/bin:$PATH"
```

## Set-Up

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
pgoutput-cli --host=<host> --port=<port> \
  --database=<database> --user=<user> --password=<password> \
  --publication<publication> --slot=<slot>
```

Or, via Docker, typically connecting to a Docker network with your Postgres database:

```
docker run -it --rm --network <some network> gunnarmorling/pgoutput-cli \
  pgoutput-cli --host=<host> --port=<port> \
  --database=<database> --user=<user> --password=<password> \
  --publication<publication> --slot=<slot>
```

## Build

```
docker build -t gunnarmorling/pgoutput-cli:<tag> .
```

## Source

The source of this project is located in the [pgoutput-cli](https://github.com/gunnarmorling/pgoutput-cli) repository on GitHub.

## License

This software is provided under the MIT License (MIT).
