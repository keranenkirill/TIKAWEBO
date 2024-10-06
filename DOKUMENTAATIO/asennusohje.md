# Asennusohje - Rent&Stay

(Tässä asennusohjeessa ei huomioida projektin asennusta Windows-koneelle)

1. Lataa projekti GitHubista

2. Virtuaaliympäristön luominen ja aktivoiminen:
   Virtuaaliympäristö auttaa hallitsemaan projektisi riippuvuuksia ja estämään ristiriitoja muiden projektien kanssa.

   ```bash
   python3 -m venv venv
   ```

3. Aktivoi virtuaaliympäristö:

   ```bash
   source venv/bin/activate
   ```

4. Riippuvuuksien asentaminen:

   ```bash
   pip install -r requirements.txt
   ```

5. Ympäristömuuttujien asettaminen (.env-tiedosto):

   ```bash
   touch .env
   ```

6. Avaa .env-tiedosto tekstieditorilla ja lisää sinne seuraavat tiedot:

   ```bash
   DATABASE_URL=postgresql://postgres:postgrespsql@localhost/rsdb

   SECRET_KEY= ## generoi oma avain ##
   ```

7. Tietokannan luominen ja alustaminen

   Varmista, että PostgreSQL-palvelin on asennettu ja käynnissä terminaalissa.
   Luo tietokanta "rsdb" joka vastaa .env-tiedostossa määriteltyä tietokantaa:

   ```bash
   postgres=# CREATE DATABASE rsdb;
   ```

   siirry tietokantaan rsdb:

   '''bash
   postgres=# \c rsdb
   You are now connected to database "rsdb" as user "postgres".
   rsdb=#
   '''

8. Tietokannan alustus tauluilla

   Kun suoritat projektin ensimmäistä kertaa, sovellus tarkistaa tietokannan olemassaolon ja luo sen automaattisesti käyttämällä schema.sql-tiedostoa, mikäli tietokantaa ei vielä ole.

   :warning: Mikäli tietokanta ei automaattisesti alustu, alla on manuaalisen alustamisen skripti:

   '''bash
   sudo -i -u postgres psql -d rsdb < schema.sql
   '''

   terminaalissa voit tarkistaa taulujen olemassaolon:

   '''bash
   rsdb=# \dt
   '''

9. Projektin suorittaminen

   Kun olet määrittänyt ympäristömuuttujat ja asentanut riippuvuudet, voit käynnistää Flask-sovelluksen seuraavalla komennolla:

   ```bash
   flask run
   ```
