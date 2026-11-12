---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.16 TransactionOverhead <TxOvrhd>", "47.4.4.8.16.4 DigitalNetworkFee <DgtlNtwkFee>", "47.4.4.8.16.4.2 Quantity <Qty>", "47.4.4.8.16.4.2.2 ProprietaryQuantity <PrtryQty>", "47.4.4.8.16.4.2.2.1 Quantity <Qty>"]
file_pages: [2615, 2616]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.16.4.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2615 to 2616.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2615

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 2615
   QuantityType <QtyTp> [1..1] Text 2615
   Issuer <Issr> [1..1] Text 2615
   SchemeName <SchmeNm> [0..1] Text 2615
47.4.4.8.16.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
47.4.4.8.16.4.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
47.4.4.8.16.4.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
47.4.4.8.16.4.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
47.4.4.8.16.4.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
47.4.4.8.17  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2615 May 2026
```

## File page 2616

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 2617
   SettlementPlace <SttlmPlc> [1..1]  2617
     Party <Pty> [1..1]  2618
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2618
Or       ProprietaryIdentification <PrtryId> [1..1] ± 2618
Or       NameAndAddress <NmAndAdr> [1..1] ± 2619
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2619
     LEI <LEI> [0..1] IdentifierSet 2619
   SafekeepingPlace <SfkpgPlc> [0..1] ± 2619
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2620
   TradeTransactionCondition <TradTxCond> [0..*] ± 2620
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2620
   ReceivingSideDetails <RcvgSdDtls> [1..1]  C31,
C32
2621
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2622
       PartyIdentification <PtyId> [1..1] ± 2622
       AccountIdentification <AcctId> [0..1] Text 2622
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2622
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2623
       PartyIdentification <PtyId> [1..1] ± 2623
       AccountIdentification <AcctId> [0..1] Text 2623
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2623
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2624
       PartyIdentification <PtyId> [1..1] ± 2624
       AccountIdentification <AcctId> [0..1] Text 2624
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2624
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2625
       PartyIdentification <PtyId> [1..1] ± 2625
       AccountIdentification <AcctId> [0..1] Text 2625
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2625
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2616 May 2026
```

