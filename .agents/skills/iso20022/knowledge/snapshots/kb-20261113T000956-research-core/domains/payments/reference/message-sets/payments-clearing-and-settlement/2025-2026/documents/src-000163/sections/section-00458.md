---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.9 PaymentMethod <PmtMtd>"]
file_pages: [630, 631]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.9 PaymentMethod <PmtMtd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 630 to 631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 630

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
5.4.3.21.9  PaymentMethod <PmtMtd>
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
5.4.3.21.10  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
630 March 2026
```

## File page 631

```text
MandateRelatedInformation <MndtRltdInf> contains one of the following
MandateRelatedData5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 632
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
{Or         Code <Cd> [1..1] CodeSet 642
Or}         Proprietary <Prtry> [1..1] Text 642
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 643
     ElectronicSignature <ElctrncSgntr> [0..1] Text 643
     FirstCollectionDate <FrstColltnDt> [0..1] Date 643
     FinalCollectionDate <FnlColltnDt> [0..1] Date 643
     Frequency <Frqcy> [0..1] ± 643
     Reason <Rsn> [0..1]  643
{Or       Code <Cd> [1..1] CodeSet 644
Or}       Proprietary <Prtry> [1..1] Text 644
     TrackingDays <TrckgDays> [0..1] Text 644
Or}   CreditTransferMandate <CdtTrfMndt> [1..1] ± 644
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
631 March 2026
```

