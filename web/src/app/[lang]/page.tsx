import Link from "next/link";

import { ConceptGraph } from "@/components/ConceptGraph";
import { GlossaryCards } from "@/components/GlossaryCards";
import { ProgressTracker } from "@/components/ProgressTracker";
import {
  getConceptGraph,
  getCourse,
  getGlossary,
  getLocalizedSummary,
  getLocalizedTitle,
} from "@/lib/course";

export function generateStaticParams() {
  return [{ lang: "zh" }, { lang: "en" }];
}

export default async function LanguageHome({
  params,
}: {
  params: Promise<{ lang: "zh" | "en" }>;
}) {
  const { lang: language } = await params;
  const course = getCourse();
  const modules = course.map((module) => ({
    ...module,
    title: getLocalizedTitle(module, language),
    summary: getLocalizedSummary(module, language),
  }));
  const glossary = getGlossary();
  const graph = getConceptGraph();

  return (
    <main className="content-grid">
      <section className="hero module-hero">
        <p className="eyebrow">{language === "zh" ? "文章总览" : "Article overview"}</p>
        <h1>{language === "zh" ? "从视觉电路一路读到助手轴" : "From visual circuits to the assistant axis"}</h1>
        <p className="hero-copy">
          {language === "zh"
            ? "每一篇文章都有自己独立的讲义和 Colab。你可以顺着时间线读，也可以按 prerequisite 从前往后走；如果你的目标是进入公司研究，还有一条带交付物和 rubric 的 12 周训练营。"
            : "Each paper now has its own mirrored note and Colab notebook. You can follow the timeline or walk the prerequisite chain from front to back; if your goal is company research, there is also a 12-week track with deliverables and a rubric."}
        </p>
        <div className="hero-actions">
          <Link href={`/${language}/research-ready`}>
            {language === "zh" ? "进入研究训练营" : "Open the research-ready path"}
          </Link>
          <Link href="/timeline">{language === "zh" ? "论文时间线" : "Paper timeline"}</Link>
        </div>
      </section>

      <section className="panel module-grid">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{language === "zh" ? "文章" : "Articles"}</p>
            <h3>{language === "zh" ? "按编号逐篇学习" : "Follow the numbered paper path"}</h3>
          </div>
        </div>
        <div className="cards">
          {modules.map((module) => (
            <Link className="module-card" href={`/${language}/modules/${module.id}`} key={module.id}>
              <span className="module-id">{module.id}</span>
              <strong>{module.title}</strong>
              <p>{module.summary}</p>
              <small>{module.runnable_tier}</small>
            </Link>
          ))}
        </div>
      </section>

      <ProgressTracker
        heading={language === "zh" ? "本地进度" : "Local progress"}
        modules={modules.map((module) => ({ id: module.id, title: module.title }))}
      />
      <ConceptGraph graph={graph} language={language} />
      <GlossaryCards terms={glossary} language={language} />
    </main>
  );
}
