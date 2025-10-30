// 質問データ
const questions = [
    { question: "カフェでまったりしたい？", yesType: "healing", noType: "power" },
    { question: "スタミナ満点のご飯で元気出したい？", yesType: "volume", noType: "healing" },
    { question: "スイーツで幸せチャージしたい？", yesType: "sweet", noType: "volume" },
    { question: "静かな空間で落ち着きたい？", yesType: "healing", noType: "volume" },
    { question: "お肉でテンション上げたい？", yesType: "niku", noType: "power" },
    { question: "ピリッと辛さでリフレッシュしたい？", yesType: "spicy", noType: "sweet" },
    { question: "さっぱりしたものが食べたい？", yesType: "sappari", noType: "volume" }
];

// タイプ対応ジャンル
const typeToCategory = {
    healing: "カフェ",
    power: "中華",
    volume: "ラーメン",
    niku: "焼肉",
    sweet: "スイーツ",
    spicy: "激辛",
    sappari: "うどん・そば"
};

// Google検索用クエリ
const typeToGoogleQuery = {
    healing: "カフェ",
    power: "中華",
    volume: "ラーメン",
    niku: "焼肉",
    sweet: "スイーツ",
    spicy: "激辛",
    sappari: "うどん・そば"
};

let step = 0;
let answers = [];
let selectedArea = "現在地";

document.addEventListener("DOMContentLoaded", () => {
    const quizContainer = document.getElementById("quiz-container");
    const resultContainer = document.getElementById("result-container");
    const areaSelect = document.getElementById("area-select");
    const areaDropdown = document.getElementById("area");
    const startButton = document.getElementById("start-button");
    const resetButton = document.getElementById("reset-button");

    startButton.onclick = () => {
        selectedArea = areaDropdown.value;
        areaSelect.style.display = "none";
        quizContainer.style.display = "block";
        step = 0;
        answers = [];
        showQuestion();
    };

    resetButton.onclick = resetApp;

    function showQuestion() {
        const q = questions[step];
        quizContainer.innerHTML = `<h2>${q.question}</h2>`;

        const yesBtn = document.createElement("button");
        yesBtn.innerText = "はい";
        yesBtn.onclick = () => {
            answers.push(q.yesType);
            nextStep();
        };

        const noBtn = document.createElement("button");
        noBtn.innerText = "いいえ";
        noBtn.onclick = () => {
            answers.push(q.noType);
            nextStep();
        };

        quizContainer.appendChild(yesBtn);
        quizContainer.appendChild(noBtn);

        // ✅ 戻るボタンを常に表示（1問目でも）
        const backBtn = document.createElement("button");
        backBtn.innerText = "← 戻る";
        backBtn.className = "back-btn";
        backBtn.onclick = () => {
            if (step === 0) {
                // 1問目で押されたらホーム画面に戻る
                quizContainer.style.display = "none";
                areaSelect.style.display = "block";
                answers = [];
                step = 0;
            } else {
                answers.pop();
                step--;
                showQuestion();
            }
        };
        quizContainer.appendChild(backBtn);
    }

    function nextStep() {
        step++;
        if (step < questions.length) {
            showQuestion();
        } else {
            showResult();
        }
    }

    function showResult() {
        quizContainer.style.display = "none";
        resultContainer.style.display = "block";

        const counts = {};
        answers.forEach((t) => {
            counts[t] = (counts[t] || 0) + 1;
        });

        let resultType = Object.keys(counts).reduce((a, b) =>
            counts[a] > counts[b] ? a : b
        );

        if (answers.includes("niku")) {
            resultType = "niku";
        }

        document.getElementById("result-title").innerText = `あなたは「${typeToCategory[resultType]}タイプ」！`;
        document.getElementById("result-text").innerText = `おすすめジャンルは「${typeToCategory[resultType]}」です`;

        const query =
            selectedArea === "現在地"
                ? `${typeToGoogleQuery[resultType]}`
                : `${selectedArea} ${typeToGoogleQuery[resultType]}`;
        const mapUrl = `https://www.google.com/maps/search/${encodeURIComponent(query)}/`;

        const mapLink = document.getElementById("map-link");
        mapLink.href = mapUrl;
        mapLink.innerText = `${selectedArea}で${typeToCategory[resultType]}を探す`;
    }

    function resetApp() {
        resultContainer.style.display = "none";
        areaSelect.style.display = "block";
        quizContainer.style.display = "none";
        step = 0;
        answers = [];
        document.getElementById("result-title").innerText = "";
        document.getElementById("result-text").innerText = "";
        document.getElementById("map-link").href = "#";
        document.getElementById("map-link").innerText = "";
    }
});
