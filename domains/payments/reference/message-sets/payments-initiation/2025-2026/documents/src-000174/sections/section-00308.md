---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>"]
file_pages: [446, 447]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 446 to 447.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
5.4.2.18.5  DirectDebitTransaction <DrctDbtTx>
Presence: [0..1]
Definition: Provides information specific to the direct debit mandate.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 446 March 2026
```

## File page 447

```text
DirectDebitTransaction <DrctDbtTx> contains the following DirectDebitTransaction12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateRelatedInformation <MndtRltdInf> [0..1]  C3, C4 448
     MandateIdentification <MndtId> [0..1] Text 450
     DateOfSignature <DtOfSgntr> [0..1] Date 450
     AmendmentIndicator <AmdmntInd> [0..1] Indicator 450
     AmendmentInformationDetails <AmdmntInfDtls> [0..1]  450
       OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 451
       OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 451
       OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 452
       OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
453
       OriginalDebtor <OrgnlDbtr> [0..1] ± 454
       OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
455
       OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 456
       OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
457
       OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 458
       OriginalFrequency <OrgnlFrqcy> [0..1] ± 458
       OriginalReason <OrgnlRsn> [0..1]  458
{Or         Code <Cd> [1..1] CodeSet 458
Or}         Proprietary <Prtry> [1..1] Text 458
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 459
     ElectronicSignature <ElctrncSgntr> [0..1] Text 459
     FirstCollectionDate <FrstColltnDt> [0..1] Date 459
     FinalCollectionDate <FnlColltnDt> [0..1] Date 459
     Frequency <Frqcy> [0..1] ± 459
     Reason <Rsn> [0..1]  459
{Or       Code <Cd> [1..1] CodeSet 460
Or}       Proprietary <Prtry> [1..1] Text 460
     TrackingDays <TrckgDays> [0..1] Text 460
   CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 460
   PreNotificationIdentification <PreNtfctnId> [0..1] Text 461
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 447 March 2026
```

