import Link from "next/link";

import { getColabUrl, getFoundations } from "@/lib/course";

export function generateStaticParams() {
  return [{ lang: "zh" }, { lang: "en" }];
}

function notebookPath(id: string, slug: string, language: "zh" | "en") {
  return `notebooks/foundations/${language}/${id.toLowerCase()}_${slug.replaceAll("-", "_")}.ipynb`;
}

function docPath(id: string, slug: string, language: "zh" | "en") {
  return `docs/${language}/foundations/${id.toLowerCase()}-${slug}.md`;
}

function githubBlob(relativePath: string) {
  return `https://github.com/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/${relativePath}`;
}

export default async function FoundationsPage({
  params,
}: {
  params: Promise<{ lang: "zh" | "en" }>;
}) {
  const { lang } = await params;
  const foundations = getFoundations();

  return (
    <main className="content-grid">
      <section className="hero module-hero">
        <p className="eyebrow">{lang === "zh" ? "Pre-P4 基础包" : "Pre-P4 foundation pack"}</p>
        <h1>{lang === "zh" ? "先补齐真正会卡住小白的四块地基" : "Repair the four foundation gaps that block true beginners"}</h1>
        <p className="hero-copy">
          {lang === "zh"
            ? "这不是又一条论文线，而是一组专门解决环境、attention 形状感、向量几何和实验纪律的短 lab。做完它们，再进入文章主线和研究训练营。"
            : "This is not another paper path. It is a short lab pack that repairs environment setup, attention-shape intuition, vector geometry, and experiment discipline before the article core and research-ready track."}
        </p>
      </section>

      <section className="panel module-grid">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "基础 Lab" : "Foundation labs"}</p>
            <h3>{lang === "zh" ? "每一项都对应一个 notebook 和一组验收题" : "Each item comes with one notebook and a self-check set"}</h3>
          </div>
        </div>
        <div className="cards">
          {foundations.map((foundation) => {
            const notebook = notebookPath(foundation.id, foundation.web_slug, lang);
            const doc = docPath(foundation.id, foundation.web_slug, lang);
            const skills = lang === "zh" ? foundation.skills_zh : foundation.skills_en;
            const deliverables = lang === "zh" ? foundation.deliverables_zh : foundation.deliverables_en;
            return (
              <article className="module-card" key={foundation.id}>
                <span className="module-id">{foundation.id}</span>
                <strong>{lang === "zh" ? foundation.title_zh : foundation.title_en}</strong>
                <p>{lang === "zh" ? foundation.summary_zh : foundation.summary_en}</p>
                <small>{foundation.runnable_tier}</small>
                <p>{lang === "zh" ? "你会补齐：" : "You will repair:"} {skills.join("；")}</p>
                <p>{lang === "zh" ? "交付物：" : "Deliverables:"} {deliverables.join("；")}</p>
                <code>{doc}</code>
                <code>{notebook}</code>
                <a href={githubBlob(doc)} rel="noreferrer" target="_blank">
                  {lang === "zh" ? "打开讲义" : "Open note"}
                </a>
                <a href={getColabUrl(notebook)} rel="noreferrer" target="_blank">
                  {lang === "zh" ? "在 Colab 中打开" : "Open in Colab"}
                </a>
              </article>
            );
          })}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "切换时机" : "When to move on"}</p>
            <h3>{lang === "zh" ? "什么时候从基础包切到文章主线" : "When to leave the foundation pack for the article core"}</h3>
          </div>
        </div>
        <div className="checklist">
          {(lang === "zh"
            ? [
                "你已经能稳定跑 notebook，而不是靠碰运气刷新环境。",
                "你能解释 baseline、variant、sweep、ablation 各自是什么。",
                "你读 attention 图和向量图时，能说出具体的形状与方向关系。",
                "你愿意把实验写成日志，而不是只记一个印象。",
              ]
            : [
                "You can run notebooks reliably instead of succeeding only by luck.",
                "You can explain what a baseline, variant, sweep, and ablation each are.",
                "When you look at attention plots or vector plots, you can name the shape and directional relationships concretely.",
                "You are willing to write experiments as logs instead of keeping only an impression.",
              ]
          ).map((item) => (
            <article className="check-item" key={item}>
              <span>{item}</span>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "下一步" : "Next step"}</p>
            <h3>{lang === "zh" ? "回到主线" : "Return to the main path"}</h3>
          </div>
        </div>
        <div className="hero-actions">
          <Link href={`/${lang}`}>{lang === "zh" ? "回到课程首页" : "Return to course home"}</Link>
          <Link href={`/${lang}/research-ready`}>
            {lang === "zh" ? "进入研究训练营" : "Open the research-ready path"}
          </Link>
        </div>
      </section>
    </main>
  );
}
