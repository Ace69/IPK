#Klient pro OpenWeatherMap API
<br>
### <center>Počítačové komunikace a sítě</center>
### <center>Jakub Dolejší</center>
<br>
### <center>Úvod</center>
Cílem projektu bylo vytvořit klienta, který na základě HTTP requestu získává potřebné informace ze serveru https://openweathermap.org/.
### <center>Popis projektu</center>
Klient přijímá dva parametry; API klíč, který slouží k autorizaci uživatele na server a název města, které uživatel chce vyhledat. Na základě těchto dvou informací vytvoří patřičný HTTP request, který následně odešle na server. V případě chyby je program ukončen s patřičnou chybovou hláškou.
### <center>Implementace</center>
Projekt byl implementován v jazyce Python
