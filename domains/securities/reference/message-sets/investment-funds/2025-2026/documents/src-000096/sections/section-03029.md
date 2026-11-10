---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.4 Message Building Blocks", "58.4.2 RequestDetails <ReqDtls>"]
file_pages: [4237, 4238]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.4.2 RequestDetails <ReqDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4237 to 4238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4237

```text
58.4.2 RequestDetails <ReqDtls>
Presence: [1..*]
Definition: Information to identify the order(s) for which the status is requested.
Impacted by: C8 "ReferenceElementRule"
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4237 May 2026
```

## File page 4238

```text
RequestDetails <ReqDtls> contains the following MessageAndBusinessReference15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1]  4239
{Or     PreviousReference <PrvsRef> [1..2] ± 4240
Or}     OtherReference <OthrRef> [1..2] ± 4240
   RelatedReference <RltdRef> [0..1] ± 4240
   OrderReference <OrdrRef> [0..*]  4240
     MasterReference <MstrRef> [0..1] Text 4242
     OrderReference <OrdrRef> [1..1] Text 4242
     ClientReference <ClntRef> [0..1] Text 4242
     CancellationReference <CxlRef> [0..1] Text 4242
     DealReference <DealRef> [0..1] Text 4243
     NonceIdentification <NonceId> [0..1] Text 4243
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C5 4243
       AccountIdentification <AcctId> [1..1] Text 4243
       AccountName <AcctNm> [0..1] Text 4244
       AccountDesignation <AcctDsgnt> [0..1] Text 4244
       OwnerIdentification <OwnrId> [0..*] ± 4244
       AccountServicer <AcctSvcr> [0..1] ± 4244
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4244
       SubAccountDetails <SubAcctDtls> [0..1] ± 4245
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4245
     FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C4 4245
       Identification <Id> [1..1]  4247
{Or         ISIN <ISIN> [1..1] IdentifierSet 4247
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4248
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4248
Or         RIC <RIC> [1..1] IdentifierSet 4248
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4248
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4248
Or         CTA <CTA> [1..1] IdentifierSet 4248
Or         QUICK <QUICK> [1..1] IdentifierSet 4248
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4249
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4238 May 2026
```

