
# T2-24-2-Backend

Para utilizar esta API, deben usar la siguiente URL base: https://t2-24-2-backend.onrender.com. En el endpoint `/docs` está la documentación de la API o en el siguiente [link](https://t2-24-2-backend.onrender.com/docs).

## ¿Cómo correr la API?

En caso de que haya problemas con el link anterior, ustedes pueden correr la API en su computador sin problemas. Para ello, deberán seguir los siguientes pasos (pensados para Ubuntu o WSL):

1. Clonar este repositorio T2-24-2-Backend en su computador.
2. Tener [docker](https://docs.docker.com/engine/install/) y [docker compose](https://docs.docker.com/compose/install/) instalados en su computador.
3. Crear un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:

    ```plaintext
    DATABASE_URL=postgresql://postgres:password@db:5432/recipes
    DB_USER=postgres
    DB_PASSWORD=password
    DB_NAME=recipes
    ```

4. Correr el comando `docker compose up --build -d`.
5. Ingresar a http://localhost:8000 para ver la API.
