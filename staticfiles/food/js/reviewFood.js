const reviewButton = document.getElementById('reviewButton');
reviewButton.addEventListener('click', function() {
    var content_type_id = reviewButton.dataset.contentTypeId;
    var object_id = reviewButton.dataset.objectId;
    console.log('content_type_id:', content_type_id);
    console.log('object_id:', object_id);
    var review_url = `/reviews/${content_type_id}/${object_id}/review_fnd/`;
    window.location.href = review_url;
});