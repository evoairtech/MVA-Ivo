document.addEventListener('DOMContentLoaded', function () {
    // Get all dropdown containers
    const dropdownContainers = document.querySelectorAll('.dropdown-container');

    // Loop through each dropdown container
    dropdownContainers.forEach(function (container) {
        // Get the dropdown button inside the container
        const button = container.querySelector('.dropdown-button');

        // Add click event to toggle the dropdown visibility
        button.addEventListener('click', function () {
            // Toggle the 'open' class to show/hide the dropdown menu
            container.classList.toggle('open');
        });
    });
});
