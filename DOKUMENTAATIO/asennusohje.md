# Asennusohje - Rent&Stay

(Tässä asennusohjeessa ei huomioida projektin asennusta Windows-koneelle)

#### Tämä asennusohje toimii ongelmitta, mikäli ET ole asentanut PostgreSQL:ää kurssin asennusskritptillä, vaan PostgreSQL:n omilta sivuilta

1. Lataa projekti GitHubista

   ```bash
   git clone https://github.com/keranenkirill/TIKAWEBO.git
   ```

2. Virtuaaliympäristön luominen ja aktivoiminen:
   Virtuaaliympäristö auttaa hallitsemaan projektisi riippuvuuksia ja estämään ristiriitoja muiden projektien kanssa.

   mene siis projektin kotihakemistoon, jonka tulisi näyttää tältä:

   ```bash
   ~/.../TIKAWEBO$
   ```

   Suorita a.o komento, joka luo projektille virtuaaliympäristön:

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

6. Avaa .env-tiedosto tekstieditorilla ja lisää sinne seuraavat rivit:

   ```bash
   DATABASE_URL=postgresql://rsuser:rspass@localhost/rsdb

   SECRET_KEY= ## generoi oma avain ##
   ```

   Oman avaimen generointi:

   ```bash
   $ python3
   import secrets
   secrets.token_hex(16)
   ```

7. Web-sovelluksen käynnistäminen:

   Postgresql:ssä on suositeltaaa jokaiselle projektille luoda oma tietokanta-käyttäjä.
   Tämä hoituu terminaalissa komennolla:

   ```bash
   psql -d postgres -f ./scripts/initdb.sql
   ```

   Kun kyse on projektin ensimmäisestä suorituskerrasta, aja komento:

   ```bash
   flask run
   ```

   Tällä suorituskerralla alustetaan tietokanta-taulut.

   #### lisäohje kurssin [**asennusskritptillä asentaneille**](./asennusohje_kurssi_skripti.md)

   Seuraavaksi suorita kaksi komentoa, jotta saadaan admin käyttäjä ja sen data tietokantaan:

   ```bash
   psql -d postgres -f ./scripts/populate.sql

   ```

   ja käynnistetään projekti

   ```bash
   flask run
   ```

   Nyt, ku avaat projektin, voit kirjautua esimerkkikäyttäjänä:
   user: admin
   password: admin123
   Tässä lähinnä on tarkoituksena, että olisi valmiiksi kiinteistöjä mitä vuokrata, kun luot itse oman käyttäjän :blush:

   [KÄYTTÖOHJE](https://github.com/keranenkirill/TIKAWEBO/blob/main/DOKUMENTAATIO/k%C3%A4ytt%C3%B6ohje.md)
