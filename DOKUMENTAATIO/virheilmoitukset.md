#### Ajettuasi komennon:

```bash
   psql -d postgres -f ./scripts/initdb.sql
```

mahdollinen virheviesti:

```bash
psql: error: connection to server on socket "/home/kayttaja/pgsql/sock/.s.PGSQL.
5432" failed: Connection refused
      Is the server running locally and acepting connections on that socket?
```

#### Ajettuasi komennon:

```bash
flask run
```

...mahdollinen virhetulostus:

```bash
DEBUG:db:Admin URL: postgresql://rsuser:rspass@localhost/postgres
ERROR:db:OperationalError while checking database existence: (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
  Is the server running on that host and accepting TCP/IP connections?

(Background on this error at: https://sqlalche.me/e/20/e3q8)
INFO:db:Database 'rsdb' does not exist. Creating it.
ERROR:db:OperationalError while creating database: (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
  Is the server running on that host and accepting TCP/IP connections?

(Background on this error at: https://sqlalche.me/e/20/e3q8)
ERROR:db:Failed to create the database 'rsdb'. Aborting initialization.
Traceback (most recent call last):
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/bin/flask", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/flask/cli.py", line 1105, in main
    cli.main()
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/click/core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/click/core.py", line 783, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/click/decorators.py", line 92, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/flask/cli.py", line 953, in run_command
    raise e from None
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/flask/cli.py", line 937, in run_command
    app: WSGIApplication = info.load_app()
                           ^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/flask/cli.py", line 339, in load_app
    app = locate_app(import_name, None, raise_if_not_found=False)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/venv/lib/python3.11/site-packages/flask/cli.py", line 245, in locate_app
    __import(module_name)
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/app.py", line 29, in <module>
    init_db(app)
  File "/home/kayttaja/hiekkalaatikko/TIKAWEBO/db.py", line 262, in init_db
    raise RuntimeError(f"Failed to create the database '{target_db}'.")
RuntimeError: Failed to create the database 'rsdb'.

.....
```
