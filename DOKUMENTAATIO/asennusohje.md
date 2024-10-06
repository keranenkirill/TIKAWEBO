# Asennusohje - Rent&Stay

1. Lataa projekti GitHubista

2. Virtuaaliympäristön luominen ja aktivoiminen:
   Virtuaaliympäristö auttaa hallitsemaan projektisi riippuvuuksia ja estämään ristiriitoja muiden projektien kanssa.

   - python3 -m venv venv
     Aktivoi virtuaaliympäristö
   - source venv/bin/activate

3. Riippuvuuksien asentaminen:

   - pip install -r requirements.txt

4. Ympäristömuuttujien asettaminen (.env-tiedosto):

   - touch .env

5. Avaa .env-tiedosto tekstieditorilla ja lisää sinne seuraavat tiedot:

   ```bash
   DATABASE_URL=postgresql://username:password@localhost/tikawebo

   SECRET_KEY= ## generoi oma avain ##
   ```

6. Tietokannan luominen ja alustaminen

   Varmista, että PostgreSQL-palvelin on käynnissä. Luo tietokanta nimellä, joka vastaa .env-tiedostossa määriteltyä tietokantaa:

   ```bash
   createdb tikawebo
   ```

   Kun suoritat projektin ensimmäistä kertaa, sovellus tarkistaa tietokannan olemassaolon ja luo sen automaattisesti käyttämällä schema.sql-tiedostoa, mikäli tietokantaa ei vielä ole.

   :warning: Mikäli terminaalissa tulee ilmoitus, tyyliin "ei ole oikeuksia tehdä muutoksia tietokantaan tietokantakäyttäjällä X", kokeile seuraavia tietokantaskriptejä

   ```bash
   sudo -i -u postgres psql

   GRANT USAGE, SELECT ON SEQUENCE properties_id_seq TO your_database_user;
   GRANT USAGE, SELECT ON SEQUENCE users_id_seq TO your_database_user;
   GRANT USAGE, SELECT ON SEQUENCE bookings_id_seq TO your_database_user;

   GRANT ALL PRIVILEGES ON TABLE properties TO your_database_user;
   GRANT ALL PRIVILEGES ON TABLE users TO your_database_user;
   GRANT ALL PRIVILEGES ON TABLE bookings TO your_database_user;
   ```

7. Projektin suorittaminen

   Kun olet määrittänyt ympäristömuuttujat ja asentanut riippuvuudet, voit käynnistää Flask-sovelluksen seuraavalla komennolla:

   ```bash
   flask run
   ```
