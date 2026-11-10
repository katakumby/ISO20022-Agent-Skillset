---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.10 ChargesInformation <ChrgsInf>", "3.4.2.10.3 Type <Tp>", "3.4.2.10.3.1 Code <Cd>"]
file_pages: [165, 166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.10.3.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 165 to 166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 165

```text
Type <Tp> contains one of the following ChargeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 165
Or}   Proprietary <Prtry> [1..1] ± 165
3.4.2.10.3.1  Code <Cd>
Presence: [1..1]
Definition: Charge type, in a coded form.
Datatype: "ExternalChargeType1Code" on page 1228
3.4.2.10.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of charge in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 1184 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1185
   Issuer <Issr> [0..1] Text 1185
3.4.2.11  RequestedCollectionDate <ReqdColltnDt>
Presence: [0..1]
Definition: Date and time at which the creditor requests that the amount of money is to be collected from
the debtor.
Datatype: "ISODate" on page 1239
3.4.2.12  DirectDebitTransaction <DrctDbtTx>
Presence: [0..1]
Definition: Provides information specific to the direct debit mandate.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
165 March 2026
```

## File page 166

```text
DirectDebitTransaction <DrctDbtTx> contains the following DirectDebitTransaction12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateRelatedInformation <MndtRltdInf> [0..1]  C3, C4 167
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
{Or         Code <Cd> [1..1] CodeSet 177
Or}         Proprietary <Prtry> [1..1] Text 177
       OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 178
     ElectronicSignature <ElctrncSgntr> [0..1] Text 178
     FirstCollectionDate <FrstColltnDt> [0..1] Date 178
     FinalCollectionDate <FnlColltnDt> [0..1] Date 178
     Frequency <Frqcy> [0..1] ± 178
     Reason <Rsn> [0..1]  178
{Or       Code <Cd> [1..1] CodeSet 179
Or}       Proprietary <Prtry> [1..1] Text 179
     TrackingDays <TrckgDays> [0..1] Text 179
   CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 179
   PreNotificationIdentification <PreNtfctnId> [0..1] Text 180
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
166 March 2026
```

