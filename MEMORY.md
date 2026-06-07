# Memory.md — Long-Term Memory

---

## SEO & Website Infrastructure — DEPLOYED (2026-06-08)

### YTT Portugal (Enhanced E-E-A-T)
- **Live Preview:** https://9a248895.teachertrainingportugal.pages.dev
- **Enhanced homepage** with instructor bios, trust signals, location depth, FAQ schema, testimonials
- **Course Schema** with AggregateRating (4.9/12)
- **Organization Schema** with sameAs links to heatlagos.com + Instagram
- **FAQ Schema** markup for Google rich snippets
- **Blog post:** "Cost of Yoga Teacher Training Portugal" (high-volume keyword)
- **Canonical URLs, Open Graph, sitemap, robots.txt** all in place
- **Status:** Needs production domain deployment + real photos + remaining blog posts

### Heat Lagos (New Luxury Site)
- **Live Preview:** https://dda90e47.heatlagos.pages.dev
- **Homepage** with luxury positioning, LocalBusiness schema, NAP
- **3 dedicated modality pages** (each with unique Schema):
  - `/infrared-hot-yoga-lagos` — Infrared Hot Yoga Lagos
  - `/mat-pilates-lagos` — Mat Pilates Lagos (no reformers)
  - `/pilates-sculpt-lagos` — Pilates Sculpt Lagos
- **Science section** explaining 30-32°C infrared vs 40°C Bikram
- **Pricing:** Drop-in €22, Vacation Week €59, Intro €79
- **Status:** Needs production domain + real photos + Google Business Profile claim

### Review System Templates
- **4 templates:** In-person ask, WhatsApp follow-up, YTT graduate email, tourist follow-up
- **Response strategy:** Reply to every review with woven keywords
- **Tracking spreadsheet** format included

### B2B Outreach Templates
- **3 templates:** Hotel concierge, surf school, restaurant/wellness
- **3-touch follow-up sequence:** Day 1, Day 5, Day 12
- **Value exchange:** Free 10-class pack for owners, 20-25% staff discount, €15 guest rate
- **Backlink requirements:** "dofollow" links with keyword-rich anchor text

### Repo
- All files pushed to `github.com/sebastianbrosche/miha`
- Includes: `seo-implementation-masterplan.md`, `review-system-templates.md`, `b2b-outreach-templates.md`

---

## Elastomania/Across Mod System — DEFERRED (2026-06-04)
**Status:** User said "save it for later" — not building now, logged for future activation.
**Spec:** Full spec file at `downloads/19e8f63a-3e12-88b9-8000-0000bf9b6daa_elasto_ai_agent_spec.md`
**What it is:** Fork Across repo, add child-friendly visual skin/mod layer (decoupled from physics), image upload for rider/bike skins, preserve deterministic replay.
**What I can do:** Fork, build skin system, set up GitHub repo, write Windows installer (Inno/NSIS). Build CI for `.exe` via GitHub Actions since I'm on Linux.

---

## Dual OpenClaw Instance Setup — PREFERRED (2026-06-04)
**User choice:** Option C — Browser Relay with two Chrome profiles
**Status:** Ready to deploy tomorrow (new computer migration)
**Goal:** Two independent gateway instances (18789 + 18790), each with own Chrome + Browser Relay, controlled entirely via Telegram (no monitor needed)
**Architecture:**
- Instance 1: Default port 18789, default workspace, existing Telegram bot
- Instance 2: Port 18790, separate workspace (`OPENCLAW_HOME=/root/.openclaw-instance2`), NEW Telegram bot token needed
- Chrome Profile 1: Browser Relay → ws://127.0.0.1:18789
- Chrome Profile 2: Browser Relay → ws://127.0.0.1:18790
- Both autostart on boot via systemd/crontab
**Next step:** Create second Telegram bot token via @BotFather, then deploy after new computer arrives
**Note:** User has a new computer coming tomorrow — migrate this setup there

---

## claude-mem + context — INSTALLED (2026-06-05)
**claude-mem** (persistent memory plugin) installed and enabled in OpenClaw. Worker running on port 37777 with OpenRouter provider. Gateway restart pending to fully activate.
**neuledge/context** (MCP docs server) installed globally at `/usr/bin/context` v1.1.0. React docs tested and working. Available to all subagents via shell commands.
## Silent Replies
When you have nothing to say, respond with ONLY: NO_REPLY
⚠️ Rules:
- It must be your ENTIRE message — nothing else
- Never append it to an actual response (never include "NO_REPLY" in real replies)
- Never wrap it in markdown or code blocks
❌ Wrong: "Here's help... NO_REPLY"
❌ Wrong: "NO_REPLY"
✅ Right: NO_REPLY
