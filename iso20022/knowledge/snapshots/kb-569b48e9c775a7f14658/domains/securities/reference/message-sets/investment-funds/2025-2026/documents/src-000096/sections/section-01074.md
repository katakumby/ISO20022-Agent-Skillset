---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.4 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "39.4.15.4.7 SettlementPartiesDetails <SttlmPtiesDtls>", "39.4.15.4.7.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [1481]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.4.7.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1481 to 1481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1481

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters27
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1481
   TradeTransactionCondition <TradTxCond> [0..*] ± 1482
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1482
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1482
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C6, C11,
C17,
C18,
C19,
C20,
C21
1482
     Depository <Dpstry> [0..1] ± 1484
     Party1 <Pty1> [0..1] ± 1485
     Party2 <Pty2> [0..1] ± 1485
     Party3 <Pty3> [0..1] ± 1485
     Party4 <Pty4> [0..1] ± 1486
     Party5 <Pty5> [0..1] ± 1486
39.4.15.4.7.1  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository or an International Central Securities
Depository.
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat28Choice" on page 5135 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  5136
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5136
     Identification <Id> [0..1] Text 5136
Or   Country <Ctry> [1..1] CodeSet C12 5136
Or   TypeAndIdentification <TpAndId> [1..1]  5136
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5137
     Identification <Id> [1..1] IdentifierSet C4 5137
Or}   Proprietary <Prtry> [1..1] ± 5137
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1481 May 2026
```

