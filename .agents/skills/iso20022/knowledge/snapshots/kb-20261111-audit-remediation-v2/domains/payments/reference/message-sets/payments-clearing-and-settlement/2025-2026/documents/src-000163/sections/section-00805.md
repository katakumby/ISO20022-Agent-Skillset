---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.9 PaymentMethod <PmtMtd>"]
file_pages: [1089, 1090]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.9 PaymentMethod <PmtMtd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1089 to 1090.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1089

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
9.4.3.11.9  PaymentMethod <PmtMtd>
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
9.4.3.11.10  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1089 March 2026
```

## File page 1090

```text
MandateRelatedInformation <MndtRltdInf> contains one of the following
MandateRelatedData5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 1091
     MandateIdentification <MndtId> [0..1] Text 1093
     DateOfSignature <DtOfSgntr> [0..1] Date 1093
     AmendmentIndicator <AmdmntInd> [0..1] Indicator 1093
     AmendmentInformationDetails <AmdmntInfDtls> [0..1]  1093
       OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 1094
       OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 1094
       OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 1095
       OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C12,
C11
1096
       OriginalDebtor <OrgnlDbtr> [0..1] ± 1097
       OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C12,
C11
1098
       OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 1099
       OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C12,
C11
1100
       OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 1101
       OriginalFrequency <OrgnlFrqcy> [0..1] ± 1101
       OriginalReason <OrgnlRsn> [0..1]  1101
{Or         Code <Cd> [1..1] CodeSet 1101
Or}         Proprietary <Prtry> [1..1] Text 1101
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 1102
     ElectronicSignature <ElctrncSgntr> [0..1] Text 1102
     FirstCollectionDate <FrstColltnDt> [0..1] Date 1102
     FinalCollectionDate <FnlColltnDt> [0..1] Date 1102
     Frequency <Frqcy> [0..1] ± 1102
     Reason <Rsn> [0..1]  1102
{Or       Code <Cd> [1..1] CodeSet 1103
Or}       Proprietary <Prtry> [1..1] Text 1103
     TrackingDays <TrckgDays> [0..1] Text 1103
Or}   CreditTransferMandate <CdtTrfMndt> [1..1] ± 1103
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1090 March 2026
```

