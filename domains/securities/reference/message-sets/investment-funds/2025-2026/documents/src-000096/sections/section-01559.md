---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>", "44.4.4.9.15.4 DigitalNetworkFee <DgtlNtwkFee>", "44.4.4.9.15.4.2 Quantity <Qty>", "44.4.4.9.15.4.2.2 ProprietaryQuantity <PrtryQty>", "44.4.4.9.15.4.2.2.1 Quantity <Qty>"]
file_pages: [2187, 2188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15.4.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2187 to 2188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2187

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 2187
   QuantityType <QtyTp> [1..1] Text 2187
   Issuer <Issr> [1..1] Text 2187
   SchemeName <SchmeNm> [0..1] Text 2187
44.4.4.9.15.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
44.4.4.9.15.4.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
44.4.4.9.15.4.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
44.4.4.9.15.4.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
44.4.4.9.15.4.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
44.4.4.9.16  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2187 May 2026
```

## File page 2188

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 2189
   SettlementPlace <SttlmPlc> [1..1]  2189
     Party <Pty> [1..1]  2190
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2190
Or       ProprietaryIdentification <PrtryId> [1..1] ± 2190
Or       NameAndAddress <NmAndAdr> [1..1] ± 2191
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2191
     LEI <LEI> [0..1] IdentifierSet 2191
   SafekeepingPlace <SfkpgPlc> [0..1] ± 2191
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2192
   TradeTransactionCondition <TradTxCond> [0..*] ± 2192
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2192
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C31,
C32
2193
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2194
       PartyIdentification <PtyId> [1..1] ± 2194
       AccountIdentification <AcctId> [0..1] Text 2194
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2194
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2195
       PartyIdentification <PtyId> [1..1] ± 2195
       AccountIdentification <AcctId> [0..1] Text 2195
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2195
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2196
       PartyIdentification <PtyId> [1..1] ± 2196
       AccountIdentification <AcctId> [0..1] Text 2196
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2196
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2197
       PartyIdentification <PtyId> [1..1] ± 2197
       AccountIdentification <AcctId> [0..1] Text 2197
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2197
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2188 May 2026
```

