//alert('ok');
$("#cep").mask("00000-000");
$("#datanasc").mask("00/00/0000");
document.getElementById("cep").addEventListener("blur", function() {
    var valor = this.value;
    var url = "https://viacep.com.br/ws/" + valor + "/json/";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById("cidade").value = data.localidade;
            document.getElementById("estado").value = data.uf;
            document.getElementById("bairro").value = data.bairro;
            document.getElementById("rua").value = data.logradouro;
            document.getElementById("numero").focus();
        })
        .catch(error => console.error("Erro na requisição:", error));
});

