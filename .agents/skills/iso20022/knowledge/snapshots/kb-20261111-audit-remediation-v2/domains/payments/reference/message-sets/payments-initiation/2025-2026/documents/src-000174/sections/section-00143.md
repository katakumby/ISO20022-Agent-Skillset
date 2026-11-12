---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.10 MandateRelatedInformation <MndtRltdInf>", "3.4.3.7.12.10.1 DirectDebitMandate <DrctDbtMndt>", "3.4.3.7.12.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "3.4.3.7.12.10.1.4.9 OriginalFinalCollectionDate <OrgnlFnlColltnDt>"]
file_pages: [212]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.10.1.4.9 OriginalFinalCollectionDate <OrgnlFnlColltnDt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 212 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 212

```text
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.3.7.12.10.1.4.9  OriginalFinalCollectionDate <OrgnlFnlColltnDt>
Presence: [0..1]
Definition: Original final collection date that has been modified.
Datatype: "ISODate" on page 603
3.4.3.7.12.10.1.4.10  OriginalFrequency <OrgnlFrqcy>
Presence: [0..1]
Definition: Original frequency that has been modified.
OriginalFrequency <OrgnlFrqcy> contains one of the following elements (see "Frequency36Choice"
on page 544 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 545
Or   Period <Prd> [1..1]  545
     Type <Tp> [1..1] CodeSet 546
     CountPerPeriod <CntPerPrd> [1..1] Quantity 546
Or}   PointInTime <PtInTm> [1..1]  546
     Type <Tp> [1..1] CodeSet 546
     PointInTime <PtInTm> [1..1] Text 547
3.4.3.7.12.10.1.4.11  OriginalReason <OrgnlRsn>
Presence: [0..1]
Definition: Original reason for the mandate to allow the user to distinguish between different mandates
for the same creditor.
OriginalReason <OrgnlRsn> contains one of the following MandateSetupReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 212
Or}   Proprietary <Prtry> [1..1] Text 212
3.4.3.7.12.10.1.4.11.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the mandate setup, as published in an external reason code list.
Datatype: "ExternalMandateSetupReason1Code" on page 595
3.4.3.7.12.10.1.4.11.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 212 March 2026
```

