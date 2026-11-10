---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>", "5.4.2.18.5.1 MandateRelatedInformation <MndtRltdInf>", "5.4.2.18.5.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "5.4.2.18.5.1.4.12 OriginalTrackingDays <OrgnlTrckgDays>"]
file_pages: [459]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.5.1.4.12 OriginalTrackingDays <OrgnlTrckgDays>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 459 to 459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 459

```text
Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 610
5.4.2.18.5.1.4.12  OriginalTrackingDays <OrgnlTrckgDays>
Presence: [0..1]
Definition: Original number of tracking days that has been modified.
Datatype: "Exact2NumericText" on page 607
5.4.2.18.5.1.5  ElectronicSignature <ElctrncSgntr>
Presence: [0..1]
Definition: Additional security provisions, such as a digital signature, as provided by the debtor.
Datatype: "Max1025Text" on page 607
5.4.2.18.5.1.6  FirstCollectionDate <FrstColltnDt>
Presence: [0..1]
Definition: Date of the first collection of a direct debit as per the mandate.
Datatype: "ISODate" on page 603
5.4.2.18.5.1.7  FinalCollectionDate <FnlColltnDt>
Presence: [0..1]
Definition: Date of the final collection of a direct debit as per the mandate.
Datatype: "ISODate" on page 603
5.4.2.18.5.1.8  Frequency <Frqcy>
Presence: [0..1]
Definition: Regularity with which direct debit instructions are to be created and processed.
Frequency <Frqcy> contains one of the following elements (see "Frequency36Choice" on page 544 for
details)
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
5.4.2.18.5.1.9  Reason <Rsn>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 459 March 2026
```

