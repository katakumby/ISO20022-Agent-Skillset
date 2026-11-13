---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.9 SettlementTypeAndAdditionalParameters14"]
file_pages: [1540]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.9 SettlementTypeAndAdditionalParameters14

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1540 to 1540.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1540

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.9  SettlementTypeAndAdditionalParameters14
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesMovementType <SctiesMvmntTp> [0..1] CodeSet 1540
   Payment <Pmt> [0..1] CodeSet 1540
   CommonIdentification <CmonId> [0..1] Text 1541
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1541
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1541
35.1.16.9.1  SecuritiesMovementType <SctiesMvmntTp>
Presence: [0..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 2113
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
35.1.16.9.2  Payment <Pmt>
Presence: [0..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 2058
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1540 March 2026
```

