import type { AssistantAxisPayload } from "@/lib/course";

export function AssistantAxisPreview({
  payload,
  language,
}: {
  payload: AssistantAxisPayload;
  language: "zh" | "en";
}) {
  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{language === "zh" ? "Artifact 预览" : "Artifact preview"}</p>
          <h3>{language === "zh" ? "助手轴中的风格分布" : "Style distribution on the assistant axis"}</h3>
        </div>
      </div>
      <svg className="graph compact" viewBox="0 0 1000 360" role="img">
        <line x1={100} x2={900} y1={180} y2={180} stroke="#8ea3b8" strokeWidth={2} />
        {payload.assistants.map((assistant) => {
          const x = 500 + assistant.axis_position * 320;
          const y = 300 - assistant.helpfulness * 180;
          return (
            <g key={assistant.id}>
              <circle cx={x} cy={y} fill="#c96a28" r={18 + assistant.safety * 8} />
              <text x={x} y={y + 42} textAnchor="middle">
                {language === "zh" ? assistant.label_zh : assistant.label_en}
              </text>
            </g>
          );
        })}
      </svg>
      <ul className="edge-list">
        {payload.assistants
          .slice()
          .sort((a, b) => a.axis_position - b.axis_position)
          .map((assistant) => (
            <li key={assistant.id}>
              <strong>{language === "zh" ? assistant.label_zh : assistant.label_en}</strong>
              <span>
                axis={assistant.axis_position.toFixed(2)} · helpfulness={assistant.helpfulness.toFixed(2)} · safety=
                {assistant.safety.toFixed(2)}
              </span>
            </li>
          ))}
      </ul>
    </section>
  );
}
