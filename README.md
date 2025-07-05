# API de Autos - FastAPI

Este proyecto es una API REST sencilla para gestionar una lista de autos, desarrollada con **FastAPI**. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una colección de autos en memoria.

## ¿Qué puedes hacer con esta API?

- **Listar todos los autos**  
- **Obtener un auto por su ID**
- **Crear un auto nuevo**
- **Actualizar completamente un auto existente (PUT)**
- **Actualizar parcialmente un auto existente (PATCH)**
- **Eliminar un auto por su ID**

---
## 📸 Vista previa
![image](https://github.com/user-attachments/assets/8372c654-de90-4725-8c28-d9a20d81479a)


---
## ¿Cómo ejecutar el proyecto?

1. **Instala las dependencias necesarias**  
   Abre una terminal y ejecuta:
   ```
   pip install fastapi uvicorn
   ```

2. **Inicia el servidor**  
   Desde la carpeta donde está `main.py`, ejecuta:
   ```
   uvicorn main:app --reload
   ```

3. **Abre tu navegador y accede a la documentación interactiva:**  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

   Aquí podrás probar todos los endpoints de la API de forma sencilla.

---

## Endpoints disponibles

- `GET /auto/ALL`  
  Devuelve la lista de todos los autos.

- `GET /auto/{auto_id}`  
  Devuelve los datos de un auto según su ID.

- `POST /auto`  
  Crea un nuevo auto. Debes enviar un JSON con los campos `id`, `marca` y `modelo`.

- `PUT /auto/{auto_id}`  
  Actualiza completamente un auto existente. Debes enviar todos los campos.

- `PATCH /auto/{auto_id}`  
  Actualiza parcialmente un auto existente. Solo envía los campos que quieras modificar.

- `DELETE /auto/{auto_id}`  
  Elimina un auto por su ID.

---

## Notas

- La API utiliza una lista en memoria, por lo que los datos se reinician cada vez que se reinicia el servidor.
- Si accedes a la ruta raíz `/`, verás un mensaje de bienvenida y una sugerencia para visitar `/docs`.

---

## Ejemplo de auto (JSON)

```json
{
  "id": 4,
  "marca": "Toyota",
  "modelo": "Corolla"
}
```

---
