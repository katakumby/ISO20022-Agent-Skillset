---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.9 PaymentMethod <PmtMtd>"]
file_pages: [331, 332]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.9 PaymentMethod <PmtMtd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 331 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

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
4.4.3.8.9.9  PaymentMethod <PmtMtd>
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
4.4.3.8.9.10  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 331 March 2026
```

## File page 332

```text
MandateRelatedInformation <MndtRltdInf> contains one of the following
MandateRelatedData5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 333
     MandateIdentification <MndtId> [0..1] Text 335
     DateOfSignature <DtOfSgntr> [0..1] Date 335
     AmendmentIndicator <AmdmntInd> [0..1] Indicator 335
     AmendmentInformationDetails <AmdmntInfDtls> [0..1]  335
       OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 336
       OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 336
       OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 337
       OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C18,
C17
338
       OriginalDebtor <OrgnlDbtr> [0..1] ± 339
       OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C18,
C17
340
       OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 341
       OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C18,
C17
342
       OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 343
       OriginalFrequency <OrgnlFrqcy> [0..1] ± 343
       OriginalReason <OrgnlRsn> [0..1]  343
{Or         Code <Cd> [1..1] CodeSet 343
Or}         Proprietary <Prtry> [1..1] Text 343
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 344
     ElectronicSignature <ElctrncSgntr> [0..1] Text 344
     FirstCollectionDate <FrstColltnDt> [0..1] Date 344
     FinalCollectionDate <FnlColltnDt> [0..1] Date 344
     Frequency <Frqcy> [0..1] ± 344
     Reason <Rsn> [0..1]  344
{Or       Code <Cd> [1..1] CodeSet 345
Or}       Proprietary <Prtry> [1..1] Text 345
     TrackingDays <TrckgDays> [0..1] Text 345
Or}   CreditTransferMandate <CdtTrfMndt> [1..1] ± 345
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 332 March 2026
```

