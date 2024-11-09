import sqlite3

conn = sqlite3.connect("restaurante.db")


conn.execute(
    """
    CREATE TABLE IF NOT EXISTS platos ( 
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio TEXT NOT NULL
        )

    """

)

conn.execute(
    """
       INSERT INTO platos (nombre, precio) VALUES 
        ('Taco', '10.50'),
        ('Pizza', '15.00'),
        ('Sushi', '20.00'),
        ('Hamburguesa', '8.75'),
        ('Ensalada', '6.50')
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS mesas ( 
        id INTEGER PRIMARY KEY,
        numero TEXT NOT NULL
        
        )

    """

)

conn.execute(
    """
       INSERT INTO mesas (numero) VALUES 
        ('4'),
        ('5'),
        ('6'),
        ('2'),
        ('1')
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS Pedidos( 
        id INTEGER PRIMARY KEY,
        plato TEXT NOT NULL, 
        mesa TEXT NOT NULL, 
        cantidad TEXT NOT NULL, 
        fecha TEXT NOT NULL
        
        )

    """

)

conn.execute(
    """
       INSERT INTO Pedidos (plato, mesa, cantidad, fecha) VALUES 
            ('Taco', 'Mesa 1', '2', '2024-11-09'),
            ('Pizza', 'Mesa 2', '1', '2024-11-09'),
            ('Sushi', 'Mesa 3', '3', '2024-11-09'),
            ('Hamburguesa', 'Mesa 4', '4', '2024-11-09'),
            ('Ensalada', 'Mesa 5', '1', '2024-11-09');
    """
)

conn.commit()