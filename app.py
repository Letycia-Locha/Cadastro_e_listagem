from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os produtos cadastrados
produtos = []

@app.route("/")
def listar_produtos():
    # Ordenar a lista de produtos pelo valor
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template("listagem.html", produtos=produtos_ordenados)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        # Pegar os dados do formulário
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")
        if valor:
            valor = float(valor)
        else:
            valor = 0.0  # Ou qualquer valor padrão que você queira usar
        disponivel = request.form.get("disponivel")

        # Adicionar produto na lista
        produtos.append({
            "nome": nome,
            "descricao": descricao,
            "valor": valor,
            "disponivel": disponivel
        })

        # Redirecionar para a listagem
        return redirect(url_for("listar_produtos"))

    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)
