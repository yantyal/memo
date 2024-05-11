// クリックしたコマンドテキストをコピーする関数
function copyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.textContent = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    textArea.remove();
}

// すべての<code>タグにイベントリスナーを追加
document.querySelectorAll('.click-to-copy').forEach(element => {
    element.addEventListener('click', function() {
        copyToClipboard(this.textContent);
    });
});

function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.className = "show";
    setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 3000);
}

document.querySelectorAll('.click-to-copy').forEach(element => {
    element.addEventListener('click', function() {
        copyToClipboard(this.textContent);
        showToast('コピーしました: ' + this.textContent);
    });
});
