class CarritoDeCompras(object):
	"""Crea objetos de carritos de compras
	para los usuarios de nuestro elegante sitio web."""
	items_en_carrito = {}
	def __init__(self, nombre_cliente):
		self.nombre_cliente = nombre_cliente
		
	def agregar_item(self, producto, precio):
		"""Agrega un producto al carrito."""
		self.producto = producto
		self.precio = precio
		
		if not producto in self.items_en_carrito:
			self.items_en_carrito[producto] = precio
			print producto + " agregado."
		else:
			print producto + " ya fue incluido en el carrito."
		
	def eliminar_item(self, producto):
		self.producto = producto
		if producto in self.items_en_carrito:
			del self.items_en_carrito[producto]
			print producto + " eliminado."
		else:
			print producto + " no está incluido en el carrito."
mi_carrito = CarritoDeCompras("mi_carrito")
mi_carrito.agregar_item("Leche", 5.25)
    