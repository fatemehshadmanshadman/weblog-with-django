const titleInput=document.querySelector('input[name=title]')
const slugInput=document.querySelector('input[name=slug]')

const slugify =(val) =>{
    return val.toString().trim()
    .toLowerCase()
    .replace(/\s+/g, '-') // Replace spaces with -
    .replace(/[^a-z0-9-]/g, '--'); // Remove any character that is not a letter, number, or -
};

titleInput.addEventListener('keyup',(e)=>{
    slugInput.setAttribute('value',slugify(titleInput.value));
});