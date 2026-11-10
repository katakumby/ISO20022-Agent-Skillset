---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.8 Transaction <Tx>", "22.1.13.2.8.1 TradeDate <TradDt>"]
file_pages: [372]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.8.1 TradeDate <TradDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 372 to 372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 372

```text
Transaction <Tx> contains the following SecuritiesTransaction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeDate <TradDt> [1..1] DateTime 372
   TradingCapacity <TradgCpcty> [1..1] CodeSet 372
   Quantity <Qty> [1..1] ± 373
   DigitalTokenQuantity <DgtlTknQty> [0..*]  373
     Identifier <Idr> [1..1] IdentifierSet 373
     Unit <Unit> [0..1] Quantity 373
     Description <Desc> [0..1] Text 373
   DerivativeNotionalChange <DerivNtnlChng> [0..1] CodeSet 373
   Price <Pric> [1..1] ± 374
   NetAmount <NetAmt> [0..1] Amount 374
   TradeVenue <TradVn> [1..1] IdentifierSet 374
   CountryOfBranch <CtryOfBrnch> [0..1] CodeSet C4 375
   UpFrontPayment <UpFrntPmt> [0..1] ± 375
   TradePlaceMatchingIdentification <TradPlcMtchgId> [0..1] Text 376
   ComplexTradeComponentIdentification
<CmplxTradCmpntId>
[0..1] Text 376
22.1.13.2.8.1  TradeDate <TradDt>
Presence: [1..1]
Definition: Specifies the date/time on which the trade was executed.
Datatype: "ISODateTime" on page 449
22.1.13.2.8.2  TradingCapacity <TradgCpcty>
Presence: [1..1]
Definition: Indication of whether the transaction results from the reporting firm carrying out matched
principal trading or dealing on own account under the local regulation, or where the transaction does not
result from the reporting firm carrying out matched principal trading or dealing on own account, the field
shall indicate that the transaction was carried out under any other capacity.
Datatype: "RegulatoryTradingCapacity1Code" on page 443
CodeName Name Definition
MTCH MatchedPrincipal Transaction was carried out as a
matched principal trading.
DEAL DealOnOwnAccount Transaction was carried out as a deal
under own account.
AOTC AnyOtherCapacity Transaction was carried out as an agent.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
372 July 2025
```

