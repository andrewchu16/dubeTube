function updatePreview(e){
    var image = document.getElementById('thumbnail-preview');
    var get_file = document.getElementById('thumbnail-upload');

    
    const [file] = get_file.files;
    console.log(file);
    if (file) {
        image.src = URL.createObjectURL(file)
    }
}