---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.12 DirectDebitTransaction <DrctDbtTx>", "3.4.2.12.1 MandateRelatedInformation <MndtRltdInf>"]
file_pages: [167, 168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.12.1 MandateRelatedInformation <MndtRltdInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 167 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 167

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreNotificationDate <PreNtfctnDt> [0..1] Date 181
3.4.2.12.1  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the direct debit mandate signed between the creditor and the
debtor.
Impacted by: C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
167 March 2026
```

## File page 168

```text
MandateRelatedInformation <MndtRltdInf> contains the following MandateRelatedInformation16
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 169
   DateOfSignature <DtOfSgntr> [0..1] Date 169
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 169
   AmendmentInformationDetails <AmdmntInfDtls> [0..1]  169
     OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 170
     OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 170
     OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 171
     OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C15,
C14
172
     OriginalDebtor <OrgnlDbtr> [0..1] ± 173
     OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C15,
C14
174
     OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 175
     OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C15,
C14
176
     OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 177
     OriginalFrequency <OrgnlFrqcy> [0..1] ± 177
     OriginalReason <OrgnlRsn> [0..1]  177
{Or       Code <Cd> [1..1] CodeSet 177
Or}       Proprietary <Prtry> [1..1] Text 177
     OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 178
   ElectronicSignature <ElctrncSgntr> [0..1] Text 178
   FirstCollectionDate <FrstColltnDt> [0..1] Date 178
   FinalCollectionDate <FnlColltnDt> [0..1] Date 178
   Frequency <Frqcy> [0..1] ± 178
   Reason <Rsn> [0..1]  178
{Or     Code <Cd> [1..1] CodeSet 179
Or}     Proprietary <Prtry> [1..1] Text 179
   TrackingDays <TrckgDays> [0..1] Text 179
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
168 March 2026
```

