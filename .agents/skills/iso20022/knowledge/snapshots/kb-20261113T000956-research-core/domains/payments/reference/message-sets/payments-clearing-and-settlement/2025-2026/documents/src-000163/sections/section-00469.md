---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.10 MandateRelatedInformation <MndtRltdInf>", "5.4.3.21.10.1 DirectDebitMandate <DrctDbtMndt>", "5.4.3.21.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "5.4.3.21.10.1.4.12 OriginalTrackingDays <OrgnlTrckgDays>"]
file_pages: [643]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.10.1.4.12 OriginalTrackingDays <OrgnlTrckgDays>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 643 to 643.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 643

```text
Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 1246
5.4.3.21.10.1.4.12  OriginalTrackingDays <OrgnlTrckgDays>
Presence: [0..1]
Definition: Original number of tracking days that has been modified.
Datatype: "Exact2NumericText" on page 1243
5.4.3.21.10.1.5  ElectronicSignature <ElctrncSgntr>
Presence: [0..1]
Definition: Additional security provisions, such as a digital signature, as provided by the debtor.
Datatype: "Max1025Text" on page 1243
5.4.3.21.10.1.6  FirstCollectionDate <FrstColltnDt>
Presence: [0..1]
Definition: Date of the first collection of a direct debit as per the mandate.
Datatype: "ISODate" on page 1239
5.4.3.21.10.1.7  FinalCollectionDate <FnlColltnDt>
Presence: [0..1]
Definition: Date of the final collection of a direct debit as per the mandate.
Datatype: "ISODate" on page 1239
5.4.3.21.10.1.8  Frequency <Frqcy>
Presence: [0..1]
Definition: Regularity with which direct debit instructions are to be created and processed.
Frequency <Frqcy> contains one of the following elements (see "Frequency36Choice" on page 1178
for details)
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
5.4.3.21.10.1.9  Reason <Rsn>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
643 March 2026
```

