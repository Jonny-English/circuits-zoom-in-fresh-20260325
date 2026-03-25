import fs from "node:fs";
import path from "node:path";

export type PaperRef = {
  title: string;
  url: string;
  date: string;
};

export type CourseModule = {
  id: string;
  order: number;
  title_zh: string;
  title_en: string;
  summary_zh: string;
  summary_en: string;
  prereqs: string[];
  paper_refs: PaperRef[];
  artifact_refs: string[];
  runnable_tier: string;
  web_slug: string;
};

export type GlossaryTerm = {
  id: string;
  term_zh: string;
  term_en: string;
  definition_zh: string;
  definition_en: string;
};

export type FoundationLab = {
  id: string;
  order: number;
  title_zh: string;
  title_en: string;
  summary_zh: string;
  summary_en: string;
  prereqs: string[];
  skills_zh: string[];
  skills_en: string[];
  deliverables_zh: string[];
  deliverables_en: string[];
  questions_zh: string[];
  questions_en: string[];
  runnable_tier: string;
  web_slug: string;
};

export type SelfCheck = {
  module_id: string;
  questions_zh: string[];
  questions_en: string[];
};

export type ReferenceOutput = {
  id: string;
  title_zh: string;
  title_en: string;
  summary_zh: string;
  summary_en: string;
  path_zh: string;
  path_en: string;
  best_for_zh: string;
  best_for_en: string;
};

export type ExtensionPaper = {
  id: string;
  title_zh: string;
  title_en: string;
  source_url: string;
  summary_zh: string;
  summary_en: string;
  why_now_zh: string;
  why_now_en: string;
  assignment_zh: string;
  assignment_en: string;
};

export type ProgramPayload = {
  goal_zh: string;
  goal_en: string;
  entry_requirements_zh: string[];
  entry_requirements_en: string[];
  study_contract_zh: string[];
  study_contract_en: string[];
  start_tracks: Array<{
    id: string;
    title_zh: string;
    title_en: string;
    audience_zh: string;
    audience_en: string;
    entry_signal_zh: string;
    entry_signal_en: string;
    first_steps_zh: string[];
    first_steps_en: string[];
    target_zh: string;
    target_en: string;
  }>;
  exit_portfolio_zh: string[];
  exit_portfolio_en: string[];
  phases: Array<{
    id: string;
    weeks: string;
    title_zh: string;
    title_en: string;
    focus_zh: string[];
    focus_en: string[];
    deliverables_zh: string[];
    deliverables_en: string[];
    gate_zh: string;
    gate_en: string;
  }>;
  weeks: Array<{
    id: string;
    title_zh: string;
    title_en: string;
    module_ids: string[];
    time_budget_hours: string;
    activities_zh: string[];
    activities_en: string[];
    outputs_zh: string[];
    outputs_en: string[];
    checkpoint_zh: string;
    checkpoint_en: string;
  }>;
  company_tasks: Array<{
    id: string;
    title_zh: string;
    title_en: string;
    brief_zh: string;
    brief_en: string;
    required_outputs_zh: string[];
    required_outputs_en: string[];
    timebox: string;
  }>;
  capstones: Array<{
    id: string;
    title_zh: string;
    title_en: string;
    brief_zh: string;
    brief_en: string;
  }>;
  rubric: Array<{
    skill_zh: string;
    skill_en: string;
    not_ready_zh: string;
    not_ready_en: string;
    near_ready_zh: string;
    near_ready_en: string;
    ready_zh: string;
    ready_en: string;
  }>;
};

export type ConceptGraph = {
  nodes: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    x: number;
    y: number;
    group: string;
  }>;
  edges: Array<{
    source: string;
    target: string;
    weight: number;
    label_zh: string;
    label_en: string;
  }>;
};

export type FeatureCatalog = {
  features: Array<{
    id: string;
    domain_zh: string;
    domain_en: string;
    label_zh: string;
    label_en: string;
    max_activation: number;
    examples_zh: string[];
    examples_en: string[];
  }>;
};

export type AttributionCase = {
  id: string;
  title_zh: string;
  title_en: string;
  question: string;
  answer: string;
  nodes: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    x: number;
    y: number;
    kind: string;
  }>;
  edges: Array<{
    source: string;
    target: string;
    score: number;
  }>;
};

export type TracingWorkflow = {
  steps: Array<{
    id: string;
    title_zh: string;
    title_en: string;
    output: string;
    estimated_minutes: number;
  }>;
};

export type PersonaPayload = {
  personas: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    scores_before: Record<string, number>;
    scores_after: Record<string, number>;
    vector: number[];
  }>;
  prompts: Array<{
    id: string;
    prompt: string;
    response_before: string;
    response_after: string;
  }>;
};

export type IntrospectionPayload = {
  cases: Array<{
    id: string;
    scenario_zh: string;
    scenario_en: string;
    self_report: number;
    behavior_signal: number;
  }>;
};

export type AssistantAxisPayload = {
  assistants: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    axis_position: number;
    helpfulness: number;
    safety: number;
    warmth: number;
  }>;
};

function repoRoot(): string {
  return path.join(process.cwd(), "..");
}

function readJson<T>(relativePath: string): T {
  const filePath = path.join(repoRoot(), relativePath);
  return JSON.parse(fs.readFileSync(filePath, "utf8")) as T;
}

export function getCourse(): CourseModule[] {
  return readJson<CourseModule[]>("content/course.json").sort((a, b) => a.order - b.order);
}

export function getGlossary(): GlossaryTerm[] {
  return readJson<GlossaryTerm[]>("content/glossary.json");
}

export function getFoundations(): FoundationLab[] {
  return readJson<FoundationLab[]>("content/foundations.json").sort((a, b) => a.order - b.order);
}

export function getSelfChecks(): SelfCheck[] {
  return readJson<SelfCheck[]>("content/self_checks.json");
}

export function getSelfCheck(id: string): SelfCheck {
  const item = getSelfChecks().find((entry) => entry.module_id === id);
  if (!item) {
    throw new Error(`Unknown self-check module: ${id}`);
  }
  return item;
}

export function getProgram(): ProgramPayload {
  return readJson<ProgramPayload>("content/program.json");
}

export function getReferenceOutputs(): ReferenceOutput[] {
  return readJson<ReferenceOutput[]>("content/reference_outputs.json");
}

export function getExtensions(): ExtensionPaper[] {
  return readJson<ExtensionPaper[]>("content/extensions.json");
}

export function getConceptGraph(): ConceptGraph {
  return readJson<ConceptGraph>("artifacts/concept_graph.json");
}

export function getFeatureCatalog(): FeatureCatalog {
  return readJson<FeatureCatalog>("artifacts/m03_feature_catalog.json");
}

export function getAttributionCases(): AttributionCase[] {
  return readJson<{ cases: AttributionCase[] }>("artifacts/m06_attribution_graph.json").cases;
}

export function getTracingWorkflow(): TracingWorkflow {
  return readJson<TracingWorkflow>("artifacts/m07_tracing_tool_workflow.json");
}

export function getPersonaPayload(): PersonaPayload {
  return readJson<PersonaPayload>("artifacts/m08_persona_vectors.json");
}

export function getIntrospectionPayload(): IntrospectionPayload {
  return readJson<IntrospectionPayload>("artifacts/m09_introspection_signals.json");
}

export function getAssistantAxisPayload(): AssistantAxisPayload {
  return readJson<AssistantAxisPayload>("artifacts/m10_assistant_axis.json");
}

export function getModule(_language: "zh" | "en", id: string): CourseModule {
  const module = getCourse().find((entry) => entry.id === id);
  if (!module) {
    throw new Error(`Unknown module: ${id}`);
  }
  return module;
}

export function getDoc(language: "zh" | "en", module: CourseModule): string {
  const filename = `${module.id.toLowerCase()}-${module.web_slug}.md`;
  return fs.readFileSync(path.join(repoRoot(), "docs", language, "modules", filename), "utf8");
}

export function getLocalizedTitle(module: CourseModule, language: "zh" | "en"): string {
  return language === "zh" ? module.title_zh : module.title_en;
}

export function getLocalizedSummary(module: CourseModule, language: "zh" | "en"): string {
  return language === "zh" ? module.summary_zh : module.summary_en;
}

export function getColabUrl(relativeNotebookPath: string): string {
  return `https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/${relativeNotebookPath}`;
}

export function flattenTimeline(course: CourseModule[]) {
  return course
    .map((module) => {
      const paper = module.paper_refs[0];
      return {
        ...paper,
        moduleId: module.id,
        moduleTitleEn: module.title_en,
        moduleTitleZh: module.title_zh,
      };
    })
    .sort((a, b) => a.date.localeCompare(b.date));
}
