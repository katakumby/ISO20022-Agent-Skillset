---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.2 Structure"]
file_pages: [4234]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4234 to 4234.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4234

```text
58.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ReqForOrdrStsRpt> [1..1]  C6, C7
   MessageIdentification <MsgId> [1..1] ± 4236
   RequestDetails <ReqDtls> [1..*]  C8 4237
     Reference <Ref> [0..1]  4239
{Or       PreviousReference <PrvsRef> [1..2] ± 4240
Or}       OtherReference <OthrRef> [1..2] ± 4240
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
{Or           ISIN <ISIN> [1..1] IdentifierSet 4247
Or           SEDOL <SEDOL> [1..1] IdentifierSet 4248
Or           CUSIP <CUSIP> [1..1] IdentifierSet 4248
Or           RIC <RIC> [1..1] IdentifierSet 4248
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 4248
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4234 May 2026
```

