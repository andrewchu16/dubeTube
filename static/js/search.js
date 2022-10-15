function submitSearch() {
    let query = document.getElementsByName('query').item(0).value.trim();

    if (query.length > 5) {
        query = query.substring(0, 5);
    }
    
    if (query) {
        document.getElementById('search-bar').submit();
    }
}