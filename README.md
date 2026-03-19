<h1 align="center">🧠 claude-skills</h1>
<p align="center"><strong>The definitive open-source AI skills library for Claude</strong></p>

<p align="center">
  <a href="https://github.com/xcrrr/claude-skills/stargazers"><img src="https://img.shields.io/github/stars/xcrrr/claude-skills?style=for-the-badge&logo=github&color=FFD700" alt="Stars"></a>
  <a href="https://github.com/xcrrr/claude-skills/network/members"><img src="https://img.shields.io/github/forks/xcrrr/claude-skills?style=for-the-badge&logo=github&color=4ECDC4" alt="Forks"></a>
  <a href="https://github.com/xcrrr/claude-skills/blob/main/LICENSE"><img src="https://img.shields.io/github/license/xcrrr/claude-skills?style=for-the-badge&color=FF6B6B" alt="License"></a>
  <a href="https://github.com/xcrrr/claude-skills/graphs/contributors"><img src="https://img.shields.io/github/contributors/xcrrr/claude-skills?style=for-the-badge&color=95E1D3" alt="Contributors"></a>
</p>

---

## What is this?

**xcrrr/claude-skills** is a curated, community-driven library of structured prompt skills designed to unlock the full potential of Claude across dozens of professional domains. Each skill is a battle-tested prompt template with clear instructions, real-world examples, and best practices so you can get expert-level results from Claude without starting from scratch. Whether you're a developer, writer, data analyst, or business professional, this library gives you a plug-and-play toolkit to supercharge your workflow.

---

## 📚 Skill Library

### ✍️ Writing

| Skill | Description |
|---|---|
| [academic-essay](skills/writing/academic-essay/) | Use this skill when writing academic essays, research papers, literature reviews, or any formal scholarly writing that requires thesis development, structured argumentation, citation integration, and academic tone. Trigger phrases: 'write an argumentative essay on', 'help me structure a literature review', 'write a thesis statement for'. Do NOT use for blog posts, casual writing, or creative nonfiction |
| [blog-post](skills/writing/blog-post/) | Use this skill when writing blog posts, articles, or long-form web content—from quick how-to guides to in-depth opinion pieces. Trigger phrases: 'write a blog post about', 'draft an article on', 'create a post for my blog'. Do NOT use for academic papers, news reporting, or content requiring real-time facts |
| [copywriter](skills/writing/copywriter/) | Use this skill when writing persuasive, conversion-focused copy—landing pages, product descriptions, ads, sales emails, or any content designed to move someone to action. Trigger phrases: 'write copy for my landing page', 'describe this product', 'write an ad for'. Do NOT use for informational content, technical documentation, or long-form editorial writing |
| [cover-letter](skills/writing/cover-letter/) | Use this skill when writing a job application cover letter that needs to be tailored to a specific role and company. Trigger phrases: 'write a cover letter for', 'help me apply to', 'draft a letter for this job posting'. Do NOT use for general professional bios, LinkedIn summaries, or any application that explicitly says not to include a cover letter |
| [email-drafter](skills/writing/email-drafter/) | Use this skill when drafting professional or personal emails—cold outreach, follow-ups, internal memos, client communication, or any message that needs to be clear and effective. Trigger phrases: 'write an email to', 'draft a follow-up', 'help me email'. Do NOT use for mass marketing email campaigns (use copywriter skill) or legal/formal notices requiring specific language |
| [proofreader](skills/writing/proofreader/) | Use this skill when reviewing written content for grammar, spelling, punctuation, style consistency, and tone—before publishing, submitting, or sending. Trigger phrases: 'proofread this', 'check my writing', 'review this for errors', 'edit this email/report/essay'. Do NOT use when structural rewrites or content changes are needed—proofreading fixes surface errors, not substantive problems |
| [social-media](skills/writing/social-media/) | Use this skill when writing platform-specific social media content—Twitter/X threads, LinkedIn posts, Instagram captions, or short-form content designed to drive engagement, shares, or follows. Trigger phrases: 'write a tweet about', 'create a LinkedIn post', 'write an Instagram caption', 'write a thread'. Do NOT use for long-form articles or blog posts, or email newsletters |
| [storyteller](skills/writing/storyteller/) | Use this skill when writing fiction, narrative nonfiction, brand stories, or any content where emotional engagement and narrative arc matter more than pure information delivery. Trigger phrases: 'write a short story', 'tell my brand's origin story', 'write a narrative about', 'create a character'. Do NOT use for purely informational content, technical writing, or persuasive copy without a narrative component |
| [technical-writer](skills/writing/technical-writer/) | Use this skill when creating technical documentation, API references, installation guides, README files, or any content that explains how a system, tool, or process works to a technical audience. Trigger phrases: 'document this API', 'write a README', 'create a setup guide'. Do NOT use for marketing copy about a product or non-technical how-to content aimed at general audiences |

### 💻 Coding

| Skill | Description |
|---|---|
| [api-designer](skills/coding/api-designer/) | Use this skill when designing or reviewing REST APIs, writing OpenAPI specifications, or making decisions about URL structure, HTTP methods, and response formats. Trigger phrases: 'design an API for', 'what endpoints do I need', 'how should I structure this API'. Not for implementing the API server code or designing GraphQL schemas |
| [architecture-designer](skills/coding/architecture-designer/) | Use this skill when designing system architecture, making technology stack decisions, evaluating trade-offs between architectural patterns, or writing Architecture Decision Records (ADRs). Trigger phrases: 'design a system for', 'what architecture should I use', 'monolith vs microservices', 'how should I structure this'. Not for implementation-level code design or UI/UX design |
| [code-reviewer](skills/coding/code-reviewer/) | Use this skill when reviewing pull requests, auditing code quality, or providing structured feedback on code. Trigger phrases: 'review this code', 'check my PR', 'what's wrong with this', 'give feedback on'. Not for writing new code from scratch or debugging runtime errors |
| [debugger](skills/coding/debugger/) | Use this skill when tracking down a bug, understanding an error message, or diagnosing unexpected behavior in code. Trigger phrases: 'this is broken', 'I'm getting an error', 'why does this crash', 'help me debug'. Not for code review of working code or designing new features |
| [documentation-writer](skills/coding/documentation-writer/) | Use this skill when writing or improving technical documentation including READMEs, docstrings, API docs, changelogs, or inline code comments. Trigger phrases: 'write a README', 'document this function', 'add docstrings', 'improve the docs'. Not for writing blog posts, marketing copy, or user-facing help articles |
| [refactorer](skills/coding/refactorer/) | Use this skill when improving the structure, clarity, or design of existing code without changing its behavior. Trigger phrases: 'clean up this code', 'this is messy', 'refactor this', 'apply SOLID principles'. Not for adding new features or fixing bugs |
| [regex-master](skills/coding/regex-master/) | Use this skill when building, explaining, or debugging regular expressions for pattern matching, validation, or text extraction. Trigger phrases: 'write a regex', 'match this pattern', 'validate this format', 'extract from text'. Not for natural language parsing or full grammar parsing (use a parser instead) |
| [security-auditor](skills/coding/security-auditor/) | Use this skill when auditing code for security vulnerabilities, reviewing authentication and authorization logic, or checking OWASP compliance. Trigger phrases: 'audit this for security', 'is this secure', 'check for vulnerabilities', 'OWASP review'. Not for penetration testing tooling or network security configuration |
| [sql-expert](skills/coding/sql-expert/) | Use this skill when writing, optimizing, or reviewing SQL queries, designing database schemas, or diagnosing slow query performance. Trigger phrases: 'write a SQL query', 'optimize this query', 'why is this slow', 'how do I join these tables'. Not for NoSQL databases or ORM-specific code generation |
| [test-writer](skills/coding/test-writer/) | Use this skill when writing unit tests, integration tests, or end-to-end tests for existing or new code. Trigger phrases: 'write tests for', 'add test coverage', 'how do I test this', 'TDD this feature'. Not for running or debugging test infrastructure or CI pipelines |

### 📊 Data

| Skill | Description |
|---|---|
| [chart-builder](skills/data/chart-builder/) | Use this skill when creating data visualizations, selecting the right chart type, or generating chart code. Trigger phrases: 'build a chart', 'visualize this data', 'create a graph', 'plot these numbers', 'which chart should I use for'. Not for building interactive dashboards, designing UI components, or creating infographics with design tools like Figma |
| [dashboard-designer](skills/data/dashboard-designer/) | Use this skill when designing a data dashboard—choosing KPIs, structuring layout, applying visual hierarchy, or deciding which BI tool to use. Trigger phrases: 'design a dashboard', 'build a KPI dashboard', 'what should my dashboard show', 'help me layout a dashboard', 'dashboard for monitoring'. Not for building chart code from scratch (use chart-builder), writing SQL queries (use sql-analyst), or designing marketing landing pages |
| [data-analyst](skills/data/data-analyst/) | Use this skill when analyzing datasets, identifying trends, running statistical summaries, or interpreting data to answer business questions. Trigger phrases: 'analyze this data', 'what does this data show', 'find patterns in', 'summarize these results', 'is this statistically significant'. Not for building production data pipelines, creating live dashboards, or writing database schema designs |
| [data-cleaner](skills/data/data-cleaner/) | Use this skill when preparing raw data for analysis—handling missing values, removing duplicates, fixing data types, resolving inconsistent formats, or filtering outliers. Trigger phrases: 'clean this data', 'fix the missing values', 'standardize these dates', 'deduplicate this dataset', 'the data has formatting issues'. Not for designing database schemas, building ETL pipelines for production systems, or statistical modeling |
| [excel-expert](skills/data/excel-expert/) | Use this skill when working with Excel or Google Sheets formulas, pivot tables, data validation, conditional formatting, or building spreadsheet-based tools. Trigger phrases: 'Excel formula for', 'how do I VLOOKUP', 'build a pivot table', 'conditional formatting rule', 'create a dashboard in Excel'. Not for writing VBA macros, building Python/SQL alternatives to Excel, or migrating data out of spreadsheets |
| [sql-analyst](skills/data/sql-analyst/) | Use this skill when writing SQL queries for data analysis, reporting, or business metrics. Trigger phrases: 'write a SQL query to', 'how do I calculate in SQL', 'build a report using SQL', 'SQL for monthly active users', 'write a retention query'. Not for database administration, schema design, query optimization for production systems, or NoSQL databases |

### 💼 Business

| Skill | Description |
|---|---|
| [business-analyst](skills/business/business-analyst/) | Use this skill when gathering and documenting business requirements, mapping processes, performing gap analysis, writing business requirements documents (BRDs), or modeling stakeholder impact. Trigger phrases: 'write a business requirements document', 'map this process', 'gather requirements for', 'gap analysis for', 'AS-IS TO-BE process'. Not for writing user stories (use product-manager skill), conducting user research (use ux-researcher), or financial modeling |
| [competitor-analyst](skills/business/competitor-analyst/) | Use this skill when analyzing competitors, building competitive positioning, creating feature comparison matrices, or applying strategic frameworks like SWOT or Porter's Five Forces. Trigger phrases: 'analyze our competitors', 'competitive analysis for', 'how do we compare to', 'create a feature matrix', 'SWOT analysis of'. Not for sizing the total market (use market-researcher), writing pitch decks (use pitch-deck-writer), or pricing strategy modeling |
| [market-researcher](skills/business/market-researcher/) | Use this skill when sizing a market, analyzing competitors, designing customer surveys, segmenting audiences, or synthesizing research into market insights. Trigger phrases: 'size the market for', 'analyze our competitors', 'who is our target customer', 'design a survey to understand', 'TAM/SAM/SOM for'. Not for building financial models, writing pitch decks, or conducting UX usability research |
| [meeting-facilitator](skills/business/meeting-facilitator/) | Use this skill when designing meeting agendas, facilitating team sessions, writing post-meeting notes, or improving meeting effectiveness. Trigger phrases: 'design an agenda for', 'facilitate a retrospective', 'write meeting notes for', 'how do I run a decision meeting', 'make our standups better'. Not for writing project plans, OKRs, or business requirements documents |
| [okr-planner](skills/business/okr-planner/) | Use this skill when defining company, team, or individual OKRs, running a quarterly planning process, scoring key results, or cascading goals across an organization. Trigger phrases: 'write OKRs for', 'help me set quarterly goals', 'is this a good key result', 'how do we cascade OKRs', 'score my OKRs'. Not for writing job descriptions, building project plans, or creating financial budgets |
| [pitch-deck-writer](skills/business/pitch-deck-writer/) | Use this skill when creating investor pitch decks, writing slide narratives, structuring a fundraising story, or preparing presentation content for VCs or angels. Trigger phrases: 'write a pitch deck', 'help me structure my pitch', 'what slides should I include', 'write the narrative for my Series A deck', 'investor presentation for'. Not for writing business plans, financial models, or internal strategy documents |
| [product-manager](skills/business/product-manager/) | Use this skill when writing product requirements documents, prioritizing features, creating user stories, defining acceptance criteria, or setting product metrics. Trigger phrases: 'write a PRD for', 'prioritize this feature backlog', 'write user stories for', 'help me define acceptance criteria', 'what metrics should we track for'. Not for writing code, designing UI mockups, or conducting user research interviews |
| [ux-researcher](skills/business/ux-researcher/) | Use this skill when planning or conducting user research, writing interview guides, designing surveys for UX insights, synthesizing qualitative findings, creating personas, or writing research reports. Trigger phrases: 'write a user interview guide', 'how do I conduct usability testing', 'synthesize research findings', 'create a user persona', 'design a UX survey'. Not for quantitative market sizing (use market-researcher), writing business requirements (use business-analyst), or product analytics |

### 🔬 Research

| Skill | Description |
|---|---|
| [citation-formatter](skills/research/citation-formatter/) | Use this skill when formatting references, citations, or bibliographies in academic or professional styles. Trigger phrases: 'format this citation', 'create a bibliography', 'cite this source in APA', 'convert citation to MLA'. Do NOT use for finding or verifying the accuracy of sources—only for formatting known sources into a specified citation style |
| [fact-checker](skills/research/fact-checker/) | Use this skill when verifying factual claims, checking accuracy of statements, or assessing the credibility of information. Trigger phrases: 'fact-check this', 'is this true', 'verify this claim', 'check if this is accurate'. Do NOT use for subjective opinions, legal or medical advice, or claims requiring real-time data or breaking news |
| [literature-reviewer](skills/research/literature-reviewer/) | Use this skill when conducting a literature review or surveying academic research on a topic. Trigger phrases: 'do a literature review', 'survey the research on', 'what does the literature say about', 'review academic papers on'. Do NOT use for primary research data collection, statistical data analysis, or generating new original knowledge |
| [summarizer](skills/research/summarizer/) | Use this skill when condensing long documents, articles, reports, or passages into shorter, accurate summaries. Trigger phrases: 'summarize this', 'give me the key points', 'TL;DR', 'condense this document'. Do NOT use when author voice and style must be preserved for creative works, or as a substitute for full reading of legal contracts, medical documents, or other high-stakes materials |
| [web-researcher](skills/research/web-researcher/) | Use this skill when you need to research a topic online, gather information from multiple sources, or evaluate source credibility. Trigger phrases: 'research', 'find information about', 'look up', 'investigate'. Not for academic systematic reviews (use literature-reviewer) or fact-checking specific claims (use fact-checker) |

### 🎨 Design

| Skill | Description |
|---|---|
| [color-palette](skills/design/color-palette/) | Use this skill when creating, evaluating, or documenting color palettes for brands, products, or design systems. Trigger phrases: 'create a color palette', 'what colors should I use', 'brand colors for', 'accessible color scheme'. Do NOT use for image editing, photo color correction, or print production color matching |
| [design-critiquer](skills/design/design-critiquer/) | Use this skill when reviewing, evaluating, or giving structured feedback on UI designs, wireframes, mockups, or design systems. Trigger phrases: 'critique this design', 'give feedback on my UI', 'review this wireframe', 'what's wrong with this design'. Do NOT use for writing code, implementing designs, or marketing material critique |
| [frontend-design](skills/design/frontend-design/) | Use this skill when specifying, designing, or documenting UI components, layouts, and design systems for frontend implementation. Trigger phrases: 'design this UI component', 'create a responsive layout', 'spec the CSS for', 'design system for'. Do NOT use for backend development, server-side logic, data engineering, or writing server code |
| [ux-writer](skills/design/ux-writer/) | Use this skill when crafting microcopy, UI text, or in-product writing—error messages, tooltips, button labels, empty states, onboarding flows, and confirmation dialogs. Trigger phrases: 'write microcopy for', 'write UI copy', 'write error messages', 'write onboarding text', 'button label for'. Do NOT use for marketing copy (use copywriter) or long-form documentation (use technical-writer) |

### ⚡ Productivity

| Skill | Description |
|---|---|
| [decision-maker](skills/productivity/decision-maker/) | Use this skill when you face a complex or high-stakes decision and need a structured framework to evaluate options objectively. Ideal for career choices, product prioritization, vendor selection, or any multi-criteria trade-off. Not for trivial daily decisions or situations that require licensed professional advice |
| [habit-builder](skills/productivity/habit-builder/) | Use this skill when designing new habits, building routines, or creating systems to make behavior change stick. Trigger phrases: 'help me build a habit', 'create a morning routine', 'how do I stick to', 'design a habit system for'. Do NOT use for medical or clinical behavior change programs requiring professional supervision |
| [journaling](skills/productivity/journaling/) | Use this skill when writing journal entries, generating reflection prompts, or reviewing a period of time through structured writing. Trigger phrases: 'help me journal about', 'journal prompts for', 'reflect on my week', 'write a journal entry'. Do NOT use for formal therapy or clinical mental health intervention |
| [note-taker](skills/productivity/note-taker/) | Use this skill when capturing, organizing, or restructuring notes from meetings, research, lectures, or brainstorms. Trigger phrases: 'take notes on this', 'organize my notes', 'summarize this meeting', 'structure these notes'. Do NOT use for formal minutes requiring legal accuracy or verbatim transcription |
| [task-planner](skills/productivity/task-planner/) | Use this skill when breaking down projects, planning a week, or turning vague goals into concrete action steps. Trigger phrases: 'help me plan my week', 'break this project into tasks', 'create an action plan for', 'prioritize my to-do list'. Do NOT use for long-term strategic roadmaps or OKR setting |

### ⚖️ Legal

| Skill | Description |
|---|---|
| [contract-reviewer](skills/legal/contract-reviewer/) | Use this skill when you need to review a contract for risky clauses, missing protections, one-sided provisions, or negotiation leverage before signing. Suitable for employment agreements, SaaS subscriptions, vendor contracts, NDAs, and freelance agreements. Not a substitute for a licensed attorney — always seek qualified legal counsel for high-value or complex contracts |
| [legal-summarizer](skills/legal/legal-summarizer/) | Use this skill when you need to translate a dense legal document—contract, court ruling, statute, regulation, or policy—into clear plain-English that a non-lawyer can understand and act on. Ideal for summarizing leases, court opinions, employment agreements, privacy policies, and legislation. Not a substitute for legal advice; consult a licensed attorney for decisions with significant legal consequences |
| [terms-of-service](skills/legal/terms-of-service/) | Use this skill when you need to draft Terms of Service, a Privacy Policy, or an End-User License Agreement (EULA) for a web application, SaaS product, or mobile app. Produces comprehensive, plain-English legal documents that cover user rights, data practices, liability limits, and dispute resolution. Not a substitute for a licensed attorney; have a lawyer review before publishing for a production product |

### 💰 Finance

| Skill | Description |
|---|---|
| [budget-planner](skills/finance/budget-planner/) | Use this skill when you need to build, review, or refine personal or business budgets — triggered by phrases like 'help me budget', 'create a spending plan', 'where is my money going', or 'plan my finances'. Not for tax filing, investment portfolio management, or legal financial advice |
| [financial-analyst](skills/finance/financial-analyst/) | Use this skill when you need financial modeling, ratio analysis, or business financial health assessment — triggered by phrases like 'analyze my financials', 'calculate my burn rate', 'model this scenario', or 'is this business profitable'. Not for tax advice, bookkeeping, or regulated investment advisory services |
| [invoice-generator](skills/finance/invoice-generator/) | Use this skill when you need to create, format, or review a professional invoice — triggered by phrases like 'generate an invoice', 'bill my client', 'create an invoice for', or 'write up my charges'. Not for tax returns, payroll processing, or accounts-receivable system integrations |

### 🎓 Education

| Skill | Description |
|---|---|
| [flashcard-maker](skills/education/flashcard-maker/) | Use this skill when creating Q&A flashcard decks optimized for spaced repetition and memorization. Triggers: 'make flashcards for', 'create an Anki deck', 'turn these notes into flashcards', 'I need to memorize'. Not for writing practice tests with multiple-choice options, generating essay prompts, or producing study guides with explanatory prose |
| [lesson-planner](skills/education/lesson-planner/) | Use this skill when designing structured lesson plans with clear learning objectives, warm-up activities, direct instruction, guided practice, independent practice, and formative assessment. Triggers: 'create a lesson plan', 'plan a class on', 'design a unit for', 'align to Common Core/NGSS'. Not for grading student work, writing full curriculum maps, or producing parent newsletters |
| [quiz-creator](skills/education/quiz-creator/) | Use this skill when you need to generate quiz questions, assessments, or practice tests — triggered by phrases like 'create a quiz on', 'write test questions about', 'make practice questions for', or 'generate an assessment'. Not for grading submitted student work, writing full lesson plans, or creating legally proctored exam content |
| [tutor](skills/education/tutor/) | Use this skill when someone needs a concept explained, a topic taught, or help understanding something difficult — triggered by phrases like 'explain this to me', 'I don't understand', 'teach me about', or 'help me learn'. Not for grading assignments, writing essays on behalf of students, or producing academic work for submission |

### 🛠️ DevOps

| Skill | Description |
|---|---|
| [ci-cd-helper](skills/devops/ci-cd-helper/) | Use this skill when designing, writing, or troubleshooting CI/CD pipelines for GitHub Actions, GitLab CI, CircleCI, Jenkins, and similar platforms. Triggers: 'set up a CI pipeline', 'write a GitHub Actions workflow', 'my pipeline is failing', 'automate my deployment'. Not for provisioning cloud infrastructure from scratch, writing application code, or designing database migration strategies |
| [docker-expert](skills/devops/docker-expert/) | Use this skill when writing optimized Dockerfiles, multi-stage builds, Docker Compose configurations, or applying container security and performance best practices. Triggers: 'write a Dockerfile for', 'optimize my Docker image', 'set up Docker Compose for', 'containerize my app'. Not for writing Kubernetes manifests, provisioning cloud container services (ECS, Cloud Run), or designing CI/CD pipelines |
| [kubernetes-helper](skills/devops/kubernetes-helper/) | Use this skill when generating, explaining, or troubleshooting Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, Ingress, HPA, and Helm chart structures. Triggers: 'write a Kubernetes manifest for', 'create a Helm chart', 'my pod is CrashLoopBackOff', 'set up autoscaling in K8s'. Not for provisioning Kubernetes clusters themselves, managing cloud provider control planes, or writing CI/CD pipelines that deploy to K8s |
| [monitoring-setup](skills/devops/monitoring-setup/) | Use this skill when designing or improving observability stacks with Prometheus, Grafana, Loki, Jaeger, or configuring alerting rules and SLIs/SLOs. Not for application code debugging or infrastructure provisioning. Not for log analysis of already-collected logs |

### 🤖 AI/ML

| Skill | Description |
|---|---|
| [dataset-curator](skills/ai-ml/dataset-curator/) | Use this skill when designing, cleaning, deduplicating, or documenting datasets for model training and evaluation including schema design, class imbalance handling, and train/val/test splits. Not for running model training or hyperparameter tuning. Not for real-time data pipeline engineering |
| [eval-designer](skills/ai-ml/eval-designer/) | Use this skill when building evaluation frameworks to measure LLM quality, safety, accuracy, or alignment including test suites, human eval rubrics, automated evals, and metrics design. Not for training or fine-tuning models. Not for dataset curation or benchmark comparison across publicly available models |
| [model-comparator](skills/ai-ml/model-comparator/) | Use this skill when comparing AI or LLM models on benchmarks, capability, cost, latency, context window, or task-specific fit to help teams select the right model for their use case and budget. Not for training or fine-tuning models. Not for building eval frameworks from scratch |
| [prompt-engineer](skills/ai-ml/prompt-engineer/) | Use this skill when crafting, iterating, or optimizing prompts for LLMs including zero-shot, few-shot, chain-of-thought, role prompting, structured output, and prompt chaining. Not for fine-tuning or training models. Not for evaluating model quality across benchmarks |

### 📄 Files

| Skill | Description |
|---|---|
| [docx](skills/files/docx/) | Use this skill when generating, planning, or describing structured Word-compatible documents from outlines, raw content, or templates including heading hierarchy, table structures, and formatting conventions. Not for editing existing DOCX files programmatically. Not for PDF layout or presentation slide design |
| [pdf](skills/files/pdf/) | Use this skill when describing, summarizing, extracting structured data from, or answering questions about PDF documents, or when planning PDF layout and structure for reports, contracts, and publications. Not for editing binary PDF files directly. Not for converting PDFs to other formats programmatically |
| [pptx](skills/files/pptx/) | Use this skill when planning and scripting PowerPoint or Google Slides presentations with slide titles, bullet points, speaker notes, transitions, and narrative flow, or when converting documents into slide decks. Not for designing graphic assets or custom visual themes. Not for video or animation production |
| [xlsx](skills/files/xlsx/) | Use this skill when designing Excel or Google Sheets workbooks with formulas, named ranges, pivot tables, charts, and data validation, or when creating financial models, trackers, and dashboards in spreadsheet format. Not for database design or SQL queries. Not for generating CSV files without workbook structure |

---

## 🚀 How to Use

1. **Browse the table above** and find the skill that matches your task.
2. **Open the `SKILL.md`** in that skill's directory and copy the prompt from the **Instructions** section.
3. **Paste it into Claude** (claude.ai or API), fill in any `{{variables}}`, and go.

---

## 🤝 How to Contribute

We welcome contributions of new skills, improvements to existing ones, and bug fixes!

1. **Read [CONTRIBUTING.md](CONTRIBUTING.md)** for the full process and quality standards.
2. **Fork the repo**, create a branch (`skill/my-new-skill`), and add your `SKILL.md`.
3. **Run the validator**: `python scripts/validate_skills.py` — all checks must pass.
4. **Open a pull request** against `main` with a clear description.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

> **Disclaimer:** Skills in this library are prompts for AI assistance and do not constitute professional legal, financial, or medical advice.
