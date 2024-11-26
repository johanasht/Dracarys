function submitFilterForm() {
    var form = document.getElementById('filterForm');
    form.addEventListener('submit', function() {
      form.reset();
    });
    form.submit();
  }

  async function showAddFoodModal() {
    document.querySelector("#modal").classList.remove("hidden");
  
    document.getElementById("confirm-modal").onclick = async function () {
        await addFood();
        closeModal();
    };
  }

  async function addFood() {
    const form = new FormData(document.querySelector("#form"));
    const response = await fetch("/foods/add_food/", {
      method: "POST",
      body: form,
    });
  
    if (!response.ok) {
      throw new Error("Failed to add food");
    }
    return false;
  }
