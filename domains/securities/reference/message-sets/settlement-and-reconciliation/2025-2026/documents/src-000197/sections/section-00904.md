---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types"]
file_pages: [1340]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35 Message Items Types

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1340 to 1340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1340

```text
35 Message Items Types
35.1 MessageComponents
35.1.1 Account
35.1.1.1  Account29
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1340
   AccountServicer <AcctSvcr> [0..1] ± 1340
35.1.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains the following elements (see "AccountIdentification26" on page 1346 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1]  1346
     Identification <Id> [1..1] Text 1347
35.1.1.1.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is, manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains one of the following elements (see
"PartyIdentification120Choice" on page 1689 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1689
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1689
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1690
35.1.1.2  SecuritiesAccount19
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1340 March 2026
```

