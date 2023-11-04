// Empty non-selected form fields.

const titleSelect = document.getElementById('titleSelect');
const authorSelect = document.getElementById('authorSelect');
const subjectSelect = document.getElementById('subjectSelect');

const titleSearch = document.getElementById('id_book_title');
const authorSearch = document.getElementById('id_author_name');
const subjectSearch = document.getElementById('id_subject_keyword');

titleSelect.addEventListener('click', (e) => {
    authorSearch.value = '';
    subjectSearch.value = '';
});

authorSelect.addEventListener('click', (e) => {
    titleSearch.value = '';
    subjectSearch.value = '';
});

subjectSelect.addEventListener('click', (e) => {
    titleSearch.value = '';
    authorSearch.value = '';
})
