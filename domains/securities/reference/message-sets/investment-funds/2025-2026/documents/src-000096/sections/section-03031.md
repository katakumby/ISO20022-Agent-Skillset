---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.4 Message Building Blocks", "58.4.2 RequestDetails <ReqDtls>", "58.4.2.1 Reference <Ref>", "58.4.2.1.1 PreviousReference <PrvsRef>"]
file_pages: [4240, 4241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.4.2.1.1 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4240 to 4241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4240

```text
58.4.2.1.1  PreviousReference <PrvsRef>
Presence: [1..2]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
58.4.2.1.2  OtherReference <OthrRef>
Presence: [1..2]
Definition: Reference to a linked proprietary message or reference of a system that was previously
received.
OtherReference <OthrRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
58.4.2.2  RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
58.4.2.3  OrderReference <OrdrRef>
Presence: [0..*]
Definition: Unique and unambiguous identifiers of one or more individual order instructions or individual
order cancellation requests.
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4240 May 2026
```

## File page 4241

```text
OrderReference <OrdrRef> contains the following InvestmentFundOrder12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       ISIN <ISIN> [1..1] IdentifierSet 4247
Or       SEDOL <SEDOL> [1..1] IdentifierSet 4248
Or       CUSIP <CUSIP> [1..1] IdentifierSet 4248
Or       RIC <RIC> [1..1] IdentifierSet 4248
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 4248
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 4248
Or       CTA <CTA> [1..1] IdentifierSet 4248
Or       QUICK <QUICK> [1..1] IdentifierSet 4248
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 4249
Or       Dutch <Dtch> [1..1] IdentifierSet 4249
Or       Valoren <Vlrn> [1..1] IdentifierSet 4249
Or       Sicovam <SCVM> [1..1] IdentifierSet 4249
Or       Belgian <Belgn> [1..1] IdentifierSet 4249
Or       Common <Cmon> [1..1] IdentifierSet 4249
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4241 May 2026
```

