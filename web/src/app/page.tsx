import Link from "next/link";

export default function HomePage() {
  return (
    <main className="landing">
      <section className="hero">
        <p className="eyebrow">Bilingual article-first interpretability course</p>
        <h1>From Circuits to Claude</h1>
        <p className="hero-copy">
          Start with visual circuits, then move article by article through superposition,
          sparse features, steering, circuit tracing, introspection, and the assistant axis.
          If you need a gentler runway first, there is also a Pre-P4 foundation pack; if you want
          to go further, the repository includes a 12-week research-ready track with deliverables,
          rubrics, reference outputs, and company-style simulation tasks.
        </p>
        <div className="hero-actions">
          <Link href="/zh">进入中文课程</Link>
          <Link href="/en">Open English course</Link>
          <Link href="/zh/foundations">基础包</Link>
          <Link href="/zh/research-ready">研究训练营</Link>
          <Link href="/timeline">View paper timeline</Link>
        </div>
      </section>
    </main>
  );
}
