const crypto = require("crypto");

const encrypt = (data, publicKey) => {
    const buffer = Buffer.from(data);
    const encrypted = crypto.publicEncrypt(publicKey, buffer);
    return encrypted.toString("base64");
}

const decrypt = (data, privateKey) => {
    const buffer = Buffer.from(data, "base64");
    const decrypted = crypto.privateDecrypt(privateKey, buffer);
    return decrypted.toString("utf8");
}

const { publicKey, privateKey } = crypto.generateKeyPairSync("rsa", {
    modulusLength: 2048,
});

const data = "Hello World";
const encryptedData = encrypt(data, publicKey);
const decryptedData = decrypt(encryptedData, privateKey);

console.log("Original Data:", data);
console.log("Encrypted Data:", encryptedData);
console.log("Decrypted Data:", decryptedData);