# Roadmap

## Phases

Work the issues in phase order. Issues within a phase are independent — do them in parallel or any order.

### Phase 1 — Core Backend

Initial Alembic migration is complete. These are all parallel.

| Issue | What                                      |
| ----- | ----------------------------------------- |
| #27   | User registration & session management    |
| #4    | Realistic payment processing flow         |
| #6    | Real settlement amounts from payment data |
| #8    | Real reporting data aggregation           |
| #3    | Expand server test coverage               |

### Phase 2 — Auth Completion & Cross-Domain

Serial chains from Phase 1.

| Issue | What                           | Depends on |
| ----- | ------------------------------ | ---------- |
| #5    | Wire JWT auth to all endpoints | #27        |
| #7    | Cross-domain validation        | #4, #6     |
| #14   | Database seed script           | #4, #6, #8 |
| #26   | JWT hardening & refresh tokens | #5         |
| #25   | Rate limiting                  | #5         |

### Phase 3 — Frontend

All parallel. Can overlap with Phase 2 — APIs work today, backend improvements just make data more realistic.

| Issue | What             | Better after        |
| ----- | ---------------- | ------------------- |
| #18   | Billing page     | — (API is complete) |
| #15   | Payments page    | #4                  |
| #16   | Dashboard page   | #8                  |
| #19   | Reporting page   | #8                  |
| #17   | Settlements page | #6                  |

### Phase 4 — Quality & Docs

After features are built.

| Issue | What                        |
| ----- | --------------------------- |
| #1    | E2E testing with Playwright |
| #21   | CONTRIBUTING.md             |
| #11   | Architecture diagrams       |

### Phase 5 — Production Readiness

| Issue | What                            | Depends on |
| ----- | ------------------------------- | ---------- |
| #22   | Harden nginx config             | —          |
| #23   | Docker image build & push to CI | —          |
| #24   | Deployment pipeline             | #23        |

## Dependencies

**Hard** — will break or require rework if ignored:

```
#27 → #5
#5 → #26, #25
#4 + #6 → #7
#23 → #24
Frontend pages → #1
```

**Soft** — better in order, won't break if skipped:

```
#4 → #15 (payments page)
#6 → #17 (settlements page)
#8 → #16, #19 (dashboard, reporting pages)
#9, #10 → everything (nice to have hooks/formatting early)
```
