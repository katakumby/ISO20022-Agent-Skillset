---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.13 Intermediary44", "35.1.18.13.1 Identification <Id>"]
file_pages: [1683]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.13.1 Identification <Id>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1683 to 1683.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1683

```text
35.1.18.13.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of the intermediary.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 1671 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
35.1.18.13.2  Role <Role>
Presence: [0..1]
Definition: Function performed by the intermediary (investment funds).
Role <Role> contains one of the following elements (see "Role6Choice" on page 1549 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1549
Or   Proprietary <Prtry> [1..1] ± 1550
Or}   Text <Txt> [1..1] Text 1550
35.1.18.13.3  Account <Acct>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Account <Acct> contains the following elements (see "Account29" on page 1340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1340
   AccountServicer <AcctSvcr> [0..1] ± 1340
35.1.18.14  PartyIdentification15
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C7 1683
   Identification <Id> [1..1] Text 1684
35.1.18.14.1  Country <Ctry>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1683 March 2026
```

