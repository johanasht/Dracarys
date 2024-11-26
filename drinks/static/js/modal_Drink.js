function submitFilterForm() {
    var form = document.getElementById('filterForm');
    form.addEventListener('submit', function() {
      form.reset();
    });
    form.submit();
  }

  async function showAddDrinkModal() {
    document.querySelector("#modal").classList.remove("hidden");
  
    document.getElementById("confirm-modal").onclick = async function () {
        await addDrink();
        closeModal();
    };
  }

  async function addDrink() {
    const form = new FormData(document.querySelector("#form"));
    const response = await fetch("/foods/add_drink/", {
      method: "POST",
      body: form,
    });
  
    if (!response.ok) {
      throw new Error("Failed to add drink");
    }
    return false;
  }
