
function toggleAnswer(button) {
    const answer = button.nextElementSibling;
    if (answer.style.display === 'block') {
        answer.style.display = 'none';
    } else {
        answer.style.display = 'block';
    }
}

function openModal(imgElement) {
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modalImg');
    const caption = document.getElementById('caption');

    modal.style.display = 'block';
    modalImg.src = imgElement.src;
    caption.innerText = imgElement.alt;
}


function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
}


document.addEventListener('DOMContentLoaded', () => {
    const closeBtn = document.querySelector('.close');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }

    const modal = document.getElementById('modal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal();
            }
        });
    }
});
