document.getElementById('playButton').addEventListener('click', function () {
    const video = document.getElementById('backgroundVideo');
    const container = document.getElementById('container');

    video.play().then(() => {
        video.muted = false;
    }).catch(error => {
        console.error("视频播放失败:", error);
        alert("视频播放失败，请检查控制台日志。");
    });

    container.classList.add('hidden');
});
