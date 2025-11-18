const API = "http://127.0.0.1:8000";

const exprEl = document.getElementById("expr");
const modeLabel = document.getElementById("modeLabel");

const algebraPanel = document.getElementById("panel-algebra");
const vectorPanel = document.getElementById("panel-vetores");
const matrixPanel = document.getElementById("panel-matrizes");
const relationPanel = document.getElementById("panel-relacoes");

const tabs = document.querySelectorAll(".tab");
let currentTab = "algebra";

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.remove("active"));
    tab.classList.add("active");

    currentTab = tab.dataset.tab;
    showPanel(currentTab);
  });
});

function showPanel(name) {
  algebraPanel.style.display = "none";
  vectorPanel.style.display = "none";
  matrixPanel.style.display = "none";
  relationPanel.style.display = "none";

  const panel = document.getElementById(`panel-${name}`);
  if (panel) panel.style.display = "block";

  const labelMap = {
    algebra: "Modo: Álgebra — Simplificar",
    vetores: "Modo: Vetores",
    matrizes: "Modo: Matrizes",
    relacoes: "Modo: Relações",
  };
  modeLabel.textContent = labelMap[name] ?? "CAS Calculator";
}

function press(key) {
  if (!exprEl) return;
  if (exprEl.textContent === "0") exprEl.textContent = "";
  exprEl.textContent += key;
}

function allClear() {
  exprEl.textContent = "0";
  document.getElementById("algebraResult").textContent =
    "Resultado aparecerá aqui";
}

function backspace() {
  if (!exprEl) return;
  exprEl.textContent = exprEl.textContent.slice(0, -1) || "0";
}

function updateMode() {
  const op = document.getElementById("algebraOp").value;
  const map = {
    simplify: "Simplificar",
    diff: "Derivar",
    integrate: "Integrar",
    factor: "Fatorar",
    solve: "Resolver Equação",
  };
  modeLabel.textContent = `Modo: Álgebra — ${map[op] || op}`;
}

async function callAPI(path, payload) {
  try {
    const res = await fetch(`${API}/${path}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const text = await res.text().catch(() => "");
      throw new Error(
        `HTTP ${res.status} ${res.statusText} ${text ? "- " + text : ""}`
      );
    }

    const contentType = res.headers.get("content-type") || "";
    if (contentType.includes("application/json")) {
      const data = await res.json();
      if (data && typeof data === "object" && "result" in data)
        return data.result;
      return data;
    } else {
      const txt = await res.text();
      return txt;
    }
  } catch (err) {
    return { __error: err.message || String(err) };
  }
}

async function sendAlgebra() {
  const op = document.getElementById("algebraOp").value;
  const expr = exprEl && exprEl.textContent ? exprEl.textContent : "0";
  const box = document.getElementById("algebraResult");
  box.textContent = "Processando...";

  const payload = op === "solve" ? { equation: expr } : { expr };

  const result = await callAPI(`algebra/${op}`, payload);

  if (result && result.__error) {
    box.textContent = "Erro: " + result.__error;
    return;
  }

  box.textContent = simpleFormat(result);
}

async function sendVectors() {
  const box = document.getElementById("vectorResult");
  box.textContent = "Processando...";

  let v1s = document.getElementById("vecA").value.trim();
  let v2s = document.getElementById("vecB").value.trim();

  if (!v1s || !v2s) {
    box.textContent = "Preencha ambos os vetores (formato JSON, ex: [1,2,3]).";
    return;
  }

  try {
    const v1 = JSON.parse(v1s);
    const v2 = JSON.parse(v2s);
    const op = document.getElementById("vectorOp").value;

    const result = await callAPI(`vector/${op}`, { v1, v2 });

    if (result && result.__error)
      return (box.textContent = "Erro: " + result.__error);

    box.textContent = simpleFormat(result);
  } catch {
    box.textContent = "Formato inválido: use JSON, ex: [1,2,3]";
  }
}

async function sendMatrices() {
  const box = document.getElementById("matrixResult");
  box.textContent = "Processando...";

  const aText = document.getElementById("matA").value.trim();
  const bText = document.getElementById("matB").value.trim();
  const op = document.getElementById("matrixOp").value;

  if (!aText) {
    box.textContent = "Preencha a Matriz A (ex: [[1,2],[3,4]]).";
    return;
  }

  try {
    const A = JSON.parse(aText);
    let B = null;
    if (bText) {
      B = JSON.parse(bText);
    }

    let payload;
    if (op === "det") payload = { A };
    else if (op === "solve") payload = { A, b: B };
    else payload = { A, B };

    const result = await callAPI(`matrix/${op}`, payload);

    if (result && result.__error)
      return (box.textContent = "Erro: " + result.__error);

    box.textContent = simpleFormat(result);
  } catch (e) {
    box.textContent =
      "Formato inválido — use JSON para matrizes, ex: [[1,2],[3,4]]";
  }
}

async function sendRelations() {
  const box = document.getElementById("relationResult");
  box.textContent = "Processando...";

  const aText = document.getElementById("setA").value.trim();
  const bText = document.getElementById("setB").value.trim();

  if (!aText || !bText) {
    box.textContent = "Preencha ambos os conjuntos A e B.";
    return;
  }

  try {
    const A = JSON.parse(aText);
    const B = JSON.parse(bText);

    const result = await callAPI("relations/cartesian", { A, B });

    if (result && result.__error)
      return (box.textContent = "Erro: " + result.__error);

    box.textContent = simpleFormat(result);
  } catch {
    box.textContent = 'Formato inválido — use JSON: ["a","b"] ou [1,2]';
  }
}

function clearRelations() {
  document.getElementById("setA").value = "";
  document.getElementById("setB").value = "";
  document.getElementById("relationResult").innerText =
    "Resultado aparecerá aqui";
}

function simpleFormat(v) {
  if (v === null || v === undefined) return "null";
  if (typeof v === "string" || typeof v === "number" || typeof v === "boolean")
    return String(v);
  try {
    return JSON.stringify(v, null, 2);
  } catch {
    return String(v);
  }
}

showPanel(currentTab);
updateMode();
