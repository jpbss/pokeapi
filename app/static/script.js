document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('searchInput');
    const box = document.getElementById('suggestionsBox');

    let currentFocus = -1;

    if (typeof todosPokemons === 'undefined') {
        console.error('Lista de Pokémons não carregada.');
        return;
    }

    input.addEventListener('input', function() {
        const texto = this.value.toLowerCase();
        box.innerHTML = '';
        currentFocus = -1; // Reseta a seleção

        if (!texto) {
            box.style.display = 'none';
            return;
        }

        const encontrados = todosPokemons.filter(p => p.name.startsWith(texto)).slice(0, 5);

        if (encontrados.length > 0) {
            box.style.display = 'block';

            encontrados.forEach(p => {
                const div = document.createElement('div');
                div.className = 'suggestion-item';

                const imgUrl = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${p.id}.png`;

                div.innerHTML = `
                    <img src="${imgUrl}" alt="">
                    <span>${p.name}</span>
                    <input type='hidden' value='${p.name}'>
                `;

                div.addEventListener('click', function() {
                    input.value = p.name;
                    box.style.display = 'none';
                });

                box.appendChild(div);
            });
        } else {
            box.style.display = 'none';
        }
    });

    input.addEventListener('keydown', function(e) {
        let items = box.getElementsByClassName('suggestion-item');

        if (e.key === 'ArrowDown') {
            currentFocus++;
            addActive(items);
        } else if (e.key === 'ArrowUp') {
            currentFocus--;
            addActive(items);
        } else if (e.key === 'Enter') {
            if (currentFocus > -1 && items.length > 0) {
                e.preventDefault();
                items[currentFocus].click();
            }
        }
    });

    function addActive(items) {
        if (!items) return false;

        removeActive(items);

        if (currentFocus >= items.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (items.length - 1);

        items[currentFocus].classList.add('suggestion-active');

        items[currentFocus].scrollIntoView({ block: 'nearest' });
    }

    function removeActive(items) {
        for (let i = 0; i < items.length; i++) {
            items[i].classList.remove('suggestion-active');
        }
    }

    document.addEventListener('click', function(e) {
        if (e.target !== input && e.target !== box) {
            box.style.display = 'none';
        }
    });
});