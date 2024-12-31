document.getElementById('playButton').addEventListener('click', function () {
    const video = document.getElementById('backgroundVideo');
    const container = document.getElementById('container');

    // 播放视频并取消静音
    video.play().then(() => {
        video.muted = false;
    }).catch(error => {
        console.error("视频播放失败:", error);
        alert("视频播放失败，请检查控制台日志。");
    });

    // 隐藏容器
    container.classList.add('hidden');
});
