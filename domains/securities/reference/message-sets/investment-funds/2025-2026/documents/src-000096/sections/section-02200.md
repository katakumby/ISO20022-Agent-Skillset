---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.16 TransactionOverhead <TxOvrhd>", "50.4.4.9.16.4 DigitalNetworkFee <DgtlNtwkFee>", "50.4.4.9.16.4.2 Quantity <Qty>", "50.4.4.9.16.4.2.2 ProprietaryQuantity <PrtryQty>", "50.4.4.9.16.4.2.2.1 Quantity <Qty>"]
file_pages: [3095, 3096]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.16.4.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3095 to 3096.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3095

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 3095
   QuantityType <QtyTp> [1..1] Text 3095
   Issuer <Issr> [1..1] Text 3095
   SchemeName <SchmeNm> [0..1] Text 3095
50.4.4.9.16.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
50.4.4.9.16.4.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
50.4.4.9.16.4.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
50.4.4.9.16.4.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
50.4.4.9.16.4.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
50.4.4.9.17  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3095 May 2026
```

## File page 3096

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 3097
   SettlementPlace <SttlmPlc> [1..1]  3097
     Party <Pty> [1..1]  3098
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 3098
Or       ProprietaryIdentification <PrtryId> [1..1] ± 3098
Or       NameAndAddress <NmAndAdr> [1..1] ± 3099
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3099
     LEI <LEI> [0..1] IdentifierSet 3099
   SafekeepingPlace <SfkpgPlc> [0..1] ± 3099
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3100
   TradeTransactionCondition <TradTxCond> [0..*] ± 3100
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3100
   ReceivingSideDetails <RcvgSdDtls> [1..1]  C31,
C32
3101
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3102
       PartyIdentification <PtyId> [1..1] ± 3102
       AccountIdentification <AcctId> [0..1] Text 3102
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3102
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3103
       PartyIdentification <PtyId> [1..1] ± 3103
       AccountIdentification <AcctId> [0..1] Text 3103
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3103
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3104
       PartyIdentification <PtyId> [1..1] ± 3104
       AccountIdentification <AcctId> [0..1] Text 3104
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3104
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3105
       PartyIdentification <PtyId> [1..1] ± 3105
       AccountIdentification <AcctId> [0..1] Text 3105
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3105
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3096 May 2026
```

