import type { IntrospectionPayload } from "@/lib/course";

export function IntrospectionPreview({
  payload,
  language,
}: {
  payload: IntrospectionPayload;
  language: "zh" | "en";
}) {
  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{language === "zh" ? "Artifact 预览" : "Artifact preview"}</p>
          <h3>{language === "zh" ? "自述与行为的差距" : "Gaps between self-report and behavior"}</h3>
        </div>
      </div>
      <div className="metric-grid">
        {payload.cases.map((item) => {
          const gap = Math.abs(item.self_report - item.behavior_signal);
          return (
            <article className="metric-card" key={item.id}>
              <strong>{language === "zh" ? item.scenario_zh : item.scenario_en}</strong>
              <div className="metric-row">
                <span>{language === "zh" ? "自述" : "Self-report"}</span>
                <div className="mini-track">
                  <div className="mini-fill report" style={{ width: `${item.self_report * 100}%` }} />
                </div>
              </div>
              <div className="metric-row">
                <span>{language === "zh" ? "行为" : "Behavior"}</span>
                <div className="mini-track">
                  <div className="mini-fill behavior" style={{ width: `${item.behavior_signal * 100}%` }} />
                </div>
              </div>
              <p>{language === "zh" ? "差距" : "Gap"}: {gap.toFixed(2)}</p>
            </article>
          );
        })}
      </div>
    </section>
  );
}
