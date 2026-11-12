---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.4 Message Building Blocks", "65.4.2 RequestDetails <ReqDtls>"]
file_pages: [4307, 4308]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.4.2 RequestDetails <ReqDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4307 to 4308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4307

```text
65.4.2 RequestDetails <ReqDtls>
Presence: [1..*]
Definition: Information to identify the order confirmation for which the status is requested.
Impacted by: C8 "ReferenceElementRule"
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4307 May 2026
```

## File page 4308

```text
RequestDetails <ReqDtls> contains the following MessageAndBusinessReference15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1]  4309
{Or     PreviousReference <PrvsRef> [1..2] ± 4310
Or}     OtherReference <OthrRef> [1..2] ± 4310
   RelatedReference <RltdRef> [0..1] ± 4310
   OrderReference <OrdrRef> [0..*]  4310
     MasterReference <MstrRef> [0..1] Text 4312
     OrderReference <OrdrRef> [1..1] Text 4312
     ClientReference <ClntRef> [0..1] Text 4312
     CancellationReference <CxlRef> [0..1] Text 4312
     DealReference <DealRef> [0..1] Text 4313
     NonceIdentification <NonceId> [0..1] Text 4313
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C5 4313
       AccountIdentification <AcctId> [1..1] Text 4313
       AccountName <AcctNm> [0..1] Text 4314
       AccountDesignation <AcctDsgnt> [0..1] Text 4314
       OwnerIdentification <OwnrId> [0..*] ± 4314
       AccountServicer <AcctSvcr> [0..1] ± 4314
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4314
       SubAccountDetails <SubAcctDtls> [0..1] ± 4315
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4315
     FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C4 4315
       Identification <Id> [1..1]  4317
{Or         ISIN <ISIN> [1..1] IdentifierSet 4317
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4318
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4318
Or         RIC <RIC> [1..1] IdentifierSet 4318
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4318
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4318
Or         CTA <CTA> [1..1] IdentifierSet 4318
Or         QUICK <QUICK> [1..1] IdentifierSet 4318
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4319
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4308 May 2026
```

