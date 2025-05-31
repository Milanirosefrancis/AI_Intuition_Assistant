body {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(to right, #fceabb, #f8b500);
    margin: 0;
    padding: 0;
}

.navbar {
    background-color: #333;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar a {
    color: #fceabb;
    text-decoration: none;
    font-weight: bold;
}

.container {
    max-width: 600px;
    margin: 2rem auto;
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
}

h2 {
    color: #333;
    margin-bottom: 1rem;
}

form input, form button {
    margin: 0.5rem 0;
    padding: 0.5rem;
    font-size: 1rem;
}

form button {
    background: #ff8800;
    border: none;
    color: white;
    cursor: pointer;
    border-radius: 5px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin: 0.5rem 0;
    padding: 0.5rem;
    background: #f0f0f0;
    border-left: 5px solid #ff8800;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

li.done {
    text-decoration: line-through;
    color: gray;
}

.flash {
    background: #ffdddd;
    color: red;
    padding: 10px;
    margin-bottom: 1rem;
}
