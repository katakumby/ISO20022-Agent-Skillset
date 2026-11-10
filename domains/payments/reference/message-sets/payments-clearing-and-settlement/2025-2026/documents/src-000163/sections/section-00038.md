---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.10 MandateRelatedInformation <MndtRltdInf>", "2.4.3.18.10.1 DirectDebitMandate <DrctDbtMndt>"]
file_pages: [62, 63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.10.1 DirectDebitMandate <DrctDbtMndt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 62 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 62

```text
2.4.3.18.10.1  DirectDebitMandate <DrctDbtMndt>
Presence: [1..1]
Definition: Specific direct debit mandate data.
Impacted by: C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
62 March 2026
```

## File page 63

```text
DirectDebitMandate <DrctDbtMndt> contains the following MandateRelatedInformation16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 64
   DateOfSignature <DtOfSgntr> [0..1] Date 64
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 64
   AmendmentInformationDetails <AmdmntInfDtls> [0..1]  64
     OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 65
     OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 65
     OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 66
     OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
67
     OriginalDebtor <OrgnlDbtr> [0..1] ± 68
     OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
69
     OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 70
     OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
71
     OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 72
     OriginalFrequency <OrgnlFrqcy> [0..1] ± 72
     OriginalReason <OrgnlRsn> [0..1]  72
{Or       Code <Cd> [1..1] CodeSet 72
Or}       Proprietary <Prtry> [1..1] Text 72
     OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 73
   ElectronicSignature <ElctrncSgntr> [0..1] Text 73
   FirstCollectionDate <FrstColltnDt> [0..1] Date 73
   FinalCollectionDate <FnlColltnDt> [0..1] Date 73
   Frequency <Frqcy> [0..1] ± 73
   Reason <Rsn> [0..1]  73
{Or     Code <Cd> [1..1] CodeSet 74
Or}     Proprietary <Prtry> [1..1] Text 74
   TrackingDays <TrckgDays> [0..1] Text 74
Constraints
• AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
63 March 2026
```

