---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.85 SettlingCapacity7Choice", "35.1.16.85.2 Proprietary <Prtry>"]
file_pages: [1632]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.85.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1632 to 1632.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1632

```text
CodeName Name Definition
CUST SettlingCustodian Settlement party is a custodian. It
receives/delivers the securities and
carries out custodial duties.
SPRI SettlingPrincipal Settlement party is settling its own
trades.
RISP SettlingRisklessPrincipal Party settles trades that were
simultaneously offset.
35.1.16.85.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.86  SettlementTypeAndAdditionalParameters12
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1632
   Payment <Pmt> [1..1] CodeSet 1632
   CommonIdentification <CmonId> [0..1] Text 1633
35.1.16.86.1  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 2113
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
35.1.16.86.2  Payment <Pmt>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1632 March 2026
```

