function submitSearch(e) {
    e.preventDefault();
    let query = document.getElementsByName('query').item(0).value.trim();

    if (query.length > 5) {
        query = query.substring(0, 5);
        document.getElementsByName('query').item(0).value = query.substring(0, 5);
    }
    
    if (query) {
        document.getElementById('search-bar').submit();
    }
}