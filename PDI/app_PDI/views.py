from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Produtos
import pdb
"""import pyrebase

config = {
    "apiKey": "AIzaSyALk1BtgWC5ObEN6Ha2JDjMl6KSgZvFr90",
    "authDomain": "pdi-system.firebaseapp.com",
    "projectId": "pdi-system",
    "storageBucket": "pdi-system.appspot.com",
    "messagingSenderId": "498525661804",
    "appId": "1:498525661804:web:5642764fd6d639d5638649",
    "measurementId": "G-YCWBD457E4"
}
firebase=pyrebase."""

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def vendas(request):
    carrinho = request.session.get('carrinho', {})
    
    

    if request.method == 'GET':
        nome_produto = request.GET.get('produto')
        quantidade = request.GET.get('quantidade')

        # Suponha que você busca o produto no banco de dados com base no nome
        try:
            produto = Produtos.objects.get(nome=nome_produto)
            print(f"name = {produto.nome}")

            # Verificar se a quantidade do produto é suficiente
            if produto.quantidade <= 0:
                print(f"Produto com nome {nome_produto} está fora de estoque")
            elif produto.quantidade < int(quantidade):
                print(f"Não há quantidade suficiente do produto {nome_produto} no estoque")
            else:
                produto.quantidade -= int(quantidade)
                produto.save()

                carrinho = request.session.get('carrinho', {})
                if not isinstance(carrinho, dict):
                    carrinho = {}
                
                if nome_produto in carrinho:
                    if isinstance(carrinho[nome_produto], dict):
                        carrinho[nome_produto]['quantidade'] += int(quantidade)
                        carrinho[nome_produto]['total'] = int(carrinho[nome_produto]['quantidade']) * int(produto.valor)
                        print(carrinho[nome_produto]['total'])
                        
                    else:
                        carrinho[nome_produto] = {'quantidade': int(quantidade), 'valor': produto.valor, 'total': int(quantidade) * int(produto.valor)}
                else:
                    carrinho[nome_produto] = {'quantidade': int(quantidade), 'valor': produto.valor, 'total': int(quantidade) * int(produto.valor)}
                
                carrinho['total_do_carrinho'] = sum(int(item['total']) for item in carrinho.values() if isinstance(item, dict))
                
                
                

                request.session['carrinho'] = carrinho

                
                
                

        except Produtos.DoesNotExist:
            # Caso o produto não seja encontrado, você pode tratar isso aqui[
            print(f"Produto com nome {nome_produto} não encontrado")

    return render(request, 'vendas/caixa/caixa.html', {'carrinho': carrinho})

def caixa(request):
    pass

    #return render(request, 'seu_template.html', {'produto': produto})

def get_produto(request):
    if request.method == 'GET':
        nome_produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')

        try:
            produto = Produtos.objects.get(nome=nome_produto)
            return {
                "produto": produto,
                "quantidade": quantidade, 
            }
        
        except Produtos.DoesNotExist:
            print("Produto não encontrado")

def cadrasto_estoque(request):
    return render(request, 'estoque/adicionar_estoque.html')

def estoque_home(request):
    return render(request, "estoque/home_estoque.html")

def push_estoque(request):
    if request.method == 'POST':
        # Obtendo os dados do formulário
        nome_produto = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        valor = request.POST.get('valor')
        validade = request.POST.get('validade')
        lucro = request.POST.get('lucro')
        img = request.FILES['img'] if 'img' in request.FILES else None

        # Verificando se o produto já existe no banco de dados
        if not Produtos.objects.filter(nome=nome_produto).exists():
            # Se não existe, cria um novo objeto de Produto e salva no banco de dados
            produto = Produtos(nome=nome_produto, quantidade=quantidade, valor=valor, validade=validade, lucro=lucro, img=img)
            produto.save()
            print("Produto criado:", produto.nome)
        else:
            # Se o produto já existe, atualiza os campos e salva
            produto = Produtos.objects.get(nome=nome_produto)
            produto.quantidade = quantidade
            produto.valor = valor
            produto.validade = validade
            produto.lucro = lucro
            produto.img = img
            produto.save()
            print("Produto atualizado:", produto.nome)

    # Após salvar ou atualizar, obtenha todos os produtos novamente para renderizar a página
    produtos = {
        'produtos': Produtos.objects.all()
    }

    return render(request, 'estoque/adicionar_estoque.html', produtos)

def estoque(request):
    produtos = {
            'produtos': Produtos.objects.all()
        }
    return render(request, 'estoque/estoque.html', produtos)

def get_estoque(request):
    pass

def codrasto_funcionarios(request):
    return render(request, "RH/contratacao.html")

def finalizar_compra(request):
    # Limpa o carrinho
    request.session['carrinho'] = {}
    # Redireciona o usuário para a página de vendas
    return redirect('vendas')