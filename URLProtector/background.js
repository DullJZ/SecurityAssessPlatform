setInterval(() => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        const url = tabs[0].url;
        fetch('http://localhost:5000/post', {
            method: 'POST',
            body: JSON.stringify({url}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                alert('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.status == 'hack') {
                alert('You are hacker!');
                chrome.tabs.update({url: 'https://www.google.com/'});
            }
        })
        .catch(error => {
            alert('Error:', error);
        });
    });
}, 5000);
