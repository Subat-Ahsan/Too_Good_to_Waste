function selectStore(storeID) {
    fetch("/select-store", {
      method: "POST",
      body: JSON.stringify({ storeID: storeID }),
    }).then((_res) => {
      window.location.href = "/store-view";
    });
}