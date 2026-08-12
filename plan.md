# Implementation Plan: Self-Service Customer Admin Portal

## Overview
Prove you can reduce support overhead by building tools enterprise teams can actually operate themselves, without opening a support ticket for routine admin tasks.

## Phase 1 — Happy Path
- `provisioning/`: endpoints to list/invite/remove users within the caller's own organization.
- `feature_flags/`: a simple per-tenant flag store (`GET/PUT /flags`) so an admin can toggle features without a deploy.
- Ship: an admin can invite a user and toggle a feature flag for their org.

## Phase 2 — Hardening
- `provisioning/`: enforce role checks (only org admins can invite/remove users) — reuse the RBAC pattern from the SSO project if built.
- `quotas/`: show current usage against plan limits (seats used, API calls this month) and block actions that would exceed quota, with a clear error rather than a silent failure.
- `audit/`: log every admin action (who changed what, when) visible to the org's own admins, not just internal ops.

## Phase 3 — Production-Grade
- `feature_flags/`: support gradual rollout (percentage-based or user-list-based flags), not just on/off.
- `support/`: integrated escalation — a "contact support" action that auto-attaches the relevant audit log context (recent actions, current plan/quota state) so the support team isn't starting from zero.
- `provisioning/`: bulk operations (CSV user import) with per-row validation and a clear partial-failure report.

## Testing & Deployment
- Test quota enforcement at the exact boundary (last allowed seat succeeds, next one is blocked with a clear message).
- Test that audit logs are immutable from the portal's own API (admins can read but not edit/delete their org's audit trail).
