
TABLE = (

    """CREATE TABLE IF NOT EXISTS Sistema (
            codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            
            UNIQUE (nome)
        );
    """,

        """CREATE TABLE IF NOT EXISTS Usuario (
                codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                CPF TEXT NOT NULL,
                
                UNIQUE (CPF)
        );
    """,
        
        """CREATE TABLE IF NOT EXISTS PerfilAcesso (
            codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CodigoSistema INTEGER NOT NULL,
            Nome TEXT NOT NULL,
            Descricao TEXT NOT NULL,
            
            UNIQUE (CodigoSistema, Nome)
        );

    """,

        """CREATE TABLE IF NOT EXISTS PerfilUsuario (
            codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CodigoUsuario INTEGER NOT NULL,
            CodigoPerfilAcesso INTEGER NOT NULL,
            
            UNIQUE (CodigoUsuario, CodigoPerfilAcesso)
        );

    """,

        """CREATE TABLE IF NOT EXISTS MatrizSoD (
            codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CodigoPerfilAcesso1 INTEGER NOT NULL,
            CodigoPerfilAcesso2 INTEGER NOT NULL,
            Descricao TEXT NOT NULL,
            
            UNIQUE (CodigoPerfilAcesso1, CodigoPerfilAcesso2)
        );

    """
)

