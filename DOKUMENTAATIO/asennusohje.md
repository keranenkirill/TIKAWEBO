# Asennusohje - Rent&Stay

(Tässä asennusohjeessa ei huomioida projektin asennusta Windows-koneelle)

1. Lataa projekti GitHubista
   '''bash
   git clone https://github.com/keranenkirill/TIKAWEBO.git
   '''

2. Virtuaaliympäristön luominen ja aktivoiminen:
   Virtuaaliympäristö auttaa hallitsemaan projektisi riippuvuuksia ja estämään ristiriitoja muiden projektien kanssa.

   mene siis projektin kotihakemistoon, jonka tulisi näyttää tältä: ~/Documents/TKT/TIKAWEBO_S24/TIKAWEBO$

   suorita a.o komento, joka luo projektille virtuaaliympäristön

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

   oman avaimen generointi:
   '''bash
   $ python3
   import secrets
   secrets.token_hex(16)
   '''

7. Web-sovelluksen käynnistäminen:

   Postgresql:ssä on suotavaa jokaiselle projektille luoda oma tietokanta-käyttäjä.
   Tämä hoituu terminaalissa komennolla:
   '''bash
   psql -d postgres -f ./scripts/initdb.sql
   '''

   tämän jäkeen voidaan suorittaa sovelluksen käynnistyskomento:
   '''bash
   flask run
   '''

   Tähän komentoon on integroitu tietokantataulujen automaattinen alustus

   Kun olet määrittänyt ympäristömuuttujat ja asentanut riippuvuudet, voit käynnistää Flask-sovelluksen seuraavalla komennolla:

   ```bash
   flask run
   ```

   Tämän komennon ajettuasi, projektiin alustetaan tietokanta-taulut ja ohjelma on suoritettavissa
   [_käyttöohje_](DOKUMENTAATIO/asennusohje.md)
