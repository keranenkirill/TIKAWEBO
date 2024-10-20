# Rent&Stay - Web-sovellus 🏠   

## [**LOPPUPALAUTUS**](https://github.com/keranenkirill/TIKAWEBO/releases/tag/LOPPUPALAUTUS) :rocket:
### [**Asennusohje & Käyttöohje**](DOKUMENTAATIO/asennusohje.md) 🛠️

📊 [_Kirjanpito & työtila_](https://trello.com/invite/b/66dd979b69f8fe952329e9df/ATTIdecd3e46f5556f7fad0b770e17d14b7f159592A9/tikawebo)  
🤖 [_Laajan kielimallin käyttö projektin kehityksessä (LLM)_](DOKUMENTAATIO/chatgpt_selvitys.md)

---

## Sovelluksen tarkoitus 🎯
Rent&Stay on verkkosovellus, jonka avulla käyttäjät voivat kirjautua sisään, listata vuokrattavia asuntoja ja varata asuntoja. Sovellus tukee myös kirjautuneiden käyttäjien tietojen hallintaa ja listattujen kohteiden näyttämistä.

---

## Toiminnallisuus ⚙️

- ✅ Rekisteröityminen, kirjautuminen ja tilin poistaminen
- 📝 Varausten hallinta (lisääminen / poistaminen)
- 🏘️ Kohteiden lisääminen ja hallinta
- 🔐 Salasanojen turvallinen hajauttaminen

---

## Tietoturva 🛡️

Sovelluksessa on huomioitu seuraavat tietoturva-asiat:

- **XSS (Cross-Site Scripting)**: Kaikki käyttäjän syötteet validoidaan ja estetään haitallisen koodin injektointi.
- **CSRF (Cross-Site Request Forgery)**: Käytössä on CSRF-suojaus, joka estää luvattomien pyyntöjen suorittamisen toisen käyttäjän istunnon nimissä.
- **SQL-injektio**: Kaikki tietokantakyselyt on toteutettu parametrisoituna estääkseen SQL-injektiot.

---

## Tietokanta 📊

Sovellus käyttää **PostgreSQL**-tietokantaa. Seuraavat taulut löytyvät:

| Taulu         | Kuvaus                                          |
| ------------- | ----------------------------------------------- |
| **users**     | Käyttäjien tiedot (id, username, password)       |
| **profiles**  | Käyttäjäprofiilit (id, user_id, email, phone)    |
| **properties**| Vuokrattavat asunnot (id, title, price, etc.)    |
| **bookings**  | Varaukset (id, property_id, user_id, dates)      |
| **reviews**   | Arvostelut (id, user_id, property_id, review)    |

---

## Tuotannon kehitysideoita 💡

### Kehityksessä 🚧

- mikäli listatulla kohteella on varauksia, varmennus kohteen poistamisesta ja siihen liittyvien varauksien poistaisesta
- kokemus-kommentin poistaminen

### Kehitysideoita ✨

- 👍 Tykkäykset
- listaaminen suosion perusteella
- keskiarvon antaminen kohteille
