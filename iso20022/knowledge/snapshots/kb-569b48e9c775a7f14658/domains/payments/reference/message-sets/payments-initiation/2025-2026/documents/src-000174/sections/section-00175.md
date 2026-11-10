---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.7 GarnishmentRemittance <GrnshmtRmt>", "3.4.3.7.12.11.2.7.1 Type <Tp>", "3.4.3.7.12.11.2.7.1.1 CodeOrProprietary <CdOrPrtry>", "3.4.3.7.12.11.2.7.1.1.1 Code <Cd>"]
file_pages: [252]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.7.1.1.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 252 to 252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 252

```text
3.4.3.7.12.11.2.7.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Garnishment type in a coded form.
Would suggest this to be an External Code List to contain:
GNCS    Garnishment from a third party payer for Child Support
GNDP    Garnishment from a Direct Payer for Child Support
GTPP     Garnishment from a third party payer to taxing agency.
Datatype: "ExternalGarnishmentType1Code" on page 594
3.4.3.7.12.11.2.7.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of garnishment.
Datatype: "Max35Text" on page 609
3.4.3.7.12.11.2.7.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the garnishment type.
Datatype: "Max35Text" on page 609
3.4.3.7.12.11.2.7.2  Garnishee <Grnshee>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the
garnisher.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 252 March 2026
```

