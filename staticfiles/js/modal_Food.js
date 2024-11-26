function submitFilterForm() {
    var form = document.getElementById('filterForm');
    form.addEventListener('submit', function() {
      form.reset();
    });
    form.submit();
  }
