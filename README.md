# kafka_python_base
***
## Descripción
Proyecto para crear localmente un servicio Kafka basico. Además se entregaran dos modulos python (producer y consumer), los cuales sera los encargados de generar y leer los mensajes en Kafka.
***
## Estuctura del proyecto
~~~
├── docker-compose.yaml 
├── requirements.txt  
├── kafka_utils  
    ├── main.py  
    ├── producer.py  
    ├── consumer.py
~~~
***
## Instalación y uso
Para poder utilizar esta api en Windows debemos tener instalado WSL2 y Docker Desktop. En caso de querer utilizarla en macOS o distros Linux, no hace falta instalar nada ya que se puede ejecutar nativamente.  
Una vez instalados los requisitos anteriores debemos clonar el repositorio con el siguiente comando:  
~~~
git clone https://github.com/Marcosgdelgado/kafka_python_base.git --config core.autocrlf=input
~~~

Todos los comandos utilizados para descargar e instalar los requisitos son para la terminal CMD.

Debemos crear un entorno virtual donde instalaremos nuestras librerias externas:
~~~
python -m venv venv
~~~
Para activar dicho entorno virtual debemos ingresar el siguiente comando por consola:
~~~
.\venv\Scripts\activate
~~~
Por ultimo, debemos instalar nuestro archivo requirements.txt, el cual contendra las librerias necesarias:
~~~
pip install requirements.txt -r
~~~
Luego, debemos abrir el proyecto en nuestro IDE o acceder a la ruta principal mediante nuestra terminar e ingresar por consola el siguiente comando:
~~~
docker-compose up --build
~~~  
Esto construirá nuestro servicio kafka en docker, ingresaremos a al CLI en Docker e ingresaremos el siguiente comando:
~~~
/opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
~~~
Luego en otra consola ingresaremos el siguiente comando para generar nuestros mensajes:
~~~
python producer.py
~~~
Luego en otra consola ingresaremos el siguiente comando para leer nuestros mensajes:
~~~
python consumer.py
~~~
***
## Tecnogías utilizadas
- Python 3.11
- Docker
- Kafka
- CMD
***
