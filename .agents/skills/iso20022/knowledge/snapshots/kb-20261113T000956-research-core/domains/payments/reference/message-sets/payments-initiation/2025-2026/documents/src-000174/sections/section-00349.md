---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.2.18.17.2.1.4 LineDetails <LineDtls>", "5.4.2.18.17.2.1.4.1 Identification <Id>", "5.4.2.18.17.2.1.4.1.1 Type <Tp>", "5.4.2.18.17.2.1.4.1.1.2 Issuer <Issr>"]
file_pages: [498]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.1.4.1.1.2 Issuer <Issr>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 498 to 498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 498

```text
Definition: Proprietary identification of the type of the remittance document.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.1.4.1.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the reference document line identificationtype.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.1.4.1.2  Number <Nb>
Presence: [0..1]
Definition: Identification of the type specified for the referred document line.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.1.4.1.3  RelatedDate <RltdDt>
Presence: [0..1]
Definition: Date associated with the referred document line.
Datatype: "ISODate" on page 603
5.4.2.18.17.2.1.4.2  Description <Desc>
Presence: [0..1]
Definition: Description associated with the document line.
Datatype: "Max2048Text" on page 608
5.4.2.18.17.2.1.4.3  Amount <Amt>
Presence: [0..1]
Definition: Provides details on the amounts of the document line.
Impacted by: C18 "RemittanceAmountAndTypeGuideline"
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 498 March 2026
```

