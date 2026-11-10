---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.18 RelatedQuantities <RltdQties>", "2.4.2.15.18.2.18.2 OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt>"]
file_pages: [212]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.18.2 OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 212 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 212

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
2.4.2.15.18.2.18.2  OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt>
Presence: [1..1]
Definition: Face amount and amortised value of security.
OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> contains the following elements (see
"OriginalAndCurrentQuantities1" on page 881 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 882
   AmortisedValue <AmtsdVal> [1..1] Amount 882
2.4.2.15.18.2.18.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary quantities specification defined in the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryQuantity1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 212
   Quantity <Qty> [1..1] Text 212
2.4.2.15.18.2.18.3.1  Type <Tp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.18.3.2  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity in free format.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.19  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Identification of a security, as assigned under a formal or proprietary identification scheme.
Impacted by: C8 "DescriptionPresenceRule", C9 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C24 "OtherIdentificationPresenceRule"
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
212 March 2026
```

