from html import escape
from pathlib import Path
import re

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse


router = APIRouter(prefix="/documentation", tags=["documentation"])

DOCS_ROOT = Path(__file__).resolve().parents[4] / "docs"
PROJECT_ROOT = Path(__file__).resolve().parents[4]
LOGO_URL = "/assets/egestIcon.png"

NAVIGATION = (
    ("Accueil", "index.md"),
    ("Vision", "vision.md"),
    ("Architecture", "architecture.md"),
    ("Installation", "installation.md"),
    ("API backend", "api.md"),
    ("Base de donnees", "database.md"),
    ("Frontend", "frontend.md"),
    ("Modules", "modules.md"),
    ("Securite", "security.md"),
    ("Roadmap", "roadmap.md"),
)


def _resolve_document(document_path: str) -> Path:
    clean_path = document_path.strip("/") or "index.md"
    if not clean_path.endswith(".md"):
        clean_path = f"{clean_path}.md"

    resolved_path = (DOCS_ROOT / clean_path).resolve()

    if DOCS_ROOT.resolve() not in resolved_path.parents and resolved_path != DOCS_ROOT.resolve():
        raise HTTPException(status_code=404, detail="Document introuvable")

    if not resolved_path.is_file():
        raise HTTPException(status_code=404, detail="Document introuvable")

    return resolved_path


def _markdown_links_to_routes(line: str, current_dir: Path) -> str:
    def replace_link(match: re.Match[str]) -> str:
        label = escape(match.group(1))
        target = match.group(2)

        if target.startswith(("http://", "https://", "#")):
            href = escape(target)
        elif target.endswith(".md"):
            route_path = (current_dir / target).as_posix()
            href = f"/documentation/{escape(route_path)}"
        elif target.endswith("/"):
            route_path = (current_dir / target / "index.md").as_posix()
            href = f"/documentation/{escape(route_path)}"
        else:
            href = escape(target)

        return f'<a href="{href}">{label}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, escape(line))


def _render_markdown(markdown: str, relative_dir: Path) -> str:
    html_lines: list[str] = []
    in_code_block = False
    in_list = False

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("</code></pre>" if in_code_block else "<pre><code>")
            in_code_block = not in_code_block
            continue

        if in_code_block:
            html_lines.append(escape(line))
            continue

        if not line:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            continue

        heading_level = len(line) - len(line.lstrip("#"))
        if 1 <= heading_level <= 6 and line[heading_level : heading_level + 1] == " ":
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            content = _markdown_links_to_routes(line[heading_level + 1 :], relative_dir)
            html_lines.append(f"<h{heading_level}>{content}</h{heading_level}>")
            continue

        if line.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            content = _markdown_links_to_routes(line[2:], relative_dir)
            html_lines.append(f"<li>{content}</li>")
            continue

        if in_list:
            html_lines.append("</ul>")
            in_list = False

        content = _markdown_links_to_routes(line, relative_dir)
        html_lines.append(f"<p>{content}</p>")

    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)


def _navigation(active_path: str) -> str:
    links = []
    for label, path in NAVIGATION:
        active_class = "active" if path == active_path else ""
        href = "/documentation" if path == "index.md" else f"/documentation/{path}"
        links.append(f'<a class="{active_class}" href="{href}">{escape(label)}</a>')

    return "\n".join(links)


def _layout(title: str, body: str, active_path: str) -> str:
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} - EGest</title>
  <style>
    :root {{
      --bg: #f3f6fb;
      --panel: #ffffff;
      --text: #1f2937;
      --muted: #667085;
      --line: #d9e2ec;
      --brand: #1f5f8b;
      --brand-dark: #173f5f;
      --accent: #2f80ed;
      --code-bg: #202938;
      --code-text: #f8fafc;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      color: var(--text);
      font-family: "Segoe UI", Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      background: var(--bg);
    }}
    .topbar {{
      background: var(--brand-dark);
      border-bottom: 4px solid var(--accent);
      color: #ffffff;
    }}
    .topbar-inner {{
      align-items: center;
      display: flex;
      gap: 16px;
      max-width: 1180px;
      margin: 0 auto;
      padding: 18px 24px;
    }}
    .logo {{
      background: #ffffff;
      border-radius: 8px;
      height: 48px;
      padding: 6px;
      width: 48px;
    }}
    .brand-title {{
      font-size: 24px;
      font-weight: 700;
      line-height: 1.2;
      margin: 0;
    }}
    .brand-subtitle {{
      color: #d6e6f5;
      font-size: 14px;
      margin: 2px 0 0;
    }}
    .shell {{
      display: grid;
      grid-template-columns: 260px minmax(0, 1fr);
      gap: 28px;
      max-width: 1180px;
      margin: 0 auto;
      padding: 28px 24px 56px;
    }}
    aside {{
      align-self: start;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      position: sticky;
      top: 20px;
    }}
    aside h2 {{
      color: var(--brand-dark);
      font-size: 13px;
      letter-spacing: .08em;
      margin: 0 0 12px;
      text-transform: uppercase;
    }}
    nav a {{
      border-radius: 6px;
      color: #344054;
      display: block;
      font-size: 15px;
      margin: 2px 0;
      padding: 8px 10px;
      text-decoration: none;
    }}
    nav a:hover {{
      background: #eef5fc;
      color: var(--brand);
    }}
    nav a.active {{
      background: var(--brand);
      color: #ffffff;
      font-weight: 600;
    }}
    main {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      min-width: 0;
      padding: 34px 42px 52px;
    }}
    .quick-links {{
      border-bottom: 1px solid var(--line);
      color: var(--muted);
      font-size: 14px;
      margin: -10px 0 28px;
      padding-bottom: 16px;
    }}
    a {{
      color: var(--accent);
      text-decoration-thickness: 1px;
      text-underline-offset: 3px;
    }}
    h1 {{
      color: var(--brand-dark);
      font-size: 34px;
      margin: 0 0 18px;
    }}
    h2 {{
      border-top: 1px solid var(--line);
      color: var(--brand-dark);
      font-size: 24px;
      margin: 34px 0 12px;
      padding-top: 24px;
    }}
    h3 {{
      color: var(--brand);
      font-size: 19px;
      margin: 24px 0 8px;
    }}
    p, li {{
      font-size: 16px;
    }}
    ul {{
      padding-left: 24px;
    }}
    pre {{
      overflow-x: auto;
      padding: 16px;
      background: var(--code-bg);
      color: var(--code-text);
      border-radius: 6px;
    }}
    code {{
      font-family: Consolas, "Courier New", monospace;
      font-size: 14px;
    }}
    p code, li code {{
      background: #eef2f7;
      border-radius: 4px;
      color: #1d4ed8;
      padding: 2px 5px;
    }}
    @media (max-width: 820px) {{
      .topbar-inner {{
        padding: 16px;
      }}
      .shell {{
        display: block;
        padding: 16px;
      }}
      aside {{
        margin-bottom: 16px;
        position: static;
      }}
      main {{
        padding: 24px 20px 38px;
      }}
      h1 {{
        font-size: 28px;
      }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <img class="logo" src="{LOGO_URL}" alt="Logo EGest">
      <div>
        <p class="brand-title">Documentation EGest</p>
        <p class="brand-subtitle">Application de gestion scolaire avec FastAPI et PySide6</p>
      </div>
    </div>
  </header>
  <div class="shell">
    <aside>
      <h2>Sommaire</h2>
      <nav>
        {_navigation(active_path)}
      </nav>
    </aside>
    <main>
      <p class="quick-links"><a href="/documentation">Accueil documentation</a> | <a href="/docs">Swagger API</a></p>
      {body}
    </main>
  </div>
</body>
</html>"""


@router.get("", response_class=HTMLResponse)
async def documentation_index() -> HTMLResponse:
    return await documentation_page("index.md")


@router.get("/{document_path:path}", response_class=HTMLResponse)
async def documentation_page(document_path: str) -> HTMLResponse:
    document = _resolve_document(document_path)
    relative_path = document.relative_to(DOCS_ROOT)
    markdown = document.read_text(encoding="utf-8")
    body = _render_markdown(markdown, relative_path.parent)
    return HTMLResponse(_layout(relative_path.as_posix(), body, relative_path.as_posix()))
