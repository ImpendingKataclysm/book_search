/* Toggle disabled status for all search inputs that don't correspond to the
* selected radio input */

const titleSelect = document.getElementById('search_title');
const authorSelect = document.getElementById('search_author');
const subjectSelect = document.getElementById('search_subject');

const titleSearch = document.getElementById('id_book_title');
const authorSearch = document.getElementById('id_author_name');
const subjectSearch = document.getElementById('id_subject_keyword');

function updateInputs() {
    titleSearch.disabled = !titleSelect.checked;
    authorSearch.disabled = !authorSelect.checked;
    subjectSearch.disabled = !subjectSelect.checked;
}

titleSelect.addEventListener('change', updateInputs);
authorSelect.addEventListener('change', updateInputs);
subjectSelect.addEventListener('change', updateInputs);

updateInputs();