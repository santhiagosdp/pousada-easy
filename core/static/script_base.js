    $(document).ready(function() {
        // Função para ordenar a tabela ao clicar em uma coluna
        $('.ordenavel').click(function() {
            var coluna = $(this);
            var ordem = coluna.hasClass('asc') ? 'desc' : 'asc';
            var indice = coluna.index();
            var linhas = $('#tabela-produtos tbody tr').toArray();

            // Ordena as linhas da tabela de acordo com a coluna clicada e a ordem selecionada
            linhas.sort(function(a, b) {
                var valorA = $(a).children('td').eq(indice).text();
                var valorB = $(b).children('td').eq(indice).text();
                if (ordem == 'asc') {
                    return valorA.localeCompare(valorB, undefined, { sensitivity: 'base' });
                } else {
                    return valorB.localeCompare(valorA, undefined, { sensitivity: 'base' });
                }
            });

            // Atualiza a tabela com as linhas ordenadas
            $('#tabela-produtos tbody').empty().append(linhas);

            // Adiciona a classe "asc" ou "desc" à coluna clicada para indicar a ordem atual
            $('#tabela-produtos th').removeClass('asc desc');
            coluna.addClass(ordem);
        });
    });