---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.9 PaymentMethod <PmtMtd>"]
file_pages: [60, 61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.9 PaymentMethod <PmtMtd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 60 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation27" on page 1206 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 1206
   ClearingChannel <ClrChanl> [0..1] CodeSet 1207
   ServiceLevel <SvcLvl> [0..*]  1207
{Or     Code <Cd> [1..1] CodeSet 1207
Or}     Proprietary <Prtry> [1..1] Text 1207
   LocalInstrument <LclInstrm> [0..1]  1208
{Or     Code <Cd> [1..1] CodeSet 1208
Or}     Proprietary <Prtry> [1..1] Text 1208
   SequenceType <SeqTp> [0..1] CodeSet 1208
   CategoryPurpose <CtgyPurp> [0..1]  1208
{Or     Code <Cd> [1..1] CodeSet 1209
Or}     Proprietary <Prtry> [1..1] Text 1209
2.4.3.18.9  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Specifies the means of payment that will be used to move the amount of money.
Datatype: "PaymentMethod4Code" on page 1235
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
2.4.3.18.10  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
60 March 2026
```

## File page 61

```text
MandateRelatedInformation <MndtRltdInf> contains one of the following
MandateRelatedData5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 62
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
{Or         Code <Cd> [1..1] CodeSet 72
Or}         Proprietary <Prtry> [1..1] Text 72
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 73
     ElectronicSignature <ElctrncSgntr> [0..1] Text 73
     FirstCollectionDate <FrstColltnDt> [0..1] Date 73
     FinalCollectionDate <FnlColltnDt> [0..1] Date 73
     Frequency <Frqcy> [0..1] ± 73
     Reason <Rsn> [0..1]  73
{Or       Code <Cd> [1..1] CodeSet 74
Or}       Proprietary <Prtry> [1..1] Text 74
     TrackingDays <TrckgDays> [0..1] Text 74
Or}   CreditTransferMandate <CdtTrfMndt> [1..1] ± 74
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
61 March 2026
```

