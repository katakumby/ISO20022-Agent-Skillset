---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties78", "7.1.26.1.6 Party5 <Pty5>"]
file_pages: [457]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.6 Party5 <Pty5>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 457 to 457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 457

```text
Party4 <Pty4> contains the following elements (see "PartyIdentificationAndAccount170" on page 431
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 431
   LEI <LEI> [0..1] IdentifierSet 431
   SafekeepingAccount <SfkpgAcct> [0..1] ± 431
   ProcessingIdentification <PrcgId> [0..1] Text 432
7.1.26.1.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 4.
Party5 <Pty5> contains the following elements (see "PartyIdentificationAndAccount170" on page 431
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 431
   LEI <LEI> [0..1] IdentifierSet 431
   SafekeepingAccount <SfkpgAcct> [0..1] ± 431
   ProcessingIdentification <PrcgId> [0..1] Text 432
7.1.27 Statement Update Type
7.1.27.1  StatementType7Choice
Definition: Choice of format for the statement type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 457
Or}   Proprietary <Prtry> [1..1] ± 457
7.1.27.1.1  Code <Cd>
Presence: [1..1]
Definition: Statement type expressed as an ISO 20022 code.
Datatype: "ExternalSecuritiesStatementType1Code" on page 507
7.1.27.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Statement type expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 457 March 2026
```

