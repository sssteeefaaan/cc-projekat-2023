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

<h2>Detalji</h2>
<ul>
  <li>Ukoliko želite da se povežete na <strong>MongoDB Replica Set</strong> koristeći <strong>Compass</strong> sa host mašine, neophodno je:
    <ol>
      <li>Pronaći u okviru konfiguracionog fajla <code>./load-balancer/mongo/rs-init.sh</code> imena host mašina (Ovo su imena servisa koji su deo replika seta), kao i ime seta replika. Trenutno je konfigurisano kao <code>uns-database-01</code>, <code>uns-database-02</code> i replika set <code>uns-replicaset</code>.
      </li>
      <li>U okviru Vaše host mašine, u fajlu <strong>/etc/hosts</strong>, neophodno je dodati identifikovana imena za adresu <code>127.0.0.1</code> (Ovim kažemo host mašini kako da prepozna članove klastera, a s obzirom da je sve na lokalnoj mašini, oni su dostupni na localhost:{mapiran port})
      </li>
      <li>Formirati konekcioni string za <string>Compass</string> kao <code>mongodb://localhost:{port1},localhost:{port2}/?replicaSet={ime replike}</code> (Za konfiguraciju bilo kakve autentifikacije, a to podrazumeva username i password, neophodno je prilagoditi klaster da radi sa ključevima, kako bi čvorovi komunicirali, te je za ovo dodatno potrebno proučiti <a href="https://www.mongodb.com/docs/manual/tutorial/deploy-replica-set-with-keyfile-access-control/">dokumentaciju</a>)
      </li>
    </ol>
  </li>
</ul>
