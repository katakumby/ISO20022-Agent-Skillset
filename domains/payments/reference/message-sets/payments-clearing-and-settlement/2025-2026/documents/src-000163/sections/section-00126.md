---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.12 DirectDebitTransaction <DrctDbtTx>", "3.4.2.12.1 MandateRelatedInformation <MndtRltdInf>", "3.4.2.12.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "3.4.2.12.1.4.9 OriginalFinalCollectionDate <OrgnlFnlColltnDt>"]
file_pages: [177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.12.1.4.9 OriginalFinalCollectionDate <OrgnlFnlColltnDt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 177 to 177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 177

```text
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.2.12.1.4.9  OriginalFinalCollectionDate <OrgnlFnlColltnDt>
Presence: [0..1]
Definition: Original final collection date that has been modified.
Datatype: "ISODate" on page 1239
3.4.2.12.1.4.10  OriginalFrequency <OrgnlFrqcy>
Presence: [0..1]
Definition: Original frequency that has been modified.
OriginalFrequency <OrgnlFrqcy> contains one of the following elements (see "Frequency36Choice"
on page 1178 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 1179
Or   Period <Prd> [1..1]  1179
     Type <Tp> [1..1] CodeSet 1180
     CountPerPeriod <CntPerPrd> [1..1] Quantity 1180
Or}   PointInTime <PtInTm> [1..1]  1180
     Type <Tp> [1..1] CodeSet 1180
     PointInTime <PtInTm> [1..1] Text 1181
3.4.2.12.1.4.11  OriginalReason <OrgnlRsn>
Presence: [0..1]
Definition: Original reason for the mandate to allow the user to distinguish between different mandates
for the same creditor.
OriginalReason <OrgnlRsn> contains one of the following MandateSetupReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 177
Or}   Proprietary <Prtry> [1..1] Text 177
3.4.2.12.1.4.11.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the mandate setup, as published in an external reason code list.
Datatype: "ExternalMandateSetupReason1Code" on page 1231
3.4.2.12.1.4.11.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
177 March 2026
```

