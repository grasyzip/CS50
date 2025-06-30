document.addEventListener('DOMContentLoaded', function() {
    // Parte 1: Múltipla escolha
    const options = document.querySelectorAll('.option');
    const feedback1 = document.getElementById('feedback1');

    options.forEach(option => {
        option.addEventListener('click', function() {
            // Reset all options
            options.forEach(opt => {
                opt.classList.remove('correct', 'incorrect');
            });

            // Check if answer is correct
            if (this.textContent === 'Brasília') {
                this.classList.add('correct');
                feedback1.textContent = 'Correto!';
                feedback1.style.color = '#2ecc71';
            } else {
                this.classList.add('incorrect');
                feedback1.textContent = 'Incorreto';
                feedback1.style.color = '#e74c3c';
            }
        });
    });

    // Parte 2: Resposta livre
    const submit2 = document.getElementById('submit2');
    const answer2 = document.getElementById('answer2');
    const feedback2 = document.getElementById('feedback2');

    submit2.addEventListener('click', function() {
        // Remove previous classes
        answer2.classList.remove('correct', 'incorrect');

        // Check if answer is correct (case insensitive)
        if (answer2.value.trim().toLowerCase() === '8' ||
            answer2.value.trim().toLowerCase() === 'oito') {
            answer2.classList.add('correct');
            feedback2.textContent = 'Correto!';
            feedback2.style.color = '#2ecc71';
        } else {
            answer2.classList.add('incorrect');
            feedback2.textContent = 'Incorreto!';
            feedback2.style.color = '#e74c3c';
        }
    });

    // Allow pressing Enter to submit answer
    answer2.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            submit2.click();
        }
    });
});
