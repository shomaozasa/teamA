// フォームの要素
let userName = document.getElementById('name');
let mail = document.getElementById('mail');
let systemName = document.getElementById('system-name');
let systemDetails = document.getElementById('system-details');
// ポップアップの要素
let popupUserName = document.getElementById('popup-name');
let popupMail = document.getElementById('popup-mail');
let popupSystemName = document.getElementById('popup-system-name');
let popupSystemDetails = document.getElementById('popup-system-details');
let popupMessage = document.getElementById('popup-message');
let popupSubmit = document.getElementById('popup-submit');

// ポップアップ表示時にフォームのデータをポップアップに表示
function showPopup() {
    let canSent = true;
    let message = 'この内容で送信してよろしいですか？';

    // バリデーションチェック
    if (
        userName.value === ''
        || mail.value === ''
        || systemName.value === ''
        || systemDetails.value === ''
    ) {
        canSent = false;
        message = '未入力の項目があります';
    } else if (!mail.value.match(/.+@.+\..+/)) {
        canSent = false;
        message = 'メールアドレスが不正です';
    }

    if (canSent) {
        popupSubmit.removeAttribute('disabled');
    } else {
        popupSubmit.setAttribute('disabled', 'true');
    }

    popupUserName.value = userName.value;
    popupMail.value = mail.value;
    popupSystemName.value = systemName.value;
    popupSystemDetails.value = systemDetails.value;
    popupMessage.textContent = message;
}

let sendBtn = document.getElementById('send-btn');
sendBtn.addEventListener('click', showPopup);