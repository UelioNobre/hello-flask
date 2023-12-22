# Hello Flask!

Estudo sobre o framework Flask.

Para criar uma aplicação Web simples com Flask, para instalar com o comando pip:

```bash
pip install Flask
```

Após a instalação, importe a classe `Flask`, biblioteca do `flask` no seu script.

```python
from flask import Flask
```

### O básico
Um aplicação Flask, começa criando uma instancia da classe Flask no seu script e atribuindo em alguma variável. Na instanciação da classe `Flask`, passe como parâmetro a palavra reservada `__name__` (_dunder name_), pois em algum momento futuro, dentro do seu script, será preciso acessar novamente está instância recém criada.


<details>
  <summary>Exemplo</summary>

  ```python
  from flask import Flask
  app = Flask(__name__)
  ```

</details>

---

### Primeiro endpoint 
Para criar algum `endpoint` utilizando o framework `Flask`, use a seguinte _annotation_ `@app.route()`, com o endpoint como parâmetro da função `route`, em cima de algum método.


Para concluir o minímo de uma aplicação `Flask`, é preciso chamar o método `run()`, disponível na váriavel `app`.

É possível passar alguns parâmetros úteis no método `run()`, como por exemplo porta, modo execução e endereço do servidor.

<details>
  <summary>Exemplo</summary>

  ```python
  from flask import Flask

  
  app = Flask(__name__)

  @app.route("/")
  def ola():
    return 'Ola mundo!'
  
  if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
  
  ```

</details>


# Primeiro endpoint `json`

Para disponibilizar dados em formato `json` em uma aplicação `Flask`, deve-se utilizar o método disponível no módulo `jsonify`.

<details>
  <summary>Exemplo</summary>

  ```python
  from flask import Flask, jsonify

  @app.route("/")
  def ola():
    return jsonify({'msg': 'Ola mundo!'})

  # ...
  ```

</details>