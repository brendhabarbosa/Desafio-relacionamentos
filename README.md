# models.CASCADE - Justificativa de escolha:
Quando alguém tentar apagar um autor que tem livros, os livros precisam ser apagados também. Essa associação faz sentido porque os livros obrigatoriamente precisam de um autor.

## 1. Que dados se perdem quando a migração é revertida? Por quê?
Nenhum dado é perdido por causa da reverse_copy_atores.

## 2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?
O livro permanece, mas o campo atores fica vazio. Pode ser feito um signal pre-commit que valide isso.

## O que acontece quando a proteção é removida do template?

O Django impede o envio do formulário, retornando um 403 (Forbidden), "CSRF verification failed. Request aborted."

## Perguntas 1.2

a - Isso aconteceu porque o formulário é criado a partir do Model e o Django Admin também utiiza esse formulário.

b - O validator é uma função reutilizável que somente valida o campo, enquanto o clean_campo permite, além de validar, modificar/limpar o valor do campo.

c - O título não pode ser igual ao nome do autor: Como faz comparação entre dois campos, o ideal é usar clean(), que contempla validações envolvendo mais de uma campo.

c - O título deve ser salvo sem espaços no início e no fim - Como é preciso modificar um campo específicio, é melhor o clean_campo, que serve justamente para isso.

c - O número de páginas deve ser no máximo 5000 - Deve ser usado validators=[...]. A função pronta MaxValueValidator() com 5000 como argumento, estabelece 5000 como valor máximo.

c - Um livro "indisponível" precisa ter o ISBN preenchido - O clean() é a melhor estratégia porque a validação envolve dois campos: isbn e disponível.

## Perguntas 2.2

a - O formulário não dá nenhum aviso em nenhum dos casos. O formulário é enviado normalmente, mas a imagem não é recebida. No caso da view, ela apenas não recebe o upload e como a imagem é opcional, não dá erro. No caso de não ter o enctype, o Django não recebe a imagem mesmo com o request.FILES na view. Os dois são necessários para o envio correto e completo dos dados.

b - STATIC é para arquivos que fazem parte do projeto; MEDIA é para arquivos enviados pelos usuários. Na Mini biblioteca, o STATIC seria para arquivos já existentes no projeto, como uma logo do site, por exemplo. Já o MEDIA e o url, seriam para arquivos enviados pelos usuários, como é o caso da imagem da capa dos livros cadastrados.

c - Isso acontece porque o arquivo é excluído do banco, mas não da pasta que o guarda. A longo prazo, o acúmulo de arquivos não mais utilizados pode deixar o armazenamento cheio.

d - Alguém pode renomear a parte de extensão do arquivo para burlá-lo. Assim, o conteúdo do arquivo não vai ser válido. Por isso, é importante validar não só a extensão, mas também o conteúdo do arquivo. O servidor também deve limitar o tamanho, restringir formatos, gerar nomes seguros e armazenar os arquivos de maneira protegida.

## Perguntas 3.1

a - A própria CreateView faz esse controle automaticamente que antes era feito manualmente no modelo FBV.

b - A própria CreateView também faz isso internamente, recebendo automaticamente os arquivos enviados.

c - A DeleteView utiliza GET e POST. GET pega a página e POST realmente realiza a exclusão. Então, se a exclusão acontecesse no GET, bastaria acessar um link para apagar um registro sem confirmação.

d - As CBVs permitem reutilizar comportamentos prontos do Django, diminuindo linhas de código. A desvantagem é que podem ser mais difíceis de personalizar. Então, quando a lógica for pequena e mais personalizada, FBV pode ser a melhor opção.