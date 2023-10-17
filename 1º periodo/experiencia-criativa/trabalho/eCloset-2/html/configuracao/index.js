var verificarSenha = document.getElementById("password_button")
verificarSenha.onclick = function(){ 
    alert("Senha alterada com sucesso")
}

const imgDiv = document.querySelector('.profile');
const img = document.querySelector('#foto');
const file = document.querySelector('#file');
const uploadBtn = document.querySelector('#upload-btn');

file.addEventListener('change', function(){
    const choosedFile = this.files[0];
    if(choosedFile) {
        const reader = new FileReader(); 
        reader.addEventListener('load', function(){
            img.setAttribute('src', reader.result)
        });
        reader.readAsDataURL(choosedFile)
    }
})