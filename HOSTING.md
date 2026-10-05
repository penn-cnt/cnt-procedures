# Hosting the manual

The manual is public at **https://cnt-manual.neurobridge.link**, served from AWS (S3 + CloudFront,
set up from `infra/terraform/`). The repository and the site are linked both ways:

- **Edit on the site → commit on GitHub.** Every page has a pencil icon. It opens that page's file in
  GitHub's web editor; *Commit changes* saves it to the repository (or proposes it as a pull request
  for people without write access).
- **Commit on GitHub → site updates.** Every push to `main` runs *Publish site
  (cnt-manual.neurobridge.link)* (`.github/workflows/deploy-aws.yml`): content check, build, upload
  to S3, CloudFront refresh. The site changes about two minutes after the commit. If the content
  check finds a password or identifier, nothing is published and the previous version stays up.

```
pencil on a page → GitHub editor → commit to main → Actions builds → S3 + CloudFront → cnt-manual.neurobridge.link
```

## Connecting GitHub to AWS (once)

The workflow signs in to AWS with GitHub's OIDC token and the IAM role Terraform created; no keys are
stored anywhere. It needs three repository **variables** (Settings → Secrets and variables → Actions →
*Variables* tab → New repository variable), whose values come from `terraform output` in CloudShell
(`cd ~/cnt-procedures/infra/terraform && TF_DATA_DIR=/tmp/tfdata terraform output`):

| Variable | Value |
|---|---|
| `AWS_ROLE_ARN` | `AWS_ROLE_ARN` output |
| `S3_BUCKET` | `S3_BUCKET` output |
| `CLOUDFRONT_DISTRIBUTION_ID` | `CLOUDFRONT_DISTRIBUTION_ID` output |

Until they are set, the publish job is skipped. To publish by hand from CloudShell instead:
`git pull && uv run --frozen mkdocs build && aws s3 sync site/ s3://<S3_BUCKET> --delete` then
`aws cloudfront create-invalidation --distribution-id <ID> --paths "/*"`.

## Domain

`cnt-manual.neurobridge.link` is a CNAME at Hostinger (neurobridge.link DNS) pointing to the CloudFront
distribution, with an ACM certificate validated by a second CNAME. Do not delete either record. The
domain is the NeuroBridge Lab's and renews automatically.

---

The AWS and Cloudflare options below are kept for reference, in case the manual ever needs to be private again.


Two ways are written down here. **AWS (S3 + CloudFront)** is the one chosen: it runs in the CNT's
AWS @ Penn account and is built from `infra/terraform/` and `.github/workflows/deploy-aws.yml`.
**Cloudflare Pages + Access**, further down, is the quicker fallback. Either way nobody installs
anything to read or edit: readers use the website, editors use the pencil icon on any page, which
opens GitHub's web editor, and every commit to `main` republishes the site.

```
edit on GitHub (pencil) → commit → GitHub Actions builds and uploads → CloudFront serves it
```

## AWS: one-time setup (about 30 minutes, all in the browser)

What gets created: a private S3 bucket, a CloudFront distribution in front of it (HTTPS; the bucket
is reachable only through CloudFront), a small CloudFront function that maps `/page/` to
`/page/index.html`, and an IAM role that GitHub Actions assumes with OIDC, so no access keys are
ever created or pasted anywhere. Cost: well under $5/month at this size (plus about $6/month if the
IP allowlist below is turned on).

**Decide who can read it before step 4.** S3 + CloudFront on its own is a *public* website: anyone
with the address can read it, and the manual still contains staff names and some phone numbers.
Before publishing, either (a) set `allowed_cidrs` to Penn's campus and VPN address ranges (ask Penn
ISC), so only people on the Penn network or VPN can open it; (b) add a PennKey login (Cognito
federated with Penn WebLogin, which needs a registration with Penn ISC Identity); or (c) clean the
content so it is fit to be public. Until then, leave the GitHub variables unset and the deploy job
stays off.

1. **Sign in.** Go to https://aws.cloud.upenn.edu, sign in with PennKey, and open the CNT account
   with a role that can create S3, CloudFront, WAF and IAM resources.
2. **Open CloudShell** (the `>_` icon in the top bar of the AWS console): a terminal in the browser,
   nothing installed on your computer. Install Terraform there once:
   ```bash
   curl -sSLo tf.zip https://releases.hashicorp.com/terraform/1.9.8/terraform_1.9.8_linux_amd64.zip
   mkdir -p ~/bin && unzip -oq tf.zip -d ~/bin && export PATH=~/bin:$PATH && terraform version
   ```
3. **Bring the Terraform files.** On GitHub, open this repository → Code → Download ZIP. In
   CloudShell: Actions → Upload file → the ZIP, then:
   ```bash
   unzip -q cnt-procedures-main.zip && cd cnt-procedures-main/infra/terraform
   cp example.tfvars terraform.tfvars    # edit with nano if you set a domain or IP ranges
   ```
4. **Create everything.**
   ```bash
   terraform init
   terraform apply            # review the plan, type yes
   ```
   If it fails because the GitHub OIDC provider already exists in the account, set
   `create_github_oidc_provider = false` in `terraform.tfvars` and apply again. Keep the folder
   (CloudShell keeps your home directory): `terraform.tfstate` there is the record of what was
   created. To share it with a colleague, move it to an S3 backend (see `providers.tf`).
5. **Connect GitHub.** `terraform output` prints three values. In GitHub → this repository →
   Settings → Secrets and variables → Actions → **Variables** tab, add `AWS_ROLE_ARN`, `S3_BUCKET`
   and `CLOUDFRONT_DISTRIBUTION_ID`. They are identifiers, not secrets.
6. **Publish.** GitHub → Actions → *Deploy site to AWS* → Run workflow. About two minutes later the
   site is at `site_url`. From then on every commit to `main` republishes it.

### Custom domain (optional, e.g. `cnt.neurobridge.link`)

1. In AWS Certificate Manager, **in us-east-1**, request a public certificate for the domain with DNS
   validation; add the CNAME it shows at the domain's DNS provider (Hostinger) and wait for *Issued*.
2. Put `domain_name` and `acm_certificate_arn` in `terraform.tfvars` and run `terraform apply`.
3. At the DNS provider, add a CNAME from `cnt` to the `cloudfront_domain` output.

### Day to day (AWS)

- Readers open the address. Editors need a GitHub account with access to the repository, then the pencil.
- A failed build (for example the content check finding a password) stops the upload and leaves the
  previous version online; the log is under GitHub → Actions.
- To take the site down: `terraform destroy` in the same CloudShell folder.

---

## Alternative: Cloudflare Pages + Access

The manual is published as a private website with **Cloudflare Pages** (builds the site from this
repository after every commit) and **Cloudflare Access** (lets in only people with a Penn email).
Both are free for up to 50 users. Nobody needs to install anything: readers use the website,
editors use the pencil icon on any page, which opens GitHub's web editor.

```
edit on GitHub (pencil) → commit → Cloudflare rebuilds (~1–2 min) → readers sign in with a Penn email
```

### One-time setup (about 15 minutes)

You need: a penn-cnt GitHub **owner** (to approve the Cloudflare app) and a Cloudflare account
(free; create it with a shared CNT email so it does not belong to one person).

#### 1. Connect the repository

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
2. Choose GitHub, install the Cloudflare app on the **penn-cnt** organisation, and give it access to
   **cnt-procedures** only.
3. Build settings:

   | Setting | Value |
   |---|---|
   | Project name | `cnt-procedures` (the site becomes `cnt-procedures.pages.dev`) |
   | Production branch | `main` |
   | Framework preset | None |
   | Build command | `pip install uv && uv run --frozen mkdocs build` |
   | Build output directory | `site` |
   | Environment variable | `PYTHON_VERSION` = `3.12` |

4. **Save and Deploy.** The first build takes a few minutes. Do not share the URL yet.

#### 2. Put a login in front of it

1. Cloudflare dashboard → **Zero Trust** (choose the Free plan if asked; it needs a card on file
   but is not charged for up to 50 users).
2. **Settings → Authentication → Login methods**: make sure **One-time PIN** is enabled.
3. **Access → Applications → Add an application → Self-hosted.**
   - Application domain: `cnt-procedures.pages.dev`; add a second domain `*.cnt-procedures.pages.dev`
     so preview builds are protected too.
   - Session duration: 1 month.
4. Add a policy: **Action** Allow; **Include** → *Emails ending in* → `@upenn.edu`,
   `@pennmedicine.upenn.edu`, `@seas.upenn.edu` (add `@chop.edu` if CHOP collaborators need it).
   For a tighter list, use *Emails* and name people one by one.
5. Save. Open the site in a private window: you should see a Cloudflare login page asking for an
   email, then a code sent to that inbox.

#### 3. Tell people

Readers: open the site, enter your Penn email, type the code. Editors: you also need a GitHub
account added to the **cnt-procedures** repository; then use the pencil on any page.

### Day to day (Cloudflare)

- Every commit to `main` rebuilds the site. Build logs are under Workers & Pages → cnt-procedures →
  Deployments; a failed build leaves the previous version online.
- To add or remove readers, edit the Access policy. To add or remove editors, change the repository's
  collaborators on GitHub.
- If the user count passes 50, Cloudflare Zero Trust moves to a paid tier; Penn web hosting behind
  PennKey is the alternative.

## Linked from the NeuroBridge wiki

Once the site is live, the NeuroBridge wiki points its CNT links at it by changing two lines in its
`mkdocs.yml` (`extra.wiki.cnt_manual`): `url:` the site address with a trailing slash, and `style: site`.
