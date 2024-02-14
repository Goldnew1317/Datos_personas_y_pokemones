import os
import requests
import json
import webbrowser

continuar = True

def Limpiar():
    os.system('cls')

def Datos_personas():
    Limpiar()

    print("Este programa te muestra datos del numero del 1 al 10 que digites")

    num = input("Digite el numero o digite x para salir al menu anterior: ")
    if num == 'x'.lower():
        return
    url = "https://jsonplaceholder.typicode.com/users/" + num
    dat = requests.get(url).json()

    try:
        name = dat['name']
        user = dat['username']
        street = dat['address']['street']
        city = dat['address']['city']
        phone = dat['phone'][:12]
    except:
        print("Solo se admiten numeros del 1 al 10")
        input("Presione enter para continuar.....")
        return


    plantilla = """
        <html>
            <div">
                <table>
                    <tr><th> Nombre:</th> 
                    <td> @name </td></tr>
                    <tr><th> Usuario:</th> 
                    <td> @user </td></tr>
                    <tr><th> Calle:</th> 
                    <td> @street </td></tr>
                    <tr><th> Ciudad:</th> 
                    <td> @city </td></tr>
                    <tr><th> Telefono:</th> 
                    <td> @phone </td></tr>
                </table>
                <h3> Program made By / Programa hecho Por: </h3>
                <h4> Newder Manuel Espinosa Davis </h4>
                <h3> API: </h3>
                <h4><a href="https://jsonplaceholder.typicode.com"> https://jsonplaceholder.typicode.com </h4>
            </div>
        </html>
    """.replace('@name',name).replace('@user',user).replace('@street',street).replace('@city',city).replace('@phone',phone)

    F = open('Datos.html','w')
    F.write(plantilla)
    F.close

    print("Cargando...")
    webbrowser.open('Datos.html')

def Datos_pokemon():
    Limpiar()

    print("Este programa te muestra datos del pokemon que digites")

    pokedex = input("Digite el numero del pokemon en el pokedex nacional o digite x para salir al menu anterior: ")
    if pokedex == 'x'.lower():
        return
    url = "https://pokeapi.co/api/v2/pokemon/" + pokedex
    dat = requests.get(url).json()

    try:
        photo = dat['sprites']['other']['official-artwork']['front_default']
        shiny = dat['sprites']['other']['official-artwork']['front_shiny']
        poke = dat['name']
        skill1 = dat['abilities'][0]['ability']['name']
        try:
            skill2 = dat['abilities'][1]['ability']['name']
        except:   
            skill2 = "No tiene segunda habilidad"     
        try:
            skill3 = dat['abilities'][2]['ability']['name']
        except:   
            skill3 = "No tiene tercera habilidad"     
        hp = dat['stats'][0]['base_stat']
        atq = dat['stats'][1]['base_stat']
        dfs = dat['stats'][2]['base_stat']
        spatq = dat['stats'][3]['base_stat']
        spdfs = dat['stats'][4]['base_stat']
        speed = dat['stats'][5]['base_stat']
        total = hp + atq +dfs + spatq + spdfs + speed
        type1 = dat['types'][0]['type']['name']
        try:
            type2 = dat['types'][1]['type']['name']
        except:
            type2 = "No tiene segundo tipo"
    except:
        print("Solo se admiten numeros del pokedex nacional")
        input("Presione enter para continuar.....")
        return

    plantilla = """
        <html>
            <div">
                <table>
                    <tr><td><img src= "@photo" alt="Lo siento, la imagen no se puede mostrar" width="150" height="150"> </td>
                    <td><img src= "@shiny" alt="Lo siento, la imagen no se puede mostrar" width="150" height="150"> </td></tr>
                    <td> - Datos: </td>
                    <tr><th> Pokemon:</th> 
                    <td> @poke </td></tr>
                    <tr><th> Habilidad 1:</th> 
                    <td> @skill1 </td></tr>
                    <tr><th> Habilidad 2:</th> 
                    <td> @skill2 </td></tr>
                    <tr><th> Habilidad 3:</th> 
                    <td> @skill3 </td></tr>
                    <td> - STATS: </td>
                    <tr><th> Hp:</th> 
                    <td> @hp </td></tr>
                    <tr><th> Ataque:</th> 
                    <td> @atq </td></tr>
                    <tr><th> Defensa:</th> 
                    <td> @dfs </td></tr>
                    <tr><th> Ataque Especial:</th> 
                    <td> @spatq </td></tr>
                    <tr><th> Defensa Especial:</th> 
                    <td> @spdfs </td></tr>
                    <tr><th> Velocidad:</th> 
                    <td> @speed </td></tr>
                    <tr><th> Total stats:</th> 
                    <td> @total </td></tr>
                    <td> - Tipos: </td>
                    <tr><th> Tipo 1:</th>
                    <td> @type1 </td></tr>
                    <tr><th> Tipo 2:</th> 
                    <td> @type2 </td></tr>
                </table>
                <h3> Program made By / Programa hecho Por: </h3>
                <h4> Newder Manuel Espinosa Davis </h4>
                <h3> API: </h3>
                <h4><a href="https://pokeapi.co"> https://pokeapi.co </h4>
            </div>
        </html>
    """.replace('@photo',str(photo)).replace('@shiny',str(shiny)).replace('@poke',str(poke)).replace('@skill1',str(skill1)).replace('@skill2',str(skill2)).replace('@skill3',str(skill3)).replace('@hp',str(hp)).replace('@atq',str(atq)).replace('@dfs',str(dfs)).replace('@spatq',str(spatq)).replace('@spdfs',str(spdfs)).replace('@speed',str(speed)).replace('@total',str(total)).replace('@type1',str(type1)).replace('@type2',str(type2))

    F = open('Pokes.html','w')
    F.write(plantilla)
    F.close

    print("Cargando...")
    webbrowser.open('Pokes.html')


while continuar:
    Limpiar()
    print("Elige la opcion a la que quieras acceder")
    print("1. Datos de personas")
    print("2. Datos de pokemones")
    print("3. Salir")
    tmp = input("Digite la opcion aqui: ")
    if tmp == '1':
        Datos_personas()
    elif tmp == '2':
        Datos_pokemon()
    elif tmp == '3':
        print("Gracias por usar el programa 😊😊😊")
        continuar = False
    else:
        print("Por favor digite una opcion valida")
        input("Presione Enter para continuar.....")

