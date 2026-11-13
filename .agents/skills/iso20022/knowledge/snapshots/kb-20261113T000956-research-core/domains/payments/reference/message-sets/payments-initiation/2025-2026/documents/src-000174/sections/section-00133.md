---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.9 PaymentMethod <PmtMtd>"]
file_pages: [200, 201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.9 PaymentMethod <PmtMtd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 200 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation27" on page 564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 564
   ClearingChannel <ClrChanl> [0..1] CodeSet 564
   ServiceLevel <SvcLvl> [0..*]  565
{Or     Code <Cd> [1..1] CodeSet 565
Or}     Proprietary <Prtry> [1..1] Text 565
   LocalInstrument <LclInstrm> [0..1]  565
{Or     Code <Cd> [1..1] CodeSet 566
Or}     Proprietary <Prtry> [1..1] Text 566
   SequenceType <SeqTp> [0..1] CodeSet 566
   CategoryPurpose <CtgyPurp> [0..1]  566
{Or     Code <Cd> [1..1] CodeSet 566
Or}     Proprietary <Prtry> [1..1] Text 567
3.4.3.7.12.9  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Specifies the means of payment that will be used to move the amount of money.
Datatype: "PaymentMethod4Code" on page 599
CodeName Name Definition
CHK Cheque Written order to a bank to pay a certain
amount of money from one person to
another person.
TRF CreditTransfer Transfer of an amount of money in the
books of the account servicer.
DD DirectDebit Collection of an amount of money from
the debtor's bank account by the
creditor. The amount of money and
dates of collections may vary.
TRA TransferAdvice Transfer of an amount of money in the
books of the account servicer. An advice
should be sent back to the account
owner.
3.4.3.7.12.10  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 200 March 2026
```

## File page 201

```text
MandateRelatedInformation <MndtRltdInf> contains one of the following
MandateRelatedData5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 202
     MandateIdentification <MndtId> [0..1] Text 204
     DateOfSignature <DtOfSgntr> [0..1] Date 204
     AmendmentIndicator <AmdmntInd> [0..1] Indicator 204
     AmendmentInformationDetails <AmdmntInfDtls> [0..1]  204
       OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 205
       OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 205
       OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 206
       OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
207
       OriginalDebtor <OrgnlDbtr> [0..1] ± 208
       OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
209
       OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 210
       OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
211
       OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 212
       OriginalFrequency <OrgnlFrqcy> [0..1] ± 212
       OriginalReason <OrgnlRsn> [0..1]  212
{Or         Code <Cd> [1..1] CodeSet 212
Or}         Proprietary <Prtry> [1..1] Text 212
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 213
     ElectronicSignature <ElctrncSgntr> [0..1] Text 213
     FirstCollectionDate <FrstColltnDt> [0..1] Date 213
     FinalCollectionDate <FnlColltnDt> [0..1] Date 213
     Frequency <Frqcy> [0..1] ± 213
     Reason <Rsn> [0..1]  213
{Or       Code <Cd> [1..1] CodeSet 214
Or}       Proprietary <Prtry> [1..1] Text 214
     TrackingDays <TrckgDays> [0..1] Text 214
Or}   CreditTransferMandate <CdtTrfMndt> [1..1] ± 214
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 201 March 2026
```

