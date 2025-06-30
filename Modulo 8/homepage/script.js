document.addEventListener('DOMContentLoaded', function() {
    // Botões de mostrar detalhes dos projetos
    const toggleButtons = document.querySelectorAll('.toggle-details');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const details = document.getElementById(targetId);

            if (details.style.display === 'none') {
                details.style.display = 'block';
                this.textContent = 'Ocultar Detalhes';
            } else {
                details.style.display = 'none';
                this.textContent = 'Mostrar Detalhes';
            }
        });
    });

    // Formulário de contato
    const contactForm = document.getElementById('contactForm');
    const formSuccess = document.getElementById('formSuccess');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Simular envio do formulário
            setTimeout(() => {
                contactForm.reset();
                formSuccess.style.display = 'block';

                // Ocultar mensagem de sucesso após 5 segundos
                setTimeout(() => {
                    formSuccess.style.display = 'none';
                }, 5000);
            }, 1000);
        });
    }

    // Efeito de digitação no título da página inicial
    const typedText = document.querySelector('.jumbotron h1');
    if (typedText && window.location.pathname.endsWith('index.html')) {
        const originalText = typedText.textContent;
        typedText.textContent = '';

        let i = 0;
        const typingEffect = setInterval(() => {
            if (i < originalText.length) {
                typedText.textContent += originalText.charAt(i);
                i++;
            } else {
                clearInterval(typingEffect);
            }
        }, 100);
    }

    // Ativar tooltips do Bootstrap
    $('[data-toggle="tooltip"]').tooltip();

    // Alertar quando o usuário sai da página
    window.addEventListener('beforeunload', function(e) {
        // Comente a linha abaixo se não quiser o alerta
        // e.returnValue = 'Tem certeza que deseja sair?';
    });
});
