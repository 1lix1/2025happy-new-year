document.getElementById('playButton').addEventListener('click', function () {
    const video = document.getElementById('backgroundVideo');
    const container = document.getElementById('container');

    // 播放视频
    video.play();
    video.muted = false; // 取消静音

    // 隐藏按钮和容器
    container.style.display = 'none';
});