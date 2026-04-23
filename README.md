# GH-100

## What is GitHub?
Cloud-based DevOps platform that combines Git version control with collaboration, admin, product usage, licensing, and security

To use GitHub, you need to create an account on GitHub

Create an account
Create a new repository
add readme file
make first commit
view commit history


## Components of the GitHub flow

Create a branch from main
commit changes to the branch
open a pull request - this allows for a request for a review of newly introduced changes
Request reviews
Merge into main
Deploy changes.

## GitHub as a collaborative platform
Practice

create an issue for a tast or bug
assign the issue to a team member
Link the issue to a pull request
Discuss changes in PR comments
Close the issue when merged

# Github platform management
Platform management ensures repo are structured, access is controlled, and policies are enforced consistently

# What is GitHub Administration
GitHub administration focuses on managing identities, permissions, policies, and security controls accross repos and orgs

# Part 2 - Adminitration an Product Feature

# M5 - Setting secutiry Policies
Security policicy is how code is protected and who can contribute.

## Create and manage Repo Rulesets

## Reporting and Logging

## Remove commit History - Exercise

# M6: User Identity and Access Management

## User Identification
Authentication verifies user identity using password, MFA, tokens, or SSO (enterprise)

Enable MFA requirements
Configure SAML/OIDC
test authentication flow

## User Authorization
Authorization determines what authenticated users can do.

## Team Synchronization
Team synchronization authomatically maps IdP groups to GitHub teams - eliminating manual user management.

# M7: GitHub Enterprise Features
What it is
GitHub Enterprise is GitHub’s offering for large organizations that require advanced security, identity, compliance, and governance beyond standard GitHub Team plans.
It is available in:

GitHub Enterprise Cloud (hosted by GitHub)
GitHub Enterprise Server (self‑hosted)


Key Feature Categories
1. Advanced Security
GitHub Enterprise includes GitHub Advanced Security (GHAS), which enables:

Code scanning (CodeQL)
Secret scanning
Dependency scanning
Dependabot security updates

Why it matters

Detects vulnerabilities early in the SDLC
Helps meet security and compliance requirements (ISO, SOC 2)
Reduces risk of production incidents

Example
A secret accidentally committed (AWS key, API token) is detected and flagged automatically.

2. Identity & Access Management

SAML SSO
SCIM provisioning
Managed Users
Enterprise‑wide access policies

Why it matters

Centralized identity control
Reduced insider risk
Automated onboarding/offboarding


3. Compliance & Governance

Audit logs (organization & enterprise level)
Policy enforcement across organizations
Centralized billing and usage reporting

Why it matters

Supports audits and regulatory requirements
Enforces consistent controls across teams
Improves visibility across the enterprise


4. Enterprise Administration

Enterprise account spanning multiple organizations
Delegated organization management
Central policy enforcement

Why it matters
Large companies often run dozens or hundreds of repositories and teams, making per‑org management impractical.GitHub Enterprise Features
What it is
GitHub Enterprise is GitHub’s offering for large organizations that require advanced security, identity, compliance, and governance beyond standard GitHub Team plans.
It is available in:

GitHub Enterprise Cloud (hosted by GitHub)
GitHub Enterprise Server (self‑hosted)


Key Feature Categories
1. Advanced Security
GitHub Enterprise includes GitHub Advanced Security (GHAS), which enables:

Code scanning (CodeQL)
Secret scanning
Dependency scanning
Dependabot security updates

Why it matters

Detects vulnerabilities early in the SDLC
Helps meet security and compliance requirements (ISO, SOC 2)
Reduces risk of production incidents

Example
A secret accidentally committed (AWS key, API token) is detected and flagged automatically.

2. Identity & Access Management

SAML SSO
SCIM provisioning
Managed Users
Enterprise‑wide access policies

Why it matters

Centralized identity control
Reduced insider risk
Automated onboarding/offboarding


3. Compliance & Governance

Audit logs (organization & enterprise level)
Policy enforcement across organizations
Centralized billing and usage reporting

Why it matters

Supports audits and regulatory requirements
Enforces consistent controls across teams
Improves visibility across the enterprise


4. Enterprise Administration

Enterprise account spanning multiple organizations
Delegated organization management
Central policy enforcement

Why it matters
Large companies often run dozens or hundreds of repositories and teams, making per‑org management impractical.

## Scale your enterprise deployment
What scaling means in GitHub context
Scaling is not just more repos — it’s about managing:

Multiple organizations
Thousands of users
Hundreds of teams
Automated workflows
Consistent security policies


Core Scaling Challenges
1. Organization Sprawl
Without governance:

Teams create orgs independently
Security policies diverge
Visibility is lost

✅ GitHub Enterprise solves this by:

Centralizing orgs under one Enterprise account
Applying shared policies
Delegating admin roles safely


2. User Lifecycle Management
Manual user management doesn’t scale.
✅ Use:

IdP‑driven provisioning
SCIM automation
Managed Users


3. Workflow Standardization
Large enterprises need:

Shared CI/CD patterns
Reusable GitHub Actions
Central policies for reviews and branch protection

✅ Enterprise supports:

Organization‑level action policies
Required workflows
Protected environments


4. Security at Scale
Security must be:

Automated
Consistent
Auditable

✅ Enterprise enables:

Enterprise‑wide security alerts
Central GHAS management
Audit logs across all orgs

## Github Enterprise Managed users
IdP = Identity provider.

Managed Users centralize identity management - ensuring all account are controlled via the org' IdP.

Managed Users mean GitHub accounts are fully controlled by your Identity Provider (IdP) instead of individual users.
Users:

Cannot create personal repos
Cannot sign in without SSO
Exist only within the enterprise context


How Managed Users Work
Identity Control

Users authenticate exclusively via IdP (Azure AD, Okta, etc.)
Usernames are enterprise‑controlled (e.g. @company)
Passwords are not stored in GitHub


Provisioning & De‑Provisioning

Users are created automatically via SCIM
When removed from IdP:

GitHub access is revoked immediately
Tokens and sessions are invalidated


Access Enforcement

Organization membership is centrally managed
Repo access flows through teams and IdP groups
No “shadow users” or orphaned accounts


# M8: GitHub Actions in the Enterprise
GitHub Actions enables automation for CI/CD, security scans and operational workflows.

## Manage actions and workflows
Workflows define automation steps in YAML files stored in repositories.
CI/CD pipelines
security scans
Infra Automation
Issue and release management

name.yml file in `.github/workflows/*.yml`

trigger
jobs
steps
actions
