document.addEventListener("DOMContentLoaded", function () {
  const ekleBtn = document.getElementById("ekle");
  const hedefDiv = document.getElementById("ders-ekle");
  const maxLimit = 5;

  function updateDersIndices() {
    const dersDivs = hedefDiv.querySelectorAll(".eklenen-ders");
    dersDivs.forEach((div, index) => {
      const koduInput = div.querySelector('input[placeholder="0000000"]');
      const adiInput = div.querySelector('input[placeholder="Ders Adı"]');
      koduInput.name = `dersler[${index + 1}][kodu1]`;
      adiInput.name = `dersler[${index + 1}][adi1]`;
    });
  }

  ekleBtn.addEventListener("click", function () {
    const mevcutDersler = hedefDiv.querySelectorAll(".eklenen-ders");

    if (mevcutDersler.length >= maxLimit) {
      alert("Maksimum 5 ders eklenebilir!");
      return;
    }

    const index = mevcutDersler.length + 1;

    // Yeni div oluştur
    const yeniDersDiv = document.createElement("div");
    yeniDersDiv.className = "eklenen-ders flex border border-textColor rounded-lg mt-4 items-center h-10 bg-white";

    // İçeriğini belirle
    yeniDersDiv.innerHTML = `
      <div class="ders-kodu-input flex items-center border-r border-textColor h-full basis-[30%] px-2">
          <input type="text" name="dersler[${index}][kodu1]" placeholder="0000000" maxlength="7" class="w-full placeholder-textColor outline-0">
      </div>
      <div class="ders-adi-input flex items-center basis-[60%] px-2 h-full">
          <input type="text" name="dersler[${index}][adi1]" placeholder="Ders Adı" maxlength="40" class="w-full placeholder-textColor outline-0">
      </div>
      <button class="ders-cikar cursor-pointer p-2">
          <img src="assets/icon/Vector.png" alt="">
      </button>
    `;

    // Yeni div'i "ekle" butonundan önce ekle
    hedefDiv.insertBefore(yeniDersDiv, ekleBtn);

    // Çıkar butonunu tanımla
    const cikarBtn = yeniDersDiv.querySelector(".ders-cikar");
    cikarBtn.addEventListener("click", function () {
      yeniDersDiv.remove();
      updateDersIndices();
    });

    // Update indices after adding a new course
    updateDersIndices();
  });

  // Initial index update for existing courses
  updateDersIndices();
});

document.addEventListener("DOMContentLoaded", function () {
  const cakisanEkleBtn = document.getElementById("cakisan-ders-ekle");
  const cakisanContainer = document.querySelector(".ders-sil");
  const cakisanMax = 5;

  function updateCakisanDersIndices() {
    const dersDivs = cakisanContainer.querySelectorAll(".cakisan-ders");
    dersDivs.forEach((div, index) => {
      const koduInput = div.querySelector('input[placeholder="0000000"]');
      const adiInput = div.querySelector('input[placeholder="Ders Adı"]');
      const grupInput = div.querySelector('input[placeholder="Grup"]');
      koduInput.name = `dersler[${index + 1}][kodu2]`;
      adiInput.name = `dersler[${index + 1}][adi2]`;
      grupInput.name = `dersler[${index + 1}][grubu]`;
    });
  }

  cakisanEkleBtn.addEventListener("click", function () {
    const mevcutDersler = cakisanContainer.querySelectorAll(".cakisan-ders");

    if (mevcutDersler.length >= cakisanMax) {
      alert("Maksimum 5 çakışan ders eklenebilir!");
      return;
    }

    const index = mevcutDersler.length + 1;

    const yeniDers = document.createElement("div");
    yeniDers.className = "cakisan-ders flex w-full border border-textColor relative h-10 items-center bg-white mt-4 rounded-lg";

    yeniDers.innerHTML = `
      <div class="ders-kodu w-3/10 border-r border-textColor flex items-center h-full px-2">
          <input type="text" name="dersler[${index}][kodu2]" placeholder="0000000" class="w-full placeholder-textColor outline-0">
      </div>
      <div class="ders-adi w-3/5 px-2 h-full flex border-r border-textColor items-center">
          <input type="text" name="dersler[${index}][adi2]" placeholder="Ders Adı" class="w-full placeholder-textColor outline-0">
      </div>
      <div class="grup w-3/10 px-2 h-full flex items-center">
          <input type="text" name="dersler[${index}][grubu]" placeholder="Grup" maxlength="3" class="w-full placeholder-textColor outline-0">
      </div>
      <button class="cakisan-ders-cikar absolute right-2 p-2 cursor-pointer">
          <img src="assets/icon/Vector.png" alt="">
      </button>
    `;

    cakisanContainer.insertBefore(yeniDers, cakisanEkleBtn);

    const cikarBtn = yeniDers.querySelector(".cakisan-ders-cikar");
    cikarBtn.addEventListener("click", function () {
      yeniDers.remove();
      updateCakisanDersIndices();
    });

    // Update indices after adding a new course
    updateCakisanDersIndices();
  });

  // Initial index update for existing courses
  updateCakisanDersIndices();
});

function generatePDF() {
    document.getElementById("mainForm").submit();
}