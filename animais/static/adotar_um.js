
document.addEventListener('DOMContentLoaded', function () {

    // 1. Campo condicional: outros animais
    const checkboxAnimais = document.getElementById(
        'id_possui_outros_animais'
    );

    const campoQuaisAnimais = document.getElementById(
        'campo-quais-animais'
    );

    const campoQuaisAnimaisInput = document.getElementById(
        'id_quais_animais'
    );

    function atualizarCampoAnimais() {
        if (!checkboxAnimais || !campoQuaisAnimais) {
            return;
        }

        const possuiAnimais = checkboxAnimais.checked;

        campoQuaisAnimais.style.display = possuiAnimais ? 'flex' : 'none';

        if (campoQuaisAnimaisInput) {
            campoQuaisAnimaisInput.required = possuiAnimais;

            if (!possuiAnimais) {
                campoQuaisAnimaisInput.value = '';
            }
        }
    }

    if (checkboxAnimais && campoQuaisAnimais) {
        checkboxAnimais.addEventListener(
            'change',
            atualizarCampoAnimais
        );

        atualizarCampoAnimais();
    }


    // 2. Consulta de CEP com a API ViaCEP
    const campoCep = document.getElementById('id_cep');
    const campoEndereco = document.getElementById('id_endereco');
    const campoBairro = document.getElementById('id_bairro');
    const campoCidade = document.getElementById('id_cidade');
    const campoEstado = document.getElementById('id_estado');

    if (
        !campoCep ||
        !campoEndereco ||
        !campoBairro ||
        !campoCidade ||
        !campoEstado
    ) {
        return;
    }

    campoCep.addEventListener('blur', async function () {
        const cep = campoCep.value.replace(/\D/g, '');

        if (cep.length === 0) {
            return;
        }

        if (cep.length !== 8) {
            alert('Digite um CEP válido com 8 números.');
            return;
        }

        try {
            campoCep.disabled = true;

            const resposta = await fetch(
                `https://viacep.com.br/ws/${cep}/json/`
            );

            if (!resposta.ok) {
                throw new Error('Falha na consulta do CEP.');
            }

            const dados = await resposta.json();

            if (dados.erro) {
                alert('CEP não encontrado. Confira o número e tente novamente.');
                return;
            }

            campoEndereco.value = dados.logradouro || '';
            campoBairro.value = dados.bairro || '';
            campoCidade.value = dados.localidade || '';
            campoEstado.value = dados.uf || '';

        } catch (erro) {
            alert(
                'Não foi possível consultar o CEP. ' +
                'Você pode preencher o endereço manualmente.'
            );
        } finally {
            campoCep.disabled = false;
        }
    });

});
