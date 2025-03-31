const imageInput = document.getElementById('imageInput');
const previewImage = document.getElementById('previewImage');
const processingText = document.getElementById('processingText');
const resultText = document.getElementById('resultText');
const uploadForm = document.getElementById('uploadForm');

imageInput.addEventListener('change', () => {
    const file = imageInput.files[0];
    if (file) {
        previewImage.src = URL.createObjectURL(file);
        previewImage.style.opacity = '1';
        processingText.style.display = 'none';
        resultText.textContent = '';
    }
});

uploadForm.onsubmit = async (e) => {
    e.preventDefault();

    const file = imageInput.files[0];
    if (!file){
        alert("Nenhuma imagem selecionada")
        return;
    }

    previewImage.style.opacity = '0.75';
    processingText.style.display = 'block';
    resultText.textContent = '';

    const formData = new FormData();
    formData.append("image", file);

    try {
        const resposta = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (!resposta.ok) throw new Error('Falha no upload da imagem');

        const resultado = await resposta.json();

        previewImage.src = `data:image/png;base64,${resultado.image}`;
        resultText.textContent = `Número de eixos detectados: ${resultado.total_boxes}`;

    } catch (error) {
        alert('Erro no processamento da imagem');
        console.error(error);

    } finally {
        previewImage.style.opacity = '1';
        processingText.style.display = 'none';

    }
};
