const bar = document.getElementById('bar');

function resetProgress() {
    bar.style.transition = 'none'
    bar.style.width = '0%';
}

function startProgress(seconds) {
    bar.style.transition = `${seconds}s linear width`
    bar.style.width = '100%';
}
