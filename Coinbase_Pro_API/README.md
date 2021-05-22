#Coinbase Pro API

En esta carpeta se iran agregando proyectos que impliquen utilizar la API de Coinbase PRO. 

##Consideraciones: 

- Es necesario tener una cuenta en Coinbase.

- En todos los proyectos se hara uso de la sandbox de Coinbase Pro (equivalente a una cuenta demo)

- Es importante configurar correctamente la API Key seleccionando solo los permisos mínimos (View y Trade)

- Almacenar los parametros necesarios de la API Key en un fichero diferente al script. En este caso data_api.

- El uso de la API que se conecta a vuestra cuenta real con dinero real es bajo vuestro riesgo.

##Configuracion de la API Key

Para generar la conexión a la API tenemos que acceder con nuestra cuenta de Coinbasepro a https://public.sandbox.pro.coinbase.com/. Una vez hecho el login, accedemos al usuario y seleccionamos la opción API. 

Seleccionamos la opción +New API Key

Nos aparecerá una pantalla con la información correspondiente a Portfolio, API Key Nickname, Permissions, Passphrase e IP Whitelist.
Como comente previamente los permisos a seleccionar son View y Trade, os invito a que busqueis que significa o que habilita cada uno de estos permisos y porque NO se debe usar Transfer bajo ningún concepto.
El valor que nos muestra en Passphrase debe ser almacenado.

Seleccionamos la opción 'CREATE API KEY'

Nos mostrara una pantalla en la que nos dice que se ha creado la API Key y nos proporciona la API Secret, la cual debemos almacenar.

Seleccionamos DONE.

Nos mostrara la pantalla resumen de nuestras API Keys y aparecerá la public key de la API Key que acabamos de crear. Es la que se encuentra entre el nombre del portfolio y el nickname.
Almacenamos este valor y ya tendríamos todos los datos necesarios para conectarnos a la API de Coinbase Pro.

Para más información visita la documentación de la API de Coinbase Pro https://docs.pro.coinbase.com/

##BTC-Dollar-Cost-Average.py

Si alguna vez has visto aplicaciones o webs que te permiten hacer DCA comprando cryptos y te ha parecido interesante este proyecto es para ti.

Concretamente este script emula un DCA, comprando Bitcoin cada hora si su precio se encuentra por debajo de un precio límite establecido.
Este script se puede modificar para que funcione con cualquier crypto y monto, siempre que supere el mínimo establecido por Coinbase pro.

Se aceptan sugerencias de estrategias de trading para implementarlas en futuros proyectos ⚙️

