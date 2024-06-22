document.getElementById("loginForm").addEventListener("submit", function() {
    event.preventDefault();
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    
    if (username == "admin" && password == "admin123") {
    window.location.href = "../administrador/index_admin.html";
    } else {
    alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
    }
    });