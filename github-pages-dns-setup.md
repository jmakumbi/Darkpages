# GitHub Pages Setup — billableonline.co
## Dark Pages Vault — DNS, Domain & Email Safety Guide

---

## Before You Touch Anything

Log into wherever your domain is managed and **screenshot your current DNS records**
before making any changes. You're looking for the full DNS table.

To find out if it's Cloudflare or GoDaddy:
1. Go to https://lookup.icann.org and search `billableonline.co`
2. Look at the **Name Servers** field in the results
3. If you see `*.ns.cloudflare.com` → it's Cloudflare
4. If you see `*.domaincontrol.com` → it's GoDaddy

---

## Part 1 — GitHub Repository Setup

### 1.1 Create the Repo

1. Go to github.com → New repository
2. Name it: `billableonline` (or `billableonline.co` — either works)
3. Set it to **Public** ← required for GitHub Pages on free accounts
4. Do NOT initialise with a README (the scaffold prompt handles this)
5. Create the repo

### 1.2 Push Your Local Project

After running the scaffold in Claude Code:

```bash
cd billableonline
git remote add origin https://github.com/YOUR-USERNAME/billableonline.git
git add .
git commit -m "Initial scaffold"
git push -u origin main
```

### 1.3 Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. Under **Source**: select **Deploy from a branch**
3. Branch: `gh-pages` / folder: `/ (root)`
4. Click **Save**

> Note: The `gh-pages` branch won't exist yet until GitHub Actions runs for
> the first time. Push your code first, let the Action complete, then come back
> and set this.

### 1.4 Add Your Custom Domain in GitHub

1. Still in Settings → Pages
2. Under **Custom domain**: type `billableonline.co`
3. Click **Save**
4. Leave **Enforce HTTPS** unchecked for now — tick it after DNS propagates

GitHub will create a `CNAME` file in your `gh-pages` branch automatically.
Your `static/CNAME` file in the Hugo project also handles this — either works,
having both is fine.

---

## Part 2 — DNS Configuration

### ⚠️ The Email Safety Rule

Your `james@billableonline.co` alias works because of **MX records** pointing to
Microsoft's mail servers. You must **never delete or modify the MX records**.

The changes below only touch **A records** and optionally a **CNAME for www**.
MX records are left completely alone.

---

### 2A — If Your DNS is on Cloudflare

Log into dash.cloudflare.com → select `billableonline.co` → **DNS** tab.

**Add these 4 A records:**

| Type | Name | Content | Proxy status | TTL |
|------|------|---------|--------------|-----|
| A | `@` | `185.199.108.153` | **DNS only** (grey cloud) | Auto |
| A | `@` | `185.199.109.153` | **DNS only** (grey cloud) | Auto |
| A | `@` | `185.199.110.153` | **DNS only** (grey cloud) | Auto |
| A | `@` | `185.199.111.153` | **DNS only** (grey cloud) | Auto |

**Critical — Proxy must be OFF (grey cloud, not orange):**
GitHub Pages handles HTTPS itself. If Cloudflare proxies the traffic (orange cloud),
GitHub's HTTPS certificate provisioning breaks. Set all four A records to DNS only.

**Optional — www redirect:**

| Type | Name | Content | Proxy | TTL |
|------|------|---------|-------|-----|
| CNAME | `www` | `YOUR-USERNAME.github.io` | DNS only | Auto |

**Do not touch:**
- Any records with type `MX`
- Any records with type `TXT` that contain `v=spf1` (SPF for email)
- Any records with type `TXT` that contain `DKIM` or `_domainkey`

---

### 2B — If Your DNS is on GoDaddy

Log into godaddy.com → **My Products** → find `billableonline.co` → **DNS**.

**Add these 4 A records:**

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | `@` | `185.199.108.153` | 1 Hour |
| A | `@` | `185.199.109.153` | 1 Hour |
| A | `@` | `185.199.110.153` | 1 Hour |
| A | `@` | `185.199.111.153` | 1 Hour |

GoDaddy may already have an A record pointing `@` to their own parking page.
**Delete that one first**, then add the four GitHub IPs.

**Optional — www:**

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | `www` | `YOUR-USERNAME.github.io` | 1 Hour |

**Do not touch:**
- Any `MX` records (these route james@billableonline.co to Microsoft)
- Any `TXT` records starting with `v=spf1`
- Any `TXT` records containing `MS=` (Microsoft domain verification)

---

## Part 3 — Email Alias Safety Check

Your `james@billableonline.co` alias is on Outlook.com's custom domain feature
(the legacy free tier Microsoft discontinued). It works via MX records pointing
to Microsoft's servers.

### What keeps it working:

| Record type | What it does | Touch it? |
|-------------|--------------|-----------|
| MX | Routes email to Microsoft | **Never** |
| TXT (SPF) | Tells senders Microsoft is authorised | **Never** |
| TXT (MS=...) | Proves you own the domain to Microsoft | **Never** |
| A (`@`) | Routes web traffic to GitHub Pages | ✅ This is what you change |

### Quick sanity check after DNS changes:

Send a test email to `james@billableonline.co` from another account.
If it arrives, email is intact. If it bounces, you accidentally touched an MX record —
go back and restore from your screenshot.

---

## Part 4 — HTTPS Certificate

After DNS propagates (up to 48 hours, usually under 2):

1. Go back to GitHub → Settings → Pages
2. The **Custom domain** field should show a green tick: *"DNS check successful"*
3. Tick **Enforce HTTPS**
4. GitHub will provision a Let's Encrypt certificate automatically
5. Wait ~15 minutes, then visit `https://billableonline.co`

You should see the Members Only gate page over HTTPS.

---

## Part 5 — Verify Everything is Working

Run these checks in order:

```bash
# 1. Confirm A records are resolving to GitHub
dig billableonline.co A +short
# Should return the 4 GitHub IPs

# 2. Confirm MX records are untouched
dig billableonline.co MX +short
# Should still return Microsoft mail servers (outlook.com / protection.outlook.com)

# 3. Test the site
curl -I https://billableonline.co
# Should return HTTP/2 200 and a GitHub Pages server header
```

Or use the web equivalent at https://dnschecker.org — search `billableonline.co`
and check A records vs MX records separately.

---

## Part 6 — Ongoing Workflow

Once everything is live, deploying changes is:

```bash
# Make changes to content or layouts
git add .
git commit -m "Add new page: your-slug"
git push origin main
# GitHub Actions builds and deploys automatically — ~60 seconds
```

Monitor deployments at:
`https://github.com/YOUR-USERNAME/billableonline/actions`

---

## Summary Checklist

### One-time setup
- [ ] Screenshot existing DNS records before touching anything
- [ ] Create GitHub repo (Public)
- [ ] Run scaffold prompt in Claude Code
- [ ] Push to `main`
- [ ] Wait for GitHub Actions to complete and create `gh-pages` branch
- [ ] Enable Pages in repo Settings → Pages, set source to `gh-pages`
- [ ] Add custom domain `billableonline.co` in Pages settings
- [ ] Add 4 GitHub A records in DNS panel (Cloudflare: grey cloud / GoDaddy: as-is)
- [ ] Do NOT touch MX, SPF, or MS= TXT records
- [ ] Wait for DNS propagation
- [ ] Enforce HTTPS in Pages settings
- [ ] Verify `https://billableonline.co` loads the gate page
- [ ] Send test email to `james@billableonline.co` to confirm alias still works

### Each new page
- [ ] New Claude Code chat using the page-building-guide brief format
- [ ] Commit and push to `main`
- [ ] Actions deploys in ~60 seconds
- [ ] Share the URL directly — `https://billableonline.co/your-slug/`
