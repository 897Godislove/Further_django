const titleInput = document.getElementById("id_title");
const slugInput = document.getElementById("id_slug");

const slugify = (val) => {
  return val.toString().toLowerCase().trim()
  .replace(/&/g, '-and-')
  .replace(/[\s\W-]+/g, '-')
};

titleInput.addEventListener('keyup', (e) => {
  slugInput.setAttribute('value', slugify(titleInput.value));
});