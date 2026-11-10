---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>"]
file_pages: [4288, 4289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4288 to 4289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4288

```text
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
64.4.2 Reference <Ref>
Presence: [0..1]
Definition: Reference to the message or communication that was previously received.
Reference <Ref> contains one of the following elements (see "References64Choice" on page 4551 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RelatedReference <RltdRef> [1..2] ± 4551
Or}   OtherReference <OthrRef> [1..2] ± 4551
64.4.3 IndividualOrderConfirmationDetailsReport
<IndvOrdrConfDtlsRpt>
Presence: [1..*]
Definition: Status report details of an individual order confirmation.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4288 May 2026
```

## File page 4289

```text
IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt> contains the following
IndividualOrderConfirmationStatusAndReason3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 4290
   OrderReference <OrdrRef> [1..1] Text 4290
   Confirmation <Conf> [1..1]  4290
{Or     ConfirmationRejected <ConfRjctd> [1..10] ± C8 4291
Or     AmendmentRejected <AmdmntRjctd> [1..10] ± C8 4291
Or}     Status <Sts> [1..1] CodeSet 4292
   ClientReference <ClntRef> [0..1] Text 4292
   DealReference <DealRef> [0..1] Text 4292
   NonceIdentification <NonceId> [0..1] Text 4292
   StatusInitiator <StsInitr> [0..1] ± 4292
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C6 4293
     AccountIdentification <AcctId> [1..1] Text 4293
     AccountName <AcctNm> [0..1] Text 4293
     AccountDesignation <AcctDsgnt> [0..1] Text 4294
     OwnerIdentification <OwnrId> [0..*] ± 4294
     AccountServicer <AcctSvcr> [0..1] ± 4294
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4294
     SubAccountDetails <SubAcctDtls> [0..1] ± 4295
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4295
   FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C4 4295
     Identification <Id> [1..1]  4297
{Or       ISIN <ISIN> [1..1] IdentifierSet 4297
Or       SEDOL <SEDOL> [1..1] IdentifierSet 4298
Or       CUSIP <CUSIP> [1..1] IdentifierSet 4298
Or       RIC <RIC> [1..1] IdentifierSet 4298
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 4298
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 4298
Or       CTA <CTA> [1..1] IdentifierSet 4298
Or       QUICK <QUICK> [1..1] IdentifierSet 4298
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 4299
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4289 May 2026
```

