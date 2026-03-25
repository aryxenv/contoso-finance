# Roadmap

## Phases

Work the issues in phase order. Issues within a phase are independent — do them in parallel or any order.

### Phase 0 — Foundation

No dependencies. Do these first to set up the base.

| Issue | What                                                         |
| ----- | ------------------------------------------------------------ |
| #10   | Set up client test infrastructure (Vitest + Testing Library) |
| #17   | Add pre-commit hooks (Husky)                                 |
| #18   | Set up Prettier                                              |
| #20   | Add .env.example                                             |
| #21   | Enable FastAPI OpenAPI docs                                  |
| #28   | Add .dockerignore files                                      |

### Phase 1 — Core Backend

Initial Alembic migration is complete. These are all parallel.

| Issue | What                                      |
| ----- | ----------------------------------------- |
| #35   | User registration & session management    |
| #12   | Realistic payment processing flow         |
| #14   | Real settlement amounts from payment data |
| #16   | Real reporting data aggregation           |
| #11   | Expand server test coverage               |

### Phase 2 — Auth Completion & Cross-Domain

Serial chains from Phase 1.

| Issue | What                           | Depends on    |
| ----- | ------------------------------ | ------------- |
| #13   | Wire JWT auth to all endpoints | #35           |
| #15   | Cross-domain validation        | #12, #14      |
| #22   | Database seed script           | #12, #14, #16 |
| #34   | JWT hardening & refresh tokens | #13           |
| #33   | Rate limiting                  | #13           |

### Phase 3 — Frontend

All parallel. Can overlap with Phase 2 — APIs work today, backend improvements just make data more realistic.

| Issue | What             | Better after        |
| ----- | ---------------- | ------------------- |
| #26   | Billing page     | — (API is complete) |
| #23   | Payments page    | #12                 |
| #24   | Dashboard page   | #16                 |
| #27   | Reporting page   | #16                 |
| #25   | Settlements page | #14                 |

### Phase 4 — Quality & Docs

After features are built.

| Issue | What                        |
| ----- | --------------------------- |
| #9    | E2E testing with Playwright |
| #29   | CONTRIBUTING.md             |
| #19   | Architecture diagrams       |

### Phase 5 — Production Readiness

| Issue | What                            | Depends on |
| ----- | ------------------------------- | ---------- |
| #30   | Harden nginx config             | —          |
| #31   | Docker image build & push to CI | —          |
| #32   | Deployment pipeline             | #31        |

## Dependencies

**Hard** — will break or require rework if ignored:

```
#35 → #13
#13 → #34, #33
#12 + #14 → #15
#31 → #32
Frontend pages → #9
```

**Soft** — better in order, won't break if skipped:

```
#12 → #23 (payments page)
#14 → #25 (settlements page)
#16 → #24, #27 (dashboard, reporting pages)
#17, #18 → everything (nice to have hooks/formatting early)
```
