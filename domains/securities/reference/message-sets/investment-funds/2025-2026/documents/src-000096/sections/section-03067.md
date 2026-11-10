---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.2 Structure"]
file_pages: [4285]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4285 to 4285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4285

```text
64.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <OrdrConfStsRpt> [1..1]  C5, C7
   MessageIdentification <MsgId> [1..1] ± 0
   Reference <Ref> [0..1] ± 0
   IndividualOrderConfirmationDetailsReport
<IndvOrdrConfDtlsRpt>
[1..*]  4288
     MasterReference <MstrRef> [0..1] Text 4290
     OrderReference <OrdrRef> [1..1] Text 4290
     Confirmation <Conf> [1..1]  4290
{Or       ConfirmationRejected <ConfRjctd> [1..10] ± C8 4291
Or       AmendmentRejected <AmdmntRjctd> [1..10] ± C8 4291
Or}       Status <Sts> [1..1] CodeSet 4292
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
{Or         ISIN <ISIN> [1..1] IdentifierSet 4297
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4298
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4298
Or         RIC <RIC> [1..1] IdentifierSet 4298
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4285 May 2026
```

