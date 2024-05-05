document.addEventListener('DOMContentLoaded', function() {
    // Obtener los botones "Agregar al Carrito"
    const botonesAgregar = document.querySelectorAll('.boton-item');

    // Agregar eventos de clic a los botones "Agregar al Carrito"
    botonesAgregar.forEach(boton => {
        boton.addEventListener('click', agregarAlCarrito);
    });

    // Función para agregar un artículo al carrito
    function agregarAlCarrito(event) {
        const item = event.target.parentElement;
        const titulo = item.querySelector('.titulo-item').textContent;
        const precio = item.querySelector('.precio-item').textContent;

        // Crear un nuevo elemento de lista para el carrito
        const nuevoItem = document.createElement('li');
        nuevoItem.textContent = `${titulo} - ${precio}`;

        // Agregar el nuevo elemento a la lista del carrito
        const listaCarrito = document.getElementById('lista-carrito');
        listaCarrito.appendChild(nuevoItem);
    }

    

  

    
});