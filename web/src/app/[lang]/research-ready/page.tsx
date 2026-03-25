import { getProgram } from "@/lib/course";

export function generateStaticParams() {
  return [{ lang: "zh" }, { lang: "en" }];
}

export default async function ResearchReadyPage({
  params,
}: {
  params: Promise<{ lang: "zh" | "en" }>;
}) {
  const { lang } = await params;
  const program = getProgram();
  const entryRequirements = lang === "zh" ? program.entry_requirements_zh : program.entry_requirements_en;
  const studyContract = lang === "zh" ? program.study_contract_zh : program.study_contract_en;
  const exitPortfolio = lang === "zh" ? program.exit_portfolio_zh : program.exit_portfolio_en;

  return (
    <main className="content-grid">
      <section className="hero module-hero">
        <p className="eyebrow">{lang === "zh" ? "研究训练营" : "Research-ready bootcamp"}</p>
        <h1>{lang === "zh" ? "把课程变成入门研究能力" : "Turn the course into entry-level research ability"}</h1>
        <p className="hero-copy">{lang === "zh" ? program.goal_zh : program.goal_en}</p>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "起点" : "Starting point"}</p>
            <h3>{lang === "zh" ? "进入训练营前你要具备什么" : "What you should have before starting"}</h3>
          </div>
        </div>
        <div className="checklist">
          {entryRequirements.map((item) => (
            <article className="check-item" key={item}>
              <span>{item}</span>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "双起跑线" : "Two runways"}</p>
            <h3>{lang === "zh" ? "为小白和有基础者准备的两条起跑线" : "Two starting lines for true beginners and prepared readers"}</h3>
          </div>
        </div>
        <div className="cards">
          {program.start_tracks.map((track) => (
            <article className="module-card" key={track.id}>
              <span className="module-id">{track.id}</span>
              <strong>{lang === "zh" ? track.title_zh : track.title_en}</strong>
              <p>{lang === "zh" ? track.audience_zh : track.audience_en}</p>
              <p>{lang === "zh" ? "进入信号：" : "Entry signal:"} {lang === "zh" ? track.entry_signal_zh : track.entry_signal_en}</p>
              <p>{lang === "zh" ? "先做什么：" : "First steps:"} {(lang === "zh" ? track.first_steps_zh : track.first_steps_en).join("；")}</p>
              <p>{lang === "zh" ? "目标：" : "Target:"} {lang === "zh" ? track.target_zh : track.target_en}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "训练契约" : "Training contract"}</p>
            <h3>{lang === "zh" ? "保证内容不流于浏览的硬约束" : "Rules that keep this from becoming passive browsing"}</h3>
          </div>
        </div>
        <div className="checklist">
          {studyContract.map((item) => (
            <article className="check-item" key={item}>
              <span>{item}</span>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "阶段" : "Phases"}</p>
            <h3>{lang === "zh" ? "五段式训练路径" : "Five-stage training path"}</h3>
          </div>
        </div>
        <div className="cards">
          {program.phases.map((phase) => (
            <article className="module-card" key={phase.id}>
              <span className="module-id">{phase.id}</span>
              <strong>{lang === "zh" ? phase.title_zh : phase.title_en}</strong>
              <small>{phase.weeks}</small>
              <p>{(lang === "zh" ? phase.focus_zh : phase.focus_en).join("；")}</p>
              <p>{lang === "zh" ? "交付物：" : "Deliverables:"} {(lang === "zh" ? phase.deliverables_zh : phase.deliverables_en).join("；")}</p>
              <p>{lang === "zh" ? "过关标准：" : "Exit gate:"} {lang === "zh" ? phase.gate_zh : phase.gate_en}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "周计划" : "Weekly plan"}</p>
            <h3>{lang === "zh" ? "12 周输出导向安排" : "A 12-week output-oriented schedule"}</h3>
          </div>
        </div>
        <div className="metric-grid">
          {program.weeks.map((week) => (
            <article className="metric-card" key={week.id}>
              <strong>{week.id} · {lang === "zh" ? week.title_zh : week.title_en}</strong>
              <p>{lang === "zh" ? "时间预算：" : "Time budget:"} {week.time_budget_hours} {lang === "zh" ? "小时/周" : "hours/week"}</p>
              <p>{lang === "zh" ? "关联文章：" : "Articles:"} {week.module_ids.join(", ")}</p>
              <p>{lang === "zh" ? "任务：" : "Activities:"} {(lang === "zh" ? week.activities_zh : week.activities_en).join("；")}</p>
              <p>{lang === "zh" ? "输出：" : "Outputs:"} {(lang === "zh" ? week.outputs_zh : week.outputs_en).join("；")}</p>
              <p>{lang === "zh" ? "检查点：" : "Checkpoint:"} {lang === "zh" ? week.checkpoint_zh : week.checkpoint_en}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "公司任务" : "Company tasks"}</p>
            <h3>{lang === "zh" ? "先做像公司里真的会给你的任务" : "Practice the kinds of tasks companies actually assign"}</h3>
          </div>
        </div>
        <div className="cards">
          {program.company_tasks.map((task) => (
            <article className="module-card" key={task.id}>
              <span className="module-id">{task.id}</span>
              <strong>{lang === "zh" ? task.title_zh : task.title_en}</strong>
              <small>{task.timebox}</small>
              <p>{lang === "zh" ? task.brief_zh : task.brief_en}</p>
              <p>{lang === "zh" ? "必须产出：" : "Required outputs:"} {(lang === "zh" ? task.required_outputs_zh : task.required_outputs_en).join("；")}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "Capstone" : "Capstones"}</p>
            <h3>{lang === "zh" ? "把课程知识压缩成一个研究提案" : "Compress the course into a research proposal"}</h3>
          </div>
        </div>
        <div className="cards">
          {program.capstones.map((capstone) => (
            <article className="module-card" key={capstone.id}>
              <span className="module-id">{capstone.id}</span>
              <strong>{lang === "zh" ? capstone.title_zh : capstone.title_en}</strong>
              <p>{lang === "zh" ? capstone.brief_zh : capstone.brief_en}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "作品集" : "Exit portfolio"}</p>
            <h3>{lang === "zh" ? "训练结束时你应该拿得出什么" : "What you should be able to show at the end"}</h3>
          </div>
        </div>
        <div className="checklist">
          {exitPortfolio.map((item) => (
            <article className="check-item" key={item}>
              <span>{item}</span>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{lang === "zh" ? "准备度" : "Readiness"}</p>
            <h3>{lang === "zh" ? "你是否已经接近公司研究门槛" : "Whether you are approaching the bar for company research"}</h3>
          </div>
        </div>
        <div className="cards">
          {program.rubric.map((item) => (
            <article className="module-card" key={item.skill_en}>
              <strong>{lang === "zh" ? item.skill_zh : item.skill_en}</strong>
              <p>{lang === "zh" ? "未就绪：" : "Not ready:"} {lang === "zh" ? item.not_ready_zh : item.not_ready_en}</p>
              <p>{lang === "zh" ? "接近就绪：" : "Near ready:"} {lang === "zh" ? item.near_ready_zh : item.near_ready_en}</p>
              <p>{lang === "zh" ? "就绪：" : "Ready:"} {lang === "zh" ? item.ready_zh : item.ready_en}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
