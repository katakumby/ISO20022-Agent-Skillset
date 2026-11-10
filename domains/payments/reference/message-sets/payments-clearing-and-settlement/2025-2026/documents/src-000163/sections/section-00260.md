---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.9 PaymentMethod <PmtMtd>"]
file_pages: [376, 377]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.9 PaymentMethod <PmtMtd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 376 to 377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 376

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
4.4.3.27.9  PaymentMethod <PmtMtd>
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
4.4.3.27.10  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
376 March 2026
```

## File page 377

```text
MandateRelatedInformation <MndtRltdInf> contains one of the following
MandateRelatedData5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 378
     MandateIdentification <MndtId> [0..1] Text 380
     DateOfSignature <DtOfSgntr> [0..1] Date 380
     AmendmentIndicator <AmdmntInd> [0..1] Indicator 380
     AmendmentInformationDetails <AmdmntInfDtls> [0..1]  380
       OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 381
       OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 381
       OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 382
       OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C22,
C21
383
       OriginalDebtor <OrgnlDbtr> [0..1] ± 384
       OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C22,
C21
385
       OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 386
       OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C22,
C21
387
       OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 388
       OriginalFrequency <OrgnlFrqcy> [0..1] ± 388
       OriginalReason <OrgnlRsn> [0..1]  388
{Or         Code <Cd> [1..1] CodeSet 388
Or}         Proprietary <Prtry> [1..1] Text 388
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 389
     ElectronicSignature <ElctrncSgntr> [0..1] Text 389
     FirstCollectionDate <FrstColltnDt> [0..1] Date 389
     FinalCollectionDate <FnlColltnDt> [0..1] Date 389
     Frequency <Frqcy> [0..1] ± 389
     Reason <Rsn> [0..1]  389
{Or       Code <Cd> [1..1] CodeSet 390
Or}       Proprietary <Prtry> [1..1] Text 390
     TrackingDays <TrckgDays> [0..1] Text 390
Or}   CreditTransferMandate <CdtTrfMndt> [1..1] ± 390
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
377 March 2026
```

