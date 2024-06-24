BEGIN;
--
-- Create model CategoriaProducto
--
CREATE TABLE "uni_segun_categoriaproducto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(255) NOT NULL);
--
-- Create model Direcciones
--
CREATE TABLE "uni_segun_direcciones" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "direccion" varchar(255) NOT NULL, "ciudad" varchar(100) NOT NULL, "codigo_postal" varchar(10) NOT NULL, "pais" varchar(100) NOT NULL);
--
-- Create model Usuario
--
CREATE TABLE "uni_segun_usuario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(255) NOT NULL, "apellido" varchar(255) NOT NULL, "rut" varchar(12) NOT NULL UNIQUE, "academia" varchar(255) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "contraseña" varchar(255) NOT NULL, "numero_de_telefono" varchar(15) NOT NULL UNIQUE, "fecha_registro" datetime NOT NULL);
--
-- Create model Producto
--
CREATE TABLE "uni_segun_producto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(255) NOT NULL, "descripcion" text NOT NULL, "precio" decimal NOT NULL, "categoria_id" bigint NOT NULL REFERENCES "uni_segun_categoriaproducto" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Tarjetas
--
CREATE TABLE "uni_segun_tarjetas" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "numero_tarjeta" varchar(16) NOT NULL, "fecha_expiracion" date NOT NULL, "codigo_seguridad" varchar(4) NOT NULL, "tipo_tarjeta" varchar(50) NOT NULL, "nombre_tarjeta" varchar(225) NOT NULL, "usuario_id" bigint NOT NULL REFERENCES "uni_segun_usuario" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model CarroCompra
--
CREATE TABLE "uni_segun_carrocompra" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "usuario_id" bigint NOT NULL REFERENCES "uni_segun_usuario" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "uni_segun_carrocompra_productos" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "carrocompra_id" bigint NOT NULL REFERENCES "uni_segun_carrocompra" ("id") DEFERRABLE INITIALLY DEFERRED, "producto_id" bigint NOT NULL REFERENCES "uni_segun_producto" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "uni_segun_producto_categoria_id_30e24b82" ON "uni_segun_producto" ("categoria_id");
CREATE INDEX "uni_segun_tarjetas_usuario_id_51a8ad05" ON "uni_segun_tarjetas" ("usuario_id");
CREATE INDEX "uni_segun_carrocompra_usuario_id_7f77b17a" ON "uni_segun_carrocompra" ("usuario_id");
CREATE UNIQUE INDEX "uni_segun_carrocompra_productos_carrocompra_id_producto_id_605289bd_uniq" ON "uni_segun_carrocompra_productos" ("carrocompra_id", "producto_id");
CREATE INDEX "uni_segun_carrocompra_productos_carrocompra_id_497e6f71" ON "uni_segun_carrocompra_productos" ("carrocompra_id");
CREATE INDEX "uni_segun_carrocompra_productos_producto_id_84917b06" ON "uni_segun_carrocompra_productos" ("producto_id");
COMMIT;