async function sendPostRequest(url, data){
    return await fetch(
        url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    )
    .then(response => response.json())
    .catch((error) => {console.error(error)})
}


sendPostRequest(
    'http://127.0.0.1:8000/auth/users/activation/',
    {
        uid: "NA",
        token: "bmnfni-5cb76c05a6c8ad5fa2ad7ddb60823566"
    }
)