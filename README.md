# FulBot
Bot de Telegram para asignar 2 equipos de futbol de forma random.

## Uso
Para usar el bot hay dos opciones:

### Usar el bot ya creado en Telegram
Adentro de Telegram podemos buscar al bot como **@fulb0_bot** y hablarle directamente o agregarlo a nuestro grupo.

### Hostear al bot
Si queremos hostear nosotros mismos el bot y por ejemplo, hacer modificaciones y agregar nuevos comandos hacemos lo siguiente:<br>
<br>
Primero debemos entrar a Telegram y buscar a "BotFather" que es el bot oficial de Telegram que se usa para crear y administrar todos los demás bots.<br>
Luego tocamos en "Iniciar" o escribimos ```/start```<br>
Para crear el bot ponemos el comando ```/newbot```<br>
Luego BotFather nos pedirá un nombre para el bot y un nombre de usuario.<br>
Si todo sale bien, nos dará un token, debemos guardarlo.<br>

## Entorno de Python
Para que nuestro bot funcione, necesitamos instalar algunos paquetes que se encuentran en **requeriments.txt**. Podemos instalarlo directamente con ```pip install -r requeriments.txt``` pero lo recomendable es armarse un entorno de python de la siguiente manera:
```bash 
python3 -m venv fulbot
source fulbot/bin/activate
pip install -r requeriments.txt
```
Con esto instalaremos nuestras dependencias dentro del entorno, librandonos de posibles conflictos entre dependencias.<br>
Para salir del entorno solo debemos hacer:
```bash 
deactivate
```

## Token
Ahora, para que el bot funcione en caso que lo estemos hosteando, debemos hacer uso del token que nos dió BotFather. Para esto, debemos crear un archivo llamado **.env** en el directorio principal del repositorio. Dentro del archivo agregamos lo siguiente:
```bash 
TELEGRAM_TOKEN="TOKEN_DE_GODFATHER"
```
Reemplazando claramente por el token que nos dió GodFather.

## Ejecución
Una vez configurado todo esto, solo debemos ejecutar el programa con:
```bash 
python3 main.py
```

