# Rent&Stay - web sovellus

- [_kirjanpito & työtila_](https://trello.com/invite/b/66dd979b69f8fe952329e9df/ATTIdecd3e46f5556f7fad0b770e17d14b7f159592A9/tikawebo)
- [_asennusohjeet_](./TIKABEBO/DOKUMENTAATIO/asennusohje.md).
- [_Laajan kielimallin käyttö projektin kehityksessä (LLM)_](./TIKAWEBO/DOKUMENTAATIO/chatgpt_selvitys.md)

## Sovelluksen tarkoitus

Rent&Stay on verkkosovellus, jonka avulla käyttäjät voivat kirjautua sisään, listata vuokrattavia asuntoja ja varata asuntoja. Sovellus tukee myös kirjautuneiden käyttäjien tietojen hallintaa ja listattujen kohteiden näyttämistä.

### Toiminallisuus

Käyttäjät voivat rekisteröityä, kirjautua sisään ja ulos, hallita varauksiaan, sekä lisätä vuokrattavia kohteita. Kirjautumisen yhteydessä käytetään salasanojen hajauttamista.

### Tietokanta

Sovellus käyttää PostgreSQL-tietokantaa. Seuraavat taulut löytyvät:

users: Käyttäjien tiedot (id, username, password).
properties: Vuokrattavat asunnot (id, title, price, description, image_url, user_id).
bookings: Varaukset (id, property_id, user_id, start_date, end_date).

Käyttäjän lisäämät kuvat tallennetaan static/images/-kansioon ja liitetään kohteen tietoihin tietokannan kautta. Kuvien maksimikoko on 2 MB.S

### Tuotannon kehitysideoita/ -taskeja
