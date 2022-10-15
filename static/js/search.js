function submitSearch() {
    query = document.getElementsByName('query').item(0).value.trim();
    if (query) {
        document.getElementById('search-bar').submit();
    }
}