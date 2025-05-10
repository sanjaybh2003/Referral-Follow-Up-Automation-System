function updateStatus(referralId, newStatus) {
    if (!confirm(`Are you sure you want to mark this referral as ${newStatus}?`)) {
        return;
    }

    fetch(`/referrals/${referralId}/status`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            location.reload();
        } else {
            alert('Error updating status: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error updating status. Please try again.');
    });
} 