---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks"]
file_pages: [4210, 4211, 4212]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4210 to 4212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4210

```text
C8 ReasonElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
C9 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
57.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
57.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
57.4.2 Reference <Ref>
Presence: [0..1]
Definition: Reference to the message or communication that was previously received.
Reference <Ref> contains one of the following elements (see "References64Choice" on page 4551 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RelatedReference <RltdRef> [1..2] ± 4551
Or}   OtherReference <OthrRef> [1..2] ± 4551
57.4.3 StatusReport <StsRpt>
Presence: [1..1]
Definition: Status of the order cancellation.
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4210 May 2026
```

## File page 4211

```text
StatusReport <StsRpt> contains one of the following Status42Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CancellationStatusReport <CxlStsRpt> [1..1]  4213
     MasterReference <MstrRef> [0..1] Text 4213
     CancellationStatus <CxlSts> [1..1]  4213
{Or       Status <Sts> [1..1] CodeSet 4214
Or}       Rejected <Rjctd> [1..1]  C8 4214
         Reason <Rsn> [0..1]  4214
{Or           Code <Cd> [1..1] CodeSet 4215
Or}           Proprietary <Prtry> [1..1] ± 4215
         AdditionalInformation <AddtlInf> [0..1] Text 4215
     StatusInitiator <StsInitr> [0..1] ± 4216
Or}   IndividualCancellationStatusReport <IndvCxlStsRpt> [1..*]  4216
     MasterReference <MstrRef> [0..1] Text 4218
     OrderReference <OrdrRef> [1..1] Text 4218
     ClientReference <ClntRef> [0..1] Text 4219
     NonceIdentification <NonceId> [0..1] Text 4219
     CancellationReference <CxlRef> [0..1] Text 4219
     CancellationStatus <CxlSts> [1..1]  4219
{Or       Status <Sts> [1..1] CodeSet 4219
Or}       Rejected <Rjctd> [1..1]  C8 4220
         Reason <Rsn> [0..1]  4220
{Or           Code <Cd> [1..1] CodeSet 4220
Or}           Proprietary <Prtry> [1..1] ± 4221
         AdditionalInformation <AddtlInf> [0..1] Text 4221
     StatusInitiator <StsInitr> [0..1] ± 4221
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C6 4222
       AccountIdentification <AcctId> [1..1] Text 4222
       AccountName <AcctNm> [0..1] Text 4222
       AccountDesignation <AcctDsgnt> [0..1] Text 4222
       OwnerIdentification <OwnrId> [0..*] ± 4223
       AccountServicer <AcctSvcr> [0..1] ± 4223
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4223
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4211 May 2026
```

## File page 4212

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SubAccountDetails <SubAcctDtls> [0..1] ± 4223
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4224
     FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C4 4224
       Identification <Id> [1..1]  4226
{Or         ISIN <ISIN> [1..1] IdentifierSet 4226
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4227
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4227
Or         RIC <RIC> [1..1] IdentifierSet 4227
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4227
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4227
Or         CTA <CTA> [1..1] IdentifierSet 4227
Or         QUICK <QUICK> [1..1] IdentifierSet 4227
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4228
Or         Dutch <Dtch> [1..1] IdentifierSet 4228
Or         Valoren <Vlrn> [1..1] IdentifierSet 4228
Or         Sicovam <SCVM> [1..1] IdentifierSet 4228
Or         Belgian <Belgn> [1..1] IdentifierSet 4228
Or         Common <Cmon> [1..1] IdentifierSet 4228
Or         DTI <DTI> [1..1] IdentifierSet 4228
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  4228
           Identification <Id> [1..1] Text 4229
           IdentificationSource <IdSrc> [1..1] ± 4229
       Name <Nm> [0..1] Text 4229
       ShortName <ShrtNm> [0..1] Text 4229
       SupplementaryIdentification <SplmtryId> [0..1] Text 4229
       ClassType <ClssTp> [0..1] Text 4229
       SecuritiesForm <SctiesForm> [0..1] CodeSet 4230
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4230
       ProductGroup <PdctGrp> [0..1] Text 4230
       SeriesIdentification <SrsId> [0..1]  C9 4230
         SeriesDate <SrsDt> [0..1] ± 4231
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4212 May 2026
```

