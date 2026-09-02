document.addEventListener('DOMContentLoaded', function () {

    const checkbox = document.getElementById('id_possui_problema_saude');
    const campoProblema = document.getElementById('campo-problema-saude');

    function atualizarCampoProblema() {

        if (checkbox.checked) {
            campoProblema.style.display = 'block';
        } else {
            campoProblema.style.display = 'none';
        }

    }

    checkbox.addEventListener('change', atualizarCampoProblema);

    atualizarCampoProblema();

});

document.addEventListener('DOMContentLoaded', function () {
    const campoCep = document.getElementById('id_cep');
    const campoEndereco = document.getElementById('id_endereco');
    const campoBairro = document.getElementById('id_bairro');
    const campoCidade = document.getElementById('id_cidade');
    const campoEstado = document.getElementById('id_estado');

    if (campoCep) {
        // Escuta quando o usuário sai do campo de CEP
        campoCep.addEventListener('blur', function () {
            // Remove traços ou pontos digitados, mantendo apenas números
            const cep = campoCep.value.replace(/\D/g, '');

            // Valida se o CEP tem exatamente 8 dígitos
            if (cep.length === 8) {
                // Feedback visual indicando o carregamento
                campoEndereco.value = 'Buscando...';
                campoBairro.value = 'Buscando...';
                campoCidade.value = 'Buscando...';
                campoEstado.value = '...';

                // Requisição para a API do ViaCEP
                fetch(`https://viacep.com.br/ws/${cep}/json/`)
                    .then(response => response.json())
                    .then(dados => {
                        if (!dados.erro) {
                            // Preenche os campos com os dados retornados
                            campoEndereco.value = dados.logradouro;
                            campoBairro.value = dados.bairro;
                            campoCidade.value = dados.localidade;
                            campoEstado.value = dados.uf;
                        } else {
                            alert('CEP não encontrado. Por favor, verifique o número.');
                            limparCamposEndereco();
                        }
                    })
                    .catch(() => {
                        alert('Erro ao buscar o CEP. Preencha os campos manualmente.');
                        limparCamposEndereco();
                    });
            }
        });
    }

    function limparCamposEndereco() {
        campoEndereco.value = '';
        campoBairro.value = '';
        campoCidade.value = '';
        campoEstado.value = '';
    }
});