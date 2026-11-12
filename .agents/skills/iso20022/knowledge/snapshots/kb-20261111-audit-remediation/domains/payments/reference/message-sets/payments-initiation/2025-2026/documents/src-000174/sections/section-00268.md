---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.7 GarnishmentRemittance <GrnshmtRmt>", "4.4.3.8.9.11.2.7.1 Type <Tp>", "4.4.3.8.9.11.2.7.1.1 CodeOrProprietary <CdOrPrtry>", "4.4.3.8.9.11.2.7.1.1.1 Code <Cd>"]
file_pages: [383]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.7.1.1.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 383 to 383.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
4.4.3.8.9.11.2.7.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Garnishment type in a coded form.
Would suggest this to be an External Code List to contain:
GNCS    Garnishment from a third party payer for Child Support
GNDP    Garnishment from a Direct Payer for Child Support
GTPP     Garnishment from a third party payer to taxing agency.
Datatype: "ExternalGarnishmentType1Code" on page 594
4.4.3.8.9.11.2.7.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of garnishment.
Datatype: "Max35Text" on page 609
4.4.3.8.9.11.2.7.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the garnishment type.
Datatype: "Max35Text" on page 609
4.4.3.8.9.11.2.7.2  Garnishee <Grnshee>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the
garnisher.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 383 March 2026
```

