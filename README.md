<h1>Projekat iz predmeta <em>Računarstvo u oblaku (Cloud Computing)</em></h1>
<p>Student: <strong>Stefan Aleksić E2-42-2022</strong></p>

<h2>Pokretanje aplikacije</h2>
<ol>
  <li>Pozicionarati se u okviru direktorijuma <strong>./cc-projekat-2023</strong></li>
  <li>Izvršiti komandu</br>
    <code>docker-compose up</code>
  </li>
</ol>

<h2>Zaustavljanje aplikacije</h2>
<ol>
  <li>Pozicionarati se u okviru direktorijuma <strong>./cc-projekat-2023</strong></li>
  <li>Izvršiti komandu</br>
    <code>docker-compose down -v</code>
  </li>
</ol>

<h2>Konfiguracija aplikacije</h2>
<p>U okviru fajla <code>.env</code> nalaze se promenljive okruženja kojima se mogu konfigurisati:
<ul>
  <li>Verzije docker slika koje se koriste za servise</li>
  <li>Portovi host mašine koji se koriste za mapiranje na servisa</li>
  <li>Username, password i ime baze koje se kreiraju u okviru servisa baze postgres</li>
  <li>Username, password i email za administratora Django aplikacija</li>
</ul>
