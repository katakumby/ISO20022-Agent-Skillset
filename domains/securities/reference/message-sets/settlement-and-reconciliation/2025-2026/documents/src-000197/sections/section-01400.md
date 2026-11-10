---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.3 ConsentStatus4Choice", "35.1.29.3.2 Reason <Rsn>", "35.1.29.3.2.1 Code <Cd>"]
file_pages: [1873]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.3.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1873 to 1873.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1873

```text
Reason <Rsn> contains the following ConsentReason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1873
{Or     Code <Cd> [1..1] CodeSet 1873
Or}     Proprietary <Prtry> [1..1] ± 1873
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1874
35.1.29.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Code <Cd> contains one of the following ConsentOrRejectionReason4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1873
Or}   Proprietary <Prtry> [1..1] ± 1873
35.1.29.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the counterparty response has a rejection status.
Datatype: "CounterpartyResponseStatusReason1Code" on page 2057
CodeName Name Definition
CPTR CounterpartyTransaction Specifies that the response is related to
an allegement from the counterparty.
CPCX CounterpartyCancellation Specifies that the response is related to
the cancellation request of the
counterparty.
CPMD CounterpartyModification Specifies that the response is related to
the modification request of the
counterparty.
35.1.29.3.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the counterparty response has a rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1873 March 2026
```

