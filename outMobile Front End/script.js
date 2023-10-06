// Sample data for most visited restaurants and top food items
const restaurantsData = [
    { name: "Restaurant 1", visits: 150 },
    { name: "Restaurant 2", visits: 120 },
    // Add more restaurant data here
];

const foodItemsData = [
    { name: "Food Item 1", count: 300 },
    { name: "Food Item 2", count: 250 },
    // Add more food item data here
];

// Function to populate the restaurant list
function populateRestaurantList() {
    const restaurantList = document.getElementById("restaurant-list");
    restaurantList.innerHTML = "";

    restaurantsData.forEach((restaurant) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${restaurant.name}: ${restaurant.visits} visits`;
        restaurantList.appendChild(listItem);
    });
}

// Function to populate the food item list
function populateFoodItemList() {
    const foodItemList = document.getElementById("food-item-list");
    foodItemList.innerHTML = "";

    foodItemsData.forEach((foodItem) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${foodItem.name}: ${foodItem.count} orders`;
        foodItemList.appendChild(listItem);
    });
}

// Call the functions to populate the lists when the page loads
window.addEventListener("load", () => {
    populateRestaurantList();
    populateFoodItemList();
});
