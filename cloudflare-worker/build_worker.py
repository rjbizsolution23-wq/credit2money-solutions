import os
import json

base_dir = "/Users/kalivibecoding/Downloads/Super-agents266/credit2money-solutions"
worker_dir = os.path.join(base_dir, "cloudflare-worker")

# Read real logo from /tmp/c2m_logo_0.txt
logo_data_url = ""
if os.path.exists("/tmp/c2m_logo_0.txt"):
    with open("/tmp/c2m_logo_0.txt") as lf:
        logo_data_url = lf.read().strip()

routes_map = {
    "/": {
        "title": "C2M Sovereign Operating System — Overview & Index",
        "file": "README.md",
        "category": "Core Hub",
        "icon": "🏛️"
    },
    "/brand": {
        "title": "Official Brand Kit & CROA Compliance Contract",
        "file": "brand/BRAND_SYSTEM.md",
        "category": "Brand & Legal",
        "icon": "🎨"
    },
    "/dispute/manual": {
        "title": "Metro 2® Factual Dispute Strategy Manual",
        "file": "dispute-engine/METRO2_DISPUTE_MANUAL.md",
        "category": "Credit Dispute Suite",
        "icon": "⚖️"
    },
    "/dispute/charge-offs": {
        "title": "Definitive Charge-Off Attack Playbook",
        "file": "dispute-engine/CHARGE_OFF_ATTACK_PLAYBOOK.md",
        "category": "Credit Dispute Suite",
        "icon": "🎯"
    },
    "/dispute/round-1": {
        "title": "Round 1: Factual Dispute Letters (Inquiries & Collections)",
        "file": "dispute-engine/letters/ROUND_1_FACTUAL_DISPUTE.md",
        "category": "Dispute Letters",
        "icon": "📄"
    },
    "/dispute/stall-breaker": {
        "title": "Round 2: Bureau Stall-Breaker Legal Notice (§ 1681i(a)(3))",
        "file": "dispute-engine/letters/ROUND_2_STALL_BREAKER.md",
        "category": "Dispute Letters",
        "icon": "📄"
    },
    "/dispute/mov": {
        "title": "Round 2B: Method of Verification (MOV) Demand (§ 1681i(a)(7))",
        "file": "dispute-engine/letters/ROUND_2B_METHOD_OF_VERIFICATION.md",
        "category": "Dispute Letters",
        "icon": "📄"
    },
    "/dispute/furnisher-623": {
        "title": "Round 3: Direct Furnisher 623 Demand (§ 1681s-2b)",
        "file": "dispute-engine/letters/ROUND_3_FURNISHER_LIABILITY.md",
        "category": "Dispute Letters",
        "icon": "📄"
    },
    "/dispute/secondary-bureaus": {
        "title": "Secondary Bureau Freeze & Clean-Up Directory",
        "file": "dispute-engine/letters/SECONDARY_BUREAU_FREEZE_SWEEP.md",
        "category": "Dispute Letters",
        "icon": "🔒"
    },
    "/dispute/cfpb-ftc": {
        "title": "CFPB & FTC Administrative Complaint Playbooks",
        "file": "dispute-engine/litigation/CFPB_FTC_COMPLAINTS.md",
        "category": "Litigation & Bureau Pressure",
        "icon": "🏛️"
    },
    "/dispute/lawsuit-dossier": {
        "title": "FCRA Lawsuit Dossier & Attorney Referral Playbook",
        "file": "dispute-engine/litigation/FCRA_LAWSUIT_DOSSIER.md",
        "category": "Litigation & Bureau Pressure",
        "icon": "⚖️"
    },
    "/funding/database": {
        "title": "0% APR Business Credit Card & Lender Master Database",
        "file": "funding-matrix/LENDER_DATABASE.json",
        "category": "Funding & Stacking",
        "icon": "💳",
        "is_json": True
    },
    "/funding/stacking-blueprint": {
        "title": "0% APR Credit Card Stacking Sequencing Blueprint (3-Wave)",
        "file": "funding-matrix/STACKING_SEQUENCING_BLUEPRINT.md",
        "category": "Funding & Stacking",
        "icon": "🚀"
    },
    "/funding/pre-underwriting": {
        "title": "Pre-Underwriting & Funding Readiness Checklist",
        "file": "funding-matrix/PRE_UNDERWRITING_CHECKLIST.md",
        "category": "Funding & Stacking",
        "icon": "📋"
    },
    "/funding/grants": {
        "title": "State Grants & Non-Dilutive Capital Directory",
        "file": "funding-matrix/GRANTS_AND_STATE_FUNDING_GUIDE.md",
        "category": "Funding & Stacking",
        "icon": "🏛️"
    },
    "/web-assistant": {
        "title": "Live 24/7 AI Lead Assistant Widget",
        "file": "web-assistant/c2m-chat-widget.html",
        "category": "AI Automation & Web",
        "icon": "🤖",
        "is_html": True
    },
    "/web-assistant/guide": {
        "title": "Web Assistant Installation & Embed Guide",
        "file": "web-assistant/INSTALLATION_GUIDE.md",
        "category": "AI Automation & Web",
        "icon": "🛠️"
    },
    "/social/calendar": {
        "title": "30-Day Social Media Content Calendar",
        "file": "social-autopilot/30_DAY_CONTENT_CALENDAR.md",
        "category": "Social Auto-Pilot",
        "icon": "📅"
    },
    "/social/hooks": {
        "title": "50 Viral Credit & Funding Hooks Vault",
        "file": "social-autopilot/VIRAL_HOOKS_VAULT.md",
        "category": "Social Auto-Pilot",
        "icon": "🪝"
    },
    "/social/auto-poster": {
        "title": "Social Media Auto-Poster Setup Guide",
        "file": "social-autopilot/AUTO_POSTER_SETUP.md",
        "category": "Social Auto-Pilot",
        "icon": "🤖"
    },
    "/video/avatar-setup": {
        "title": "Antoine's AI Digital Twin Setup Guide (HeyGen)",
        "file": "video-avatar-studio/AVATAR_SETUP_HEYGEN_GUIDE.md",
        "category": "Video Avatar & Shorts",
        "icon": "🎬"
    },
    "/video/shorts-tech-stack": {
        "title": "Cinematic Animated Shorts Tech Stack",
        "file": "video-avatar-studio/CINEMATIC_SHORTS_TECH_STACK.md",
        "category": "Video Avatar & Shorts",
        "icon": "🎥"
    },
    "/video/scripts": {
        "title": "10 Word-for-Word Viral Shorts Scripts",
        "file": "video-avatar-studio/10_VIRAL_SHORTS_SCRIPTS.md",
        "category": "Video Avatar & Shorts",
        "icon": "🎙️"
    },
    "/funnel/flash-sale-100": {
        "title": "The $100 Flash Sale Funnel & Sales Copy",
        "file": "sales-funnel/FLASH_SALE_100_OFFER.md",
        "category": "Offer & Sales Funnel",
        "icon": "⚡"
    },
    "/funnel/diy-upsell": {
        "title": "$497 DIY Credit Repair Kit & Upsell Blueprint",
        "file": "sales-funnel/DIY_CREDIT_KIT_UPSELL.md",
        "category": "Offer & Sales Funnel",
        "icon": "📦"
    },
    "/funnel/funding-agreement": {
        "title": "10% Business Capital Consulting Success Fee Agreement",
        "file": "sales-funnel/HIGH_TICKET_FUNDING_CONTRACT.md",
        "category": "Offer & Sales Funnel",
        "icon": "📑"
    },
    "/ai-brain/system-prompt": {
        "title": "C2M Quantum Advisor System Prompt ('Talk-to-Rick' Agent)",
        "file": "c2m-ai-brain/C2M_QUANTUM_ADVISOR_SYSTEM_PROMPT.md",
        "category": "AI Operating System",
        "icon": "🧠"
    },
    "/ai-brain/prompts": {
        "title": "Master Operational Prompts Library",
        "file": "c2m-ai-brain/MASTER_PROMPTS_LIBRARY.md",
        "category": "AI Operating System",
        "icon": "📚"
    }
}

contents = {}
for path, meta in routes_map.items():
    file_path = os.path.join(base_dir, meta["file"])
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    contents[path] = {
        "title": meta["title"],
        "category": meta["category"],
        "icon": meta["icon"],
        "is_json": meta.get("is_json", False),
        "is_html": meta.get("is_html", False),
        "content": data
    }

# Read lender raw json for API
with open(os.path.join(base_dir, "funding-matrix/LENDER_DATABASE.json"), "r") as f:
    lender_raw = json.load(f)

worker_code = f"""// Cloudflare Worker for Credit 2 Money Solutions
// Direct Branding Kit Ingestion from credit2money.org
// Client: Antoine Solomon | credit2money.org | +1 414-399-3277
// Engineered exclusively by Rick Jefferson | RJ Business Solutions

const ROUTES_DATA = {json.dumps(contents)};
const LENDER_RAW_DATA = {json.dumps(lender_raw)};
const LOGO_DATA_URL = {json.dumps(logo_data_url)};

export default {{
  async fetch(request, env, ctx) {{
    const url = new URL(request.url);
    const path = url.pathname.replace(/\\/$/, "") || "/";

    // API Route for raw JSON
    if (path === "/api/lenders") {{
      return new Response(JSON.stringify(LENDER_RAW_DATA, null, 2), {{
        headers: {{
          "content-type": "application/json; charset=utf-8",
          "access-control-allow-origin": "*"
        }}
      }});
    }}

    // Direct standalone HTML view for live web assistant
    if (path === "/web-assistant" && url.searchParams.get("view") === "standalone") {{
      return new Response(ROUTES_DATA["/web-assistant"].content, {{
        headers: {{ "content-type": "text/html; charset=utf-8" }}
      }});
    }}

    const routeInfo = ROUTES_DATA[path];

    if (!routeInfo) {{
      return new Response(renderNotFound(path), {{
        status: 404,
        headers: {{ "content-type": "text/html; charset=utf-8" }}
      }});
    }}

    return new Response(renderPage(path, routeInfo), {{
      headers: {{ "content-type": "text/html; charset=utf-8" }}
    }});
  }}
}};

function renderNavigation(currentPath) {{
  const categories = {{}};
  for (const [p, item] of Object.entries(ROUTES_DATA)) {{
    if (!categories[item.category]) categories[item.category] = [];
    categories[item.category].push({{ path: p, ...item }});
  }}

  let html = '';
  for (const [cat, items] of Object.entries(categories)) {{
    html += `<div class="nav-cat-title">${{cat}}</div><ul class="nav-list">`;
    for (const it of items) {{
      const active = it.path === currentPath ? 'active' : '';
      html += `<li><a href="${{it.path}}" class="nav-link ${{active}}">
        <span class="nav-icon">${{it.icon}}</span>
        <span class="nav-text">${{it.title}}</span>
      </a></li>`;
    }}
    html += '</ul>';
  }}
  return html;
}}

function renderPage(currentPath, routeInfo) {{
  const navHtml = renderNavigation(currentPath);
  let contentHtml = '';

  if (routeInfo.is_html) {{
    contentHtml = `
      <div class="interactive-preview-card">
        <div class="preview-header">
          <h3>⚡ Live Interactive Widget Preview</h3>
          <a href="/web-assistant?view=standalone" target="_blank" class="preview-link">Open Fullscreen ↗</a>
        </div>
        <iframe src="/web-assistant?view=standalone" class="widget-iframe"></iframe>
      </div>
      <div class="code-wrapper" style="margin-top: 24px;">
        <div class="code-header">
          <span>Embed Source Code (c2m-chat-widget.html)</span>
          <button class="btn btn-gold" style="padding: 6px 14px; font-size: 11px;" onclick="copyContent()">Copy Code</button>
        </div>
        <pre><code id="rawContent">${{escapeHtml(routeInfo.content)}}</code></pre>
      </div>
    `;
  }} else if (routeInfo.is_json) {{
    contentHtml = `
      <div class="json-banner">
        <div><strong>REST API Endpoint Available:</strong> GET <code>/api/lenders</code> returns raw JSON for apps & CRMs.</div>
        <a href="/api/lenders" target="_blank" class="btn btn-lime" style="padding: 6px 14px; font-size: 11px;">Test API ↗</a>
      </div>
      <div class="code-wrapper">
        <div class="code-header">
          <span>0% APR Lender Database (JSON)</span>
          <button class="btn btn-gold" style="padding: 6px 14px; font-size: 11px;" onclick="copyContent()">Copy JSON</button>
        </div>
        <pre><code id="rawContent">${{escapeHtml(routeInfo.content)}}</code></pre>
      </div>
    `;
  }} else {{
    contentHtml = `
      <div class="doc-actions">
        <span class="eyebrow"><span>${{routeInfo.category}}</span></span>
        <button class="btn btn-gold" onclick="copyContent()">📋 Copy Full Text</button>
      </div>
      <div id="renderedMarkdown" class="markdown-body"></div>
      <textarea id="rawContent" style="display:none;">${{escapeHtml(routeInfo.content)}}</textarea>
    `;
  }}

  const logoMarkup = LOGO_DATA_URL ? `<img src="${{LOGO_DATA_URL}}" alt="Credit 2 Money" class="brand-img">` : `<span>CREDIT 2 MONEY</span>`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${{routeInfo.title}} | Credit 2 Money Solutions</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,700;0,800;0,900;1,800;1,900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    :root {{
      --bg: #050505;
      --bg2: #0b0b0a;
      --card: #121210;
      --card2: #171713;
      --line: #2a2618;
      --gold: #f7c948;
      --gold2: #d99a0b;
      --gold3: #fff1b0;
      --lime: #8fe03a;
      --lime2: #5fb81c;
      --text: #f5f3ea;
      --muted: #a8a28f;
      --danger: #ff5a4f;
      --gold-grad: linear-gradient(180deg,#fff4c2 0%,#f7c948 38%,#c98a06 70%,#f7c948 100%);
      --chrome-grad: linear-gradient(180deg,#ffffff 0%,#d9d9d9 40%,#8d8d8d 60%,#e8e8e8 100%);
      --lime-grad: linear-gradient(180deg,#b8f56a,#8fe03a 45%,#5fb81c);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', system-ui, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      display: flex;
      min-height: 100vh;
      line-height: 1.55;
    }}

    /* Sidebar */
    .sidebar {{
      width: 320px;
      background: var(--card);
      color: var(--muted);
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--line);
      position: fixed;
      top: 0; bottom: 0; left: 0;
      overflow-y: auto;
      z-index: 100;
    }}
    .sidebar-header {{
      padding: 20px;
      border-bottom: 1px solid var(--line);
      background: var(--bg);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .brand-img {{
      max-height: 52px;
      width: auto;
      display: block;
    }}
    .sidebar-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: "Exo 2";
      font-style: italic;
      font-weight: 800;
      font-size: 10px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--lime);
      padding: 4px 10px;
      border: 1px solid rgba(143,224,58,.35);
      background: rgba(143,224,58,.07);
      border-radius: 4px;
      transform: skewX(-8deg);
      width: fit-content;
    }}
    .sidebar-badge span {{ transform: skewX(8deg); }}
    .sidebar-nav {{
      padding: 16px 12px;
      flex: 1;
    }}
    .nav-cat-title {{
      font-family: "Exo 2", sans-serif;
      font-style: italic;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold);
      font-weight: 800;
      margin: 18px 8px 6px;
    }}
    .nav-list {{ list-style: none; }}
    .nav-link {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      color: var(--muted);
      text-decoration: none;
      font-size: 12.5px;
      border-radius: 6px;
      transition: all 0.15s;
    }}
    .nav-link:hover {{
      background: rgba(247,201,72,0.06);
      color: var(--text);
    }}
    .nav-link.active {{
      background: var(--card2);
      border: 1px solid var(--gold);
      color: var(--gold);
      font-weight: 700;
      box-shadow: 0 0 15px rgba(247,201,72,0.12);
    }}
    .nav-icon {{ font-size: 14px; }}
    .nav-text {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

    /* Main Content */
    .main-wrapper {{
      margin-left: 320px;
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      background: var(--bg);
    }}
    .topbar {{
      height: 68px;
      background: rgba(5,5,5,0.88);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      position: sticky;
      top: 0;
      z-index: 90;
    }}
    .topbar::after {{
      content: "";
      position: absolute;
      left: 0; right: 0; bottom: -1px;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--gold), var(--lime), transparent);
      opacity: 0.7;
    }}
    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .topbar-title {{
      font-family: 'Exo 2', sans-serif;
      font-style: italic;
      font-size: 16px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.2px;
      color: var(--text);
    }}
    .topbar-links {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    /* Buttons — slanted polygon */
    .btn {{
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: "Exo 2", sans-serif;
      font-style: italic;
      font-weight: 900;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 10px 20px;
      border: 0;
      cursor: pointer;
      font-size: 0.85rem;
      clip-path: polygon(8px 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
      transition: transform 0.15s, filter 0.2s;
      text-decoration: none;
    }}
    .btn:hover {{
      transform: translateY(-2px);
      filter: brightness(1.15);
    }}
    .btn-gold {{ background: var(--gold-grad); color: #1a1200; }}
    .btn-lime {{ background: var(--lime-grad); color: #0b1800; }}
    .btn-ghost {{ background: #1b1a15; color: var(--text); border: 1px solid var(--line); }}

    /* Eyebrow badge */
    .eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: "Exo 2";
      font-style: italic;
      font-weight: 800;
      font-size: 0.75rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--lime);
      padding: 6px 14px;
      border: 1px solid rgba(143,224,58,.35);
      background: rgba(143,224,58,.07);
      border-radius: 4px;
      transform: skewX(-8deg);
    }}
    .eyebrow > * {{ transform: skewX(8deg); }}

    .content-container {{
      max-width: 1000px;
      width: 100%;
      margin: 32px auto;
      padding: 0 32px 64px;
    }}
    .doc-card {{
      background: var(--card);
      border-radius: 20px;
      border: 1px solid var(--line);
      box-shadow: 0 20px 60px -20px rgba(0,0,0,0.8), 0 0 0 1px rgba(247,201,72,0.08);
      padding: 40px;
    }}
    .doc-actions {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 28px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--line);
    }}

    /* Markdown styling */
    .markdown-body {{
      font-size: 14.5px;
      line-height: 1.7;
      color: #e2e8f0;
    }}
    .markdown-body h1, .markdown-body h2, .markdown-body h3 {{
      font-family: 'Exo 2', sans-serif;
      font-style: italic;
      text-transform: uppercase;
      color: var(--text);
      margin-top: 32px;
      margin-bottom: 14px;
      font-weight: 900;
      letter-spacing: -0.3px;
    }}
    .markdown-body h1 {{
      font-size: 28px;
      border-bottom: 1px solid var(--line);
      padding-bottom: 10px;
      background: var(--gold-grad);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }}
    .markdown-body h2 {{ font-size: 22px; color: var(--gold); }}
    .markdown-body h3 {{ font-size: 18px; color: var(--lime); }}
    .markdown-body p {{ margin-bottom: 16px; color: #cbd5e1; }}
    .markdown-body ul, .markdown-body ol {{ margin-left: 24px; margin-bottom: 16px; }}
    .markdown-body li {{ margin-bottom: 6px; color: #cbd5e1; }}
    .markdown-body blockquote {{
      border-left: 4px solid var(--gold);
      padding: 14px 20px;
      background: var(--card2);
      color: var(--muted);
      margin: 20px 0;
      border-radius: 0 10px 10px 0;
      border: 1px solid var(--line);
      border-left: 4px solid var(--gold);
    }}
    .markdown-body table {{
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
      font-size: 13.5px;
    }}
    .markdown-body th, .markdown-body td {{
      padding: 12px 14px;
      border: 1px solid var(--line);
      text-align: left;
    }}
    .markdown-body th {{
      background: var(--card2);
      font-family: 'Exo 2', sans-serif;
      font-style: italic;
      font-weight: 800;
      color: var(--gold);
      text-transform: uppercase;
    }}
    .markdown-body tr:nth-child(even) {{
      background: rgba(255,255,255,0.015);
    }}
    .markdown-body pre {{
      background: var(--bg2);
      color: #f1f5f9;
      padding: 18px;
      border-radius: 10px;
      overflow-x: auto;
      font-family: ui-monospace, Menlo, monospace;
      font-size: 13px;
      margin: 20px 0;
      border: 1px solid var(--line);
    }}
    .markdown-body code {{
      background: var(--card2);
      border: 1px solid var(--line);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: ui-monospace, Menlo, monospace;
      font-size: 13px;
      color: var(--gold);
    }}
    .markdown-body pre code {{
      background: transparent;
      border: none;
      padding: 0;
      color: inherit;
    }}

    /* Code Wrapper */
    .code-wrapper {{
      border: 1px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      background: var(--bg2);
    }}
    .code-header {{
      background: var(--card2);
      color: var(--muted);
      padding: 12px 18px;
      font-size: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'Exo 2', sans-serif;
      font-style: italic;
      font-weight: 800;
      text-transform: uppercase;
      border-bottom: 1px solid var(--line);
    }}
    .code-wrapper pre {{
      padding: 18px;
      margin: 0;
      overflow-x: auto;
      color: #e2e8f0;
      font-family: ui-monospace, Menlo, monospace;
      font-size: 13px;
      line-height: 1.5;
    }}

    /* Interactive Preview Card */
    .interactive-preview-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 16px;
      overflow: hidden;
    }}
    .preview-header {{
      padding: 14px 20px;
      background: var(--card2);
      border-bottom: 1px solid var(--line);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .preview-header h3 {{
      font-size: 14px;
      font-weight: 900;
      color: var(--gold);
      font-family: 'Exo 2', sans-serif;
      font-style: italic;
      text-transform: uppercase;
    }}
    .preview-link {{
      font-size: 12px;
      font-weight: 700;
      color: var(--lime);
      text-decoration: none;
      font-family: 'Exo 2', sans-serif;
      font-style: italic;
      text-transform: uppercase;
    }}
    .widget-iframe {{
      width: 100%;
      height: 700px;
      border: none;
      display: block;
      background: var(--bg);
    }}

    /* JSON Banner */
    .json-banner {{
      background: rgba(143,224,58,0.06);
      border: 1px solid rgba(143,224,58,0.3);
      color: var(--lime);
      padding: 16px 20px;
      border-radius: 10px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13.5px;
    }}

    /* Footer Legal */
    .doc-footer {{
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--line);
      font-size: 11px;
      color: var(--muted);
      text-align: center;
      line-height: 1.6;
    }}

    /* Responsive */
    @media (max-width: 900px) {{
      .sidebar {{ display: none; }}
      .main-wrapper {{ margin-left: 0; }}
      .content-container {{ padding: 0 16px 32px; }}
    }}
  </style>
</head>
<body>
  <!-- Sidebar Navigation -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="brand-wrap">
        ${{logoMarkup}}
      </div>
      <div class="sidebar-badge"><span>Sovereign Suite</span></div>
    </div>
    <div class="sidebar-nav">
      ${{navHtml}}
    </div>
  </aside>

  <!-- Main View -->
  <div class="main-wrapper">
    <header class="topbar">
      <div class="topbar-left">
        <span class="topbar-title">${{routeInfo.icon}} ${{routeInfo.title}}</span>
      </div>
      <div class="topbar-links">
        <a href="https://credit2money.org" target="_blank" class="btn btn-ghost" style="padding:6px 12px; font-size:11px;">credit2money.org ↗</a>
        <a href="https://app.myfreescorenow.com/enroll/B02C6182" target="_blank" class="btn btn-lime" style="padding:6px 12px; font-size:11px;">Credit Report ↗</a>
        <a href="/" class="btn btn-gold" style="padding:6px 12px; font-size:11px;">Master Hub</a>
      </div>
    </header>

    <main class="content-container">
      <div class="doc-card">
        ${{contentHtml}}
        <div class="doc-footer">
          <strong>Credit 2 Money Solutions INC.</strong> · credit2money.org · mail@credit2money.org · +1 (414) 399-3277<br>
          Credit 2 Money Solutions INC. does not guarantee any specific credit score increase, removal of any item from your credit report, or approval for any loan, credit card or funding product. CROA Compliant.
        </div>
      </div>
    </main>
  </div>

  <script>
    const rawEl = document.getElementById('rawContent');
    const mdEl = document.getElementById('renderedMarkdown');
    if (rawEl && mdEl) {{
      mdEl.innerHTML = marked.parse(rawEl.value || rawEl.innerText);
    }}

    function copyContent() {{
      const el = document.getElementById('rawContent');
      const text = el.value || el.innerText;
      navigator.clipboard.writeText(text).then(() => {{
        alert('Copied to clipboard successfully!');
      }});
    }}
  </script>
</body>
</html>`;
}}

function renderNotFound(path) {{
  return `<!DOCTYPE html>
<html>
<head><title>404 Not Found</title></head>
<body style="background:#050505; color:#f5f3ea; font-family:sans-serif; text-align:center; padding:60px;">
  <h1 style="color:#f7c948;">404 — Route Not Found</h1>
  <p>The requested route <code>${{path}}</code> does not exist.</p>
  <p><a href="/" style="color:#8fe03a; font-weight:bold;">Return to Credit 2 Money Solutions Hub</a></p>
</body>
</html>`;
}}

function escapeHtml(text) {{
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}}
"""

with open(os.path.join(worker_dir, "src/index.js"), "w", encoding="utf-8") as f:
    f.write(worker_code)

print("Worker regenerated with live credit2money.org branding kit!")
