def dibujar_letras():
    letras = [
        # D
        ["********  ",
         "*       * ",
         "*       * ",
         "*       * ",
         "*       * ",
         "*       * ",
         "********  "],
        
        # Espacio entre letras
        ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
 
        # U
        ["*       * ",
         "*       * ",
         "*       * ",
         "*       * ",
         "*       * ",
         "*       * ",
         " *******  "],
 
        # Espacio entre letras
        ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
 
        # N
        ["*       *",
         "**      *",
         "* *     *",
         "*  *    *",
         "*   *   *",
         "*    *  *",
         "*     ***"]
    ]
 
    for i in range(7):  # 7 líneas de alto
        for letra in letras:
            print(letra[i], end="")
        print()
 
dibujar_letras()