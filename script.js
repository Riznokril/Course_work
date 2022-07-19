const getAllData = async () => {
    fetch("http://127.0.0.1:5000", {
    headers: {
        "Content-Type": "application/json",
    },
    method: 'POST',
    body: JSON.stringify()
})
    .then(res => {return res.json()})
    .then(data => json.stringify(data)
    ).catch (error => {
        console.error("HTTP ERROR: ", error);});
};