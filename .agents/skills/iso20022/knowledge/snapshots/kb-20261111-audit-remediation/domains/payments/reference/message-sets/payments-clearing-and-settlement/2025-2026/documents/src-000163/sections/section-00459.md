---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.10 MandateRelatedInformation <MndtRltdInf>", "5.4.3.21.10.1 DirectDebitMandate <DrctDbtMndt>"]
file_pages: [632, 633]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.10.1 DirectDebitMandate <DrctDbtMndt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 632 to 633.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 632

```text
5.4.3.21.10.1  DirectDebitMandate <DrctDbtMndt>
Presence: [1..1]
Definition: Specific direct debit mandate data.
Impacted by: C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
632 March 2026
```

## File page 633

```text
DirectDebitMandate <DrctDbtMndt> contains the following MandateRelatedInformation16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 634
   DateOfSignature <DtOfSgntr> [0..1] Date 634
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 634
   AmendmentInformationDetails <AmdmntInfDtls> [0..1]  634
     OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 635
     OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 635
     OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 636
     OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C20,
C19
637
     OriginalDebtor <OrgnlDbtr> [0..1] ± 638
     OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C20,
C19
639
     OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 640
     OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C20,
C19
641
     OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 642
     OriginalFrequency <OrgnlFrqcy> [0..1] ± 642
     OriginalReason <OrgnlRsn> [0..1]  642
{Or       Code <Cd> [1..1] CodeSet 642
Or}       Proprietary <Prtry> [1..1] Text 642
     OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 643
   ElectronicSignature <ElctrncSgntr> [0..1] Text 643
   FirstCollectionDate <FrstColltnDt> [0..1] Date 643
   FinalCollectionDate <FnlColltnDt> [0..1] Date 643
   Frequency <Frqcy> [0..1] ± 643
   Reason <Rsn> [0..1]  643
{Or     Code <Cd> [1..1] CodeSet 644
Or}     Proprietary <Prtry> [1..1] Text 644
   TrackingDays <TrckgDays> [0..1] Text 644
Constraints
• AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
633 March 2026
```

