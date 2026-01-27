// Button click handler
document.addEventListener('DOMContentLoaded', function() {
    const btnClick = document.getElementById('btn-click');
    
    if (btnClick) {
        btnClick.addEventListener('click', function() {
            alert('Button clicked! Welcome to DS Toolbox WK08');
            console.log('Button was clicked at:', new Date().toLocaleString());
        });
    }

    // Log initialization
    console.log('DS Toolbox WK08 - Page Loaded');
    console.log('Ready for development!');
});

// Add more interactivity here
window.addEventListener('resize', function() {
    console.log('Window resized to:', window.innerWidth, 'x', window.innerHeight);
});
