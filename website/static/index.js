function selectStore(storeID) {
    fetch("/select-store", {
      method: "POST",
      body: JSON.stringify({ storeID: storeID }),
    }).then((_res) => {

    });
}

function pickup(storeID) {
    fetch("/pickup", {
      method: "POST",
      body: JSON.stringify({ storeID: storeID }),
    }).then((_res) => {
        
    });
}

function dropoff(storeID) {
    fetch("/dropoff", {
      method: "POST",
      body: JSON.stringify({ storeID: storeID }),
    }).then((_res) => {
        
    });
}

function deleteItem(itemID, inventory) {
    fetch("/delete-item", {
      method: "POST",
      body: JSON.stringify({ itemID: itemID , inventory: inventory}),
    }).then((_res) => {
        window.location.reload();
    });
}