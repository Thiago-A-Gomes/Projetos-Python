from flask import Flask, jsonify,request


app = Flask(__name__)


livros =[
    
  {
    "id": 1,
    "titulo": "Café com Deus",
    "autor": "Junior Rostirola"
  },
  {
    "id": 2,
    "titulo": "Avivamento: Um Chamado Para a Renovação Espiritual",
    "autor": "Martyn Lloyd-Jones",
    "detalhes": "Uma análise profunda sobre a natureza e a necessidade do avivamento espiritual."
  },
  {
    "id": 3,
    "titulo": "Uma Vida com Propósitos",
    "autor": "Rick Warren",
    "detalhes": "Um guia prático para descobrir e viver o propósito de Deus para sua vida."
  },
  {
    "id": 4,
    "titulo": "Fé Inabalável: Enfrentando as Tempestades da Vida",
    "autor": "Max Lucado",
    "detalhes": "Mensagens de esperança e encorajamento para momentos difíceis."
  },
  {
    "id": 5,
    "titulo": "O Poder da Oração e da Fé em Deus",
    "autor": "W. Phillip Keller",
    "detalhes": "Reflexões sobre a importância da oração e da fé na vida cristã."
  },
  {
    "id": 6,
    "titulo": "O Vento Sopra Onde Quer",
    "autor": "Richard Owen Roberts",
    "detalhes": "Um estudo sobre o avivamento espiritual, com foco no avivamento no País de Gales."
  },
  {
    "id": 7,
    "titulo": "Quando o Espírito vem com Poder",
    "autor": "John White",
    "detalhes": "Explora o impacto do avivamento da Rua Azusa e a obra do Espírito Santo."
  },
  {
    "id": 8,
    "titulo": "Heróis da Fé",
    "autor": "Orlando Boyer",
    "detalhes": "Biografias de missionários e líderes cristãos que impactaram o mundo."
  },
  {
    "id": 9,
    "titulo": "Deus em Questão: Debates Contemporâneos sobre o Ateísmo Moderno",
    "autor": "Alister McGrath",
    "detalhes": "Uma defesa da fé cristã em face dos argumentos ateístas."
  },
  {
    "id": 10,
    "titulo": "Cristianismo Puro e Simples",
    "autor": "C.S. Lewis",
    "detalhes": "Uma explicação clara e concisa dos princípios básicos do cristianismo."
  },
  {
    "id": 11,
    "titulo": "O Peregrino",
    "autor": "John Bunyan",
    "detalhes": "Uma alegoria clássica sobre a jornada espiritual do cristão."
  },
  {
    "id": 12,
    "titulo": "O Peso da Glória",
    "autor": "C.S. Lewis",
    "detalhes": "Ensaios sobre a natureza da glória de Deus e seu significado para os cristãos."
  },
  {
    "id": 13,
    "titulo": "A Imitação de Cristo",
    "autor": "Tomás de Kempis",
    "detalhes": "Um guia devocional clássico sobre a vida cristã."
  },
  {
    "id": 14,
    "titulo": "Confissões",
    "autor": "Santo Agostinho",
    "detalhes": "A autobiografia espiritual de Santo Agostinho, um clássico da literatura cristã."
  },
  {
    "id": 15,
    "titulo": "Teologia Sistemática",
    "autor": "Wayne Grudem",
    "detalhes": "Uma obra abrangente que explora as principais doutrinas da fé cristã."
  },
  {
    "id": 16,
    "titulo": "O Poder da Oração",
    "autor": "E.M. Bounds",
    "detalhes": "Um livro clássico sobre a importância e o poder da oração."
  },
  {
    "id": 17,
    "titulo": "Em Seus Passos o Que Faria Jesus?",
    "autor": "Charles Sheldon",
    "detalhes": "Um romance que desafia os leitores a viverem como Jesus."
  },
  {
    "id": 18,
    "titulo": "Cartas de um Diabo a seu Aprendiz",
    "autor": "C.S. Lewis",
    "detalhes": "Uma sátira sobre as tentações e estratégias do mal."
  },
  {
    "id": 19,
    "titulo": "A Cabana",
    "autor": "William P. Young",
    "detalhes": "Um romance que explora temas de fé, perdão e o amor de Deus."
  },
  {
    "id": 20,
    "titulo": "O Grande Conflito",
    "autor": "Ellen G. White",
    "detalhes": "Uma visão da história do conflito entre o bem e o mal."
  },
    {
    "id": 21,
    "titulo": "Caminho a Cristo",
    "autor": "Ellen G. White",
    "detalhes": "Um guia prático para a vida cristã."
  },
    {
    "id": 22,
    "titulo": "Mensagens aos Jovens",
    "autor": "Ellen G. White",
    "detalhes": "Conselhos para jovens sobre diversos aspectos da vida à luz da fé cristã."
  },
    {
    "id": 23,
    "titulo": "A Cruz e o Punhal",
    "autor": "David Wilkerson",
    "detalhes": "A história do trabalho de David Wilkerson com gangues em Nova York."
  },
  {
    "id": 24,
    "titulo": "O Deus que Destrói Sonhos",
    "autor": "Rodrigo Bibo",
    "detalhes": "Reflexões sobre a soberania de Deus e seus propósitos."
  },
    {
    "id": 25,
    "titulo": "A Batalha de Cada Um",
    "autor": "Stephen Arterburn e Fred Stoeker",
    "detalhes": "Um livro sobre pureza sexual para homens cristãos."
  },
    {
    "id": 26,
    "titulo": "Mulheres que Correm com os Lobos",
    "autor": "Clarissa Pinkola Estés",
    "detalhes": "Uma análise da psique feminina através de mitos e contos de fadas. (Pode ser interpretado de uma perspectiva cristã)"
  },
    {
    "id": 27,
    "titulo": "Bíblia de Estudo MacArthur",
    "autor": "John MacArthur",
    "detalhes": "Uma Bíblia com notas e comentários para estudo aprofundado."
  },
    {
    "id": 28,
    "titulo": "Comentário Bíblico Matthew Henry",
    "autor": "Matthew Henry",
    "detalhes": "Um comentário bíblico clássico e abrangente."
  },
    {
    "id": 29,
    "titulo": "O Livro de Eli",
    "detalhes": "(Filme/Roteiro) Uma história pós-apocalíptica com temas de fé e redenção."
  },
    {
    "id": 30,
    "titulo": "O Cristão em Busca de Deus",
    "autor": "A.W. Tozer",
    "detalhes": "Um clássico sobre a busca pela presença de Deus."
  },
    {
    "id": 31,
    "titulo": "Conhecendo a Deus",
    "autor": "J.I. Packer",
    "detalhes": "Um estudo profundo sobre os atributos de Deus."
  },
    {
    "id": 32,
    "titulo": "A Graça Surpreendente",
    "autor": "Philip Yancey",
    "detalhes": "Uma exploração do conceito da graça divina."
  },
    {
    "id": 33,
    "titulo": "Igreja Irresistível",
    "autor": "Bill Hybels",
    },
]
    
#consultar livros
@app.route('/livros',methods=['GET'])
## esse app.route livros quer dizer que estou adicionando ao final 
# do meu  http://localhost:5000 --> ('/livros')

def Obter_livros():
    # está função 
    # converte o json 
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify (livro)

@app.route('/livros/<int:id>',methods = ['PUT'])
def editar_livro_alterado_id(id):
     livro_alterado = request.get_json()
     for indice,livro in enumerate(livros):
         if livro.get('id') == id:
             livros[indice].update(livro_alterado)
             return jsonify(livros[indice])
         
         
@app.route('/livros/',methods=['POST'])
def incluir():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def delete(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)