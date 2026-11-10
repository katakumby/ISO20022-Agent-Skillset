---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.14 IdentificationSource3Choice", "35.1.14.14.1 Code <Cd>"]
file_pages: [1498]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.14.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1498 to 1498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1498

```text
35.1.14.14.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: "ExternalFinancialInstrumentIdentificationType1Code" on page 2065
35.1.14.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Datatype: "Max35Text" on page 2192
35.1.14.15  GenericIdentification37
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
35.1.14.15.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 2192
35.1.14.15.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 2192
35.1.14.16  References44Choice
Definition: Choice of reference.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OtherTransactionIdentification <OthrTxId> [1..1]  1499
     MessageNumber <MsgNb> [0..1] ± C20 1499
     Identification <Id> [1..1] Text 1499
Or   SecuritiesFinancingTransactionIdentification
<SctiesFincgTxId>
[1..1] ± 1499
Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] ± 1500
Or}   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1500
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1498 March 2026
```

