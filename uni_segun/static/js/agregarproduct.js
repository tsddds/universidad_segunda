$(document).ready(function() {
    let totalPrecio = 0;  // Inicializa el total de precios acumulado
    let cantidadGeneral = 0;  // Inicializa la cantidad total de productos en el carrito

    // Evento al hacer clic en botones de "Añadir al carro" en cada producto
    $('.btn-outline-warning').on('click', function() {
        const card = $(this).closest('.card');  // Encuentra la tarjeta del producto más cercana
        const itemTitulo = card.find('h5').text();  // Obtiene el título del producto
        const itemPrecio = card.find('.text-body-secondary').text();  // Obtiene el precio del producto
        const itemImagen = card.find('div[style*="background-image"]').css('background-image').replace('url("', '').replace('")', '');  // Extrae la URL de la imagen de fondo

        const nuevoProducto = {
            titulo: itemTitulo,
            precio: itemPrecio,
            imagen: itemImagen,
            cantidad: 1
        };

        agregarAlCarrito(nuevoProducto);  // Llama a la función para agregar el producto al carrito
    });

    function agregarAlCarrito(producto) {
        let precio = parseInt(producto.precio.replace(/\D/g, ""));  // Elimina todos los caracteres no numéricos del precio y convierte a entero
        let encontrado = false;  // Bandera para verificar si el producto ya está en el carrito

        // Recorre todos los productos en el carrito para verificar si el producto ya existe
        $('.row-product').each(function() {
            let titulo = $(this).find('.text-truncate').text().trim();
            if (titulo === producto.titulo) {
                let cantidadElement = $(this).find('h6 span');
                let cantidad = parseInt(cantidadElement.text());
                cantidad++;
                cantidadElement.text(cantidad);  // Actualiza la cantidad del producto
                totalPrecio += precio;  // Aumenta el precio total del carrito
                cantidadGeneral += 1;  // Incrementa la cantidad total de productos
                encontrado = true;
            }
        });

        // Si el producto no se encuentra en el carrito, se añade un nuevo elemento
        if (!encontrado) {
            totalPrecio += precio;
            cantidadGeneral += 1;
            const productoHTML = `
                <div class="row-product" data-title="${producto.titulo}" data-precio="${precio}">
                    <div class="cart-product">
                        <div class="container text-center">
                            <div class="row justify-content-start">
                                <div class="col-4">
                                    <img src="${producto.imagen}" class="img-fluid" style="max-height: 60px;" alt="${producto.titulo}">
                                </div>
                                <div class="col-4">
                                    <h5 class="text-truncate">${producto.titulo}</h5>
                                    <h6><span>1</span>X${producto.precio}</h6>
                                </div>
                                <div class="col-4 d-flex justify-content-center align-items-center" style="padding-left:90px;">
                                    <button type="button" class="btn-close delete-btn" aria-label="Close"></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </div>
            `;
            $('.offcanvas-body').append(productoHTML);  // Añade el nuevo producto al carrito visual en el DOM
        }
        actualizarContadorCarrito();  // Actualiza el contador de productos y el precio total
    }

    // Evento al hacer clic en el botón "cerrar" para eliminar productos o disminuir su cantidad
    $('.offcanvas-body').on('click', '.btn-close', function() {
        const rowProduct = $(this).closest('.row-product');
        let cantidad = parseInt(rowProduct.find('h6 span').text());
        let precio = parseInt(rowProduct.data('precio'));  // Obtiene el precio del producto almacenado en el atributo de datos
        if (cantidad > 1) {
            cantidad--;
            rowProduct.find('h6 span').text(cantidad);
            totalPrecio -= precio;
            cantidadGeneral--;
        } else {
            totalPrecio -= precio;
            rowProduct.remove();  // Elimina el producto del DOM
            cantidadGeneral--;
        }
        actualizarContadorCarrito();  // Actualiza el contador de productos y el precio total
    });

    // Función para actualizar el contador de productos y el total de precios en el carrito
    function actualizarContadorCarrito() {
        $('.badge').text(cantidadGeneral + ' ');  // Muestra la cantidad total de productos en el carrito
        $('.total-pagar').text(`Total a pagar: $${totalPrecio}`);  // Muestra el precio total en el carrito
    }

    $('.desabilitado').click(function() {
        alert("No esta habilitado la BD");
    })
});
